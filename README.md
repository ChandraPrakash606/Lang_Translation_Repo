# Lang_Translation_Repo
# virtualenv langvenv
# actiavet virtual env "source langvenv/bin/acivate"
# change directory "cd lang_translation"
# pip install -r requirements.txt
# run "python manage.py makemigrations"
# run "python manage.py migrate"
# run "python manage.py runserver"
# API curl is
# curl --location --request GET 'http://127.0.0.1:8000/api/translate/?text=i am fine&          source_language=en&target_language=es'
# for run testcaes 
# python manage.py test translation_app.tests