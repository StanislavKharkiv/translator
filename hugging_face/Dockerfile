# Use the official Hugging Face Transformers image
FROM huggingface/transformers-pytorch-cpu

# Set the locale (optional but recommended)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install fastapi uvicorn sentencepiece

WORKDIR /app

EXPOSE 8001
