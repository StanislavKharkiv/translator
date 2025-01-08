from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
from typing import List

app = FastAPI()


# Define request and response schemas
class TranslationRequest(BaseModel):
    text: str
    lang_pair: str = "en-to-fr"


class TranslationResponse(BaseModel):
    translation: List[str]


models = {
    "en-de": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
    },
    "de-en": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en"),
    },
}


@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    lang_pair = request.lang_pair
    text = request.text
    if lang_pair not in models:
        try: 
            model = MarianMTModel.from_pretrained(f"Helsinki-NLP/opus-mt-{lang_pair}")
            tokenizer = MarianTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-{lang_pair}")
            models[lang_pair] = {"model": model, "tokenizer": tokenizer}
        except: raise HTTPException(
            status_code=400, detail=f"Language pair {lang_pair} not supported"
        )

    model = models[lang_pair]["model"]
    tokenizer = models[lang_pair]["tokenizer"]

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)

    translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return TranslationResponse(translation=translation)
