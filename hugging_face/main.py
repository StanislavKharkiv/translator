from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from models.facebook_nllb import FacebookNLLBModel
from models.helsinki_nlp import HelsinkiNLPModel

app = FastAPI()


class TranslationRequest(BaseModel):
    text: str
    lang_pair: str
    model: str


class TranslationResponse(BaseModel):
    translation: List[str]


@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    text = request.text
    lang_pair = request.lang_pair
    model_name = request.model

    try:
        if model_name == "Helsinki-NLP":
            translator = HelsinkiNLPModel(lang_pair)
        elif model_name == "facebook-nllb":
            translator = FacebookNLLBModel(lang_pair)
        else:
            raise HTTPException(
                status_code=400, detail=f"Model {model_name} is not supported."
            )

        translation = translator.translate(text)
        return TranslationResponse(translation=translation)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Translation error: {str(e)}")
