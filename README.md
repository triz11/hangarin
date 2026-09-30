# HANGARIN

# A Django web application featuring a custom dark-mode authentication interface, Google and GitHub OAuth 2.0 integration, and live deployment on PythonAnywhere.

# Live Links:
>>Login Page: trizthan11.pythonanywhere.com/accounts/login/
>>Admin Panel: trizthan11.pythonanywhere.com/admin/

# Features:
>>Custom dark-themed login UI using Bootstrap 5.
>>OAuth 2.0 social login with Google and GitHub (django-allauth).
>>Standard username/password authentication fallback.
>>Automatic post-login redirection to the Django Admin dashboard.

# Tech Stack:
>>Backend: Python, Django 5.2, django-allauth, PyJWT
>>Frontend: HTML5, CSS3, Bootstrap 5
>>Hosting: PythonAnywhere

# Quick Start (Local Setup):
1. Clone repository
git clone https://github.com/<your-username>/hangarin.git
cd hangarin

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install django django-allauth PyJWT cryptography

4. Migrate database & run server
python manage.py migrate
python manage.py runserver
