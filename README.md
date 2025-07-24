# 📰 News Summarization Web App with T5-small

This is an end-to-end **abstractive news summarization web application**, powered by a fine-tuned `T5-small` model trained on the [XSum Dataset](https://huggingface.co/datasets/xsum). It accepts long-form news and returns a clean one line, context-aware summary.

---

## 🚀 Features

- 🔍 Transformer model (`T5-small`) fine-tuned on real-world news data
- 🔁 RESTful backend using Django + Django REST Framework
- 🧠 TensorFlow + Hugging Face `transformers` backend
- 💡 User-friendly HTML frontend for quick summarization
- ☁️ Cloud-ready deployment (e.g., Render.com using Gunicorn + Docker)
- ✅ Works with `.h5` and tokenizer files saved locally (`t5_model/`)

---

## 🧠 Model Details

- **Model**: [`t5-small`](https://huggingface.co/t5-small)  fine tuned on Xsum dataset afterwards
- **Training Dataset**: [`XSum`](https://huggingface.co/datasets/xsum)
- **Training Platform**: Kaggle (P100 GPU)
- **Frameworks Used**: TensorFlow 2.19.0, Hugging Face `transformers` 4.52.4, `sentencepiece`
- **Saved Artifacts**:
  - `tf_model.h5`
  - `tokenizer_config.json`
  - `tokenizer.json`
  - `config.json`
  - `special_tokens_map.json`
  - `spiece.model`

All artifacts are saved in the local folder: `t5_model/`

![alt text](<image_sam.jpg>)
---

## 🏗️ Project Structure

```bash
summarizer_model_drf/
├── summarizer_project/              # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── summarizer_app/                 # Django app for DRF logic
│   ├── views.py                    # T5-small inference logic
│   ├── urls.py               
├── templates/
│   └── index.html                  # Frontend interface
├── t5_model/                       # Folder with model + tokenizer
│   ├── tf_model.h5
│   ├── tokenizer_config.json
│   └── ...
├── Dockerfile                      # Docker setup (optional)
├── requirements.txt
├── runtime.txt                     # python-3.10.12 for Render compatibility
└── README.md
