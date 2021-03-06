import os
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv
import dj_database_url
from functools import partial
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


BASE_DIR = Path(__file__).resolve().parent.parent

# Sentry Monitoramento de erros


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["*"]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = ["core"]

THIRD_PARTY_APPS = [
    "rest_framework",
    "djoser",
    "drf_yasg",
    "django_extensions",
    "bootstrap4",
    "crispy_forms",
    "social_django",
    "debug_toolbar",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

INTERNAL_IPS = config("INTERNAL_IPS", cast=Csv(), default="127.0.0.1")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Auth OAuth2
    "social_django.middleware.SocialAuthExceptionMiddleware",
    # Debug Toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "admin.urls"

# Conf da app debug toolbar
# if DEBUG:
#     INSTALLED_APPS.append('debug_toolbar')
#     MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware',)


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "admin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

default_db_url = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
parse_database = partial(dj_database_url.parse, conn_max_age=600)
DATABASES = {
    "default": config("DATABASE_URL", default=default_db_url, cast=parse_database)
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)


# Start forma autentica????o via JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": "Bearer",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Conf internacionaliza????o e hora
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Arquivos est??ticos(css, js, img, media)


STATIC_URL = "/static/"


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Serve ao WhiteNoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SENTRY_DSN = config("SENTRY_DSN", default=None)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# Customiza????o do User
AUTH_USER_MODEL = "core.DoctorUser"

# Redirect ap??s login
LOGIN_REDIRECT_URL = "/"

# Redirect ap??s logout
LOGOUT_REDIRECT_URL = "/login"

# Redirecionamento para acesso negado
LOGIN_URL = "/login"

# auth facebook
SOCIAL_AUTH_FACEBOOK_KEY = config("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = config("SOCIAL_AUTH_FACEBOOK_SECRET")

# auth twitter
SOCIAL_AUTH_TWITTER_KEY = ""
SOCIAL_AUTH_TWITTER_SECRET = ""

# auth google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_FACEBOOK_API_VERSION = "2.11"

CRISPY_TEMPLATE_PACK = "bootstrap4"
