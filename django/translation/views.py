from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view(["POST"])
def translate(request):
    # Parse JSON body for 'text' key
    text = request.data.get("text", "")
    if not text:
        return Response({"error": "No text provided"}, status=400)

    # Forward the text to the translation service
    response = requests.post("http://helsinki-nlp:8001/translate/", json={"text": text})

    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({"error": "Translation failed"}, status=response.status_code)
