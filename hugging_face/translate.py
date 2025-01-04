from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

# Define the FastAPI app
app = FastAPI()

# Load model and tokenizer
MODEL_NAME = "Helsinki-NLP/opus-mt-en-de"
tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
model = MarianMTModel.from_pretrained(MODEL_NAME)

# Request schema
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/")
def translate(request: TranslationRequest):
    print("Hello translate")
    try:
        inputs = tokenizer(request.text, return_tensors="pt", padding=True, truncation=True)
        outputs = model.generate(**inputs)
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
