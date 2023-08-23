from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from translation_app.models import Translation
from translation_app.serializers import TranslationSerializer
from translation_app.service import check_if_record_already_exist_in_db 

class TranslateAPIView(APIView):
    def get(self, request):
        source_text = request.query_params.get('text', '')
        source_language = request.query_params.get('source_language', 'auto')
        target_language = request.query_params.get('target_language', 'en')

        try:
            translated_text = check_if_record_already_exist_in_db(source_language,target_language,source_text)
            if translated_text:
                # If it exists in the database, return it
                return Response({'translation': translated_text}, status=status.HTTP_200_OK)
            translator = Translator()
            translated_text = translator.translate(source_text, src=source_language, dest=target_language).text

            # Save the translation to the database
            translation_data = {
                'source_language': source_language,
                'target_language': target_language,
                'source_text': source_text,
                'translated_text': translated_text,
            }
            serializer = TranslationSerializer(data=translation_data)
            
            if serializer.is_valid():
                serializer.save()  # Save the translation data
                return Response({'translation': translated_text}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
