from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view(["POST"])
def translate(request):
    text = request.data.get("text", "")
    lang_pair = request.data.get("lang_pair")
    model = request.data.get("model") or "Helsinki-NLP"

    if not text or not lang_pair:
        return Response({"error": "Expected fields text and lang_pair"}, status=400)

    try:
        response = requests.post(
            "http://helsinki-nlp:8001/translate",
            json={"text": text, "lang_pair": lang_pair, "model": model},
        )
        response.raise_for_status()
        return Response(response.json())
    except requests.exceptions.RequestException as e:
        # print('DJANGO ', type(e), e.response.text)
        error_text = ""
        try:
            error_text = e.response.json()["detail"]["msg"]
        except:
            pass
        return Response(
            {"error": f"Translation service error. {error_text}"}, status=400
        )
