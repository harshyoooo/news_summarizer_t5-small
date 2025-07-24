from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf
import os

# === Load the model & tokenizer from your local 't5_model' directory === #
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 't5_model')

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

# === Constants === #
PREFIX = "summarize: "
MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 64

# === Inference Logic === #
def generate_summary(text):
    input_text = PREFIX + text.strip()
    inputs = tokenizer(
        input_text,
        return_tensors="tf",
        padding="max_length",
        truncation=True,
        max_length=MAX_INPUT_LENGTH
    )

    summary_ids = model.generate(
        input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=MAX_TARGET_LENGTH,
        num_beams=4,
        early_stopping=True,
        decoder_start_token_id=tokenizer.pad_token_id
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# === API View (POST /api/summarize/) === #
class SummarizeAPIView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        if not text.strip():
            return Response({"error": "No input text provided."}, status=400)
        summary = generate_summary(text)
        return Response({"summary": summary})

# === HTML Form View (/ or /summarize) === #
def index(request):
    summary = ""
    text = ""
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text.strip():
            summary = generate_summary(text)
    return render(request, "index.html", {"text": text, "summary": summary})
