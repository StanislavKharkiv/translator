from transformers import MarianMTModel, MarianTokenizer

preloaded_models = {
    "Helsinki-NLP/opus-mt-en-de": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
    },
    "Helsinki-NLP/opus-mt-de-en": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en"),
    },
}


class HelsinkiNLPModel:
    def __init__(self, lang_pair):
        self.lang_pair = lang_pair
        self.model_name = f"Helsinki-NLP/opus-mt-{lang_pair}"
        if not self.model_name in preloaded_models:
            preloaded_models[self.model_name] = {
                "model": MarianMTModel.from_pretrained(self.model_name),
                "tokenizer": MarianTokenizer.from_pretrained(self.model_name),
            }

    def translate(self, text):
        inputs = preloaded_models[self.model_name]["tokenizer"](
            text, return_tensors="pt", padding=True, truncation=True
        )
        outputs = preloaded_models[self.model_name]["model"].generate(**inputs)
        return preloaded_models[self.model_name]["tokenizer"].batch_decode(
            outputs, skip_special_tokens=True
        )
