# 📰 News Summarization Web App with T5-small

This project is an end-to-end **abstractive news summarization web application**, which leverages a fine-tuned `T5-small` transformer model on the **[XSum Dataset](https://huggingface.co/datasets/xsum)**.

It provides:
- A Django + Django REST Framework API to accept long-form text and return its summary
- An HTML frontend to allow users to input news and get the summarized output instantly
- A deployable setup for platforms like **Render**, using `gunicorn` as the WSGI HTTP server

---

## 🚀 Features

- 🔍 **T5-small** model fine-tuned on `XSum`
- 🔁 RESTful API using Django REST Framework
- 🧠 TensorFlow backend with Hugging Face `transformers` for summarization
- 🎯 HTML user interface for quick testing
- 🌐 Ready for cloud deployment (e.g., Render.com)

---

## 🧠 Model Details

- **Model**: [`t5-small`](fine tuned) is in the folder t5_model/ of this repo and also may check the Notebook trained on the P-100 of Kaggle
- **Dataset**: [`XSum`](https://huggingface.co/datasets/xsum)
- **Framework**: TensorFlow + Hugging Face Transformers
- Files saved: 
  - `tf_model.h5`
  - `tokenizer_config.json`
  - `tokenizer.json`
  - `config.json`
  - `special_tokens_map.json`
  - `spiece.model`

---

## 🏗️ Project Structure

