from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view(["POST"])
def translate(request):
    text = request.data.get("text", "")
    lang_pair = request.data.get("lang_pair", "en-de")

    if not text:
        return Response({"error": "No text provided"}, status=400)

    try:
        response = requests.post(
            "http://helsinki-nlp:8001/translate/",
            json={"text": text, "lang_pair": lang_pair},
        )
        response.raise_for_status()
        return Response(response.json())
    except requests.exceptions.RequestException as e:
        return Response({"error": f"Translation service error: {e}"}, status=400)
