from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/m2m100_418M"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


class FacebookNLLBModel:
    def __init__(self, lang_pair):
        self.lang_pair = lang_pair

    def translate(self, text):
        try:
            lang = tokenizer.get_lang_id(self.lang_pair.split("-")[1])
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            outputs = model.generate(**inputs, forced_bos_token_id=lang)
            return tokenizer.batch_decode(outputs, skip_special_tokens=True)
        except Exception as e:
            raise Exception(str(e))
