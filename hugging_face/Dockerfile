# Use the official Hugging Face Transformers image
FROM huggingface/transformers-pytorch-cpu

# Set the locale (optional but recommended)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Install required libraries
RUN pip install fastapi uvicorn sentencepiece

# Copy the translation script
COPY translate.py /app/translate.py

# Set the working directory
WORKDIR /app

EXPOSE 8001

ENTRYPOINT ["uvicorn", "translate:app", "--host", "0.0.0.0", "--port", "8001"]
