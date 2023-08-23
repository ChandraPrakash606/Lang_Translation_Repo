import json
from django.test import TestCase
from rest_framework import status
from django.urls import reverse

class TranslationAPITest(TestCase):
    def test_translation(self):
        # Test basic translation
        response = self.client.get(reverse('translate') + '?text=Hello&source_language=en&target_language=es')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"translation": "Hola"})

        # Test translation of a phrase
        response = self.client.get(reverse('translate') + '?text=How are you?&source_language=en&target_language=fr')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"translation": "Comment vas-tu?"})

        # Test translation of a paragraph
        response = self.client.get(reverse('translate') + '?text=This is a sample paragraph. It can contain multiple sentences and words.&source_language=en&target_language=es')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"translation": "Este es un párrafo de ejemplo. Puede contener múltiples oraciones y palabras."})

        # Test translation error (invalid language code)
        response = self.client.get(reverse('translate') + '?text=Hello&source_language=en&target_language=xyz')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {"error": "Invalid source or target language code."})

        # Test translation error (empty text)
        response = self.client.get(reverse('translate') + '?text=&source_language=en&target_language=es')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {"error": "Source text is empty."})

    
