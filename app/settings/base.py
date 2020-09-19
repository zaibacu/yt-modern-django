import os

DEBUG = False

LOGIN_URL = "/api-auth/login/"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = "app.urls"
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static")
]

INSTALLED_APPS = [
    # Core Apps
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    # Third Party Apps
    "rest_framework",
    "rest_framework.authtoken",

    # Internal
    "crm",
    "frontend",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": ["templates"],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "data/db.sqlite3"
    }
}

