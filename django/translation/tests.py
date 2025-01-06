from rest_framework.test import APITestCase
from rest_framework import status


class TranslationAPITest(APITestCase):
    BASE_URL = "/api/translate/"

    def test_translation_success(self):
        url = "/api/translate/"
        data = {"text": "Hello, world!", "lang_pair": "en-de"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("translation", response.data)
        self.assertIsInstance(response.data["translation"], list)
        self.assertGreater(len(response.data["translation"]), 0)

    def test_translation_invalid_lang_pair(self):
        url = "/api/translate/"
        data = {"text": "Hello, world!", "lang_pair": "invalid-lang-pair"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_translation_missing_text(self):
        url = "/api/translate/"
        data = {"lang_pair": "en-de"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
