from translation_app.models import Translation

#this function check if the same record is exist in our db or not
def check_if_record_already_exist_in_db(source_language,target_language,source_text):
    existing_translation = Translation.objects.filter(
                source_language=source_language,
                target_language=target_language,
                source_text=source_text
            ).first()
    if existing_translation:
        return existing_translation.translated_text
    else:
        return None