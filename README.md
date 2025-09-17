# Django Google Playstore Search App

## Setup & Run

1. Create and activate virtualenv:
```bash
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate    # on Windows
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

3. Run migrations and create superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Import data from CSVs (adjust paths if different):
```bash
python manage.py import_googleplay_data --apps C:/Users/rajas/Downloads/django_googleplay_search/data/googleplaystore.csv --reviews C:/Users/rajas/Downloads/django_googleplay_search/data/googleplaystore_user_reviews.csv
```

5. Start the server:
```bash
python manage.py runserver
```

6. Access app at: http://127.0.0.1:8000/

