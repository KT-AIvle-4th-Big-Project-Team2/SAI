from pathlib import Path
from datetime import timedelta

SELECT_DATABASE = 0 # 0: AWS MySQL 사용  //  1: Local MySQL 사용  //  2: Django의 기본 SQLite 사용

#커밋용
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#"C:\bigproject\sensitiveDatas\DB_info.txt"
#/home/ubuntu/setting/djangoSecretKey_info.txt

sensitiveDataPath = ("/home/ubuntu/key/DB_info.txt")
sensitiveData = open(sensitiveDataPath, 'r')
django_secretKey = sensitiveData.readline()
sensitiveData.close()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = django_secretKey[:-1]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1","3.38.115.132","43.202.42.122","subdomain.storeaivle.com","storeaivle.com",]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.forms',
    
    # 사이트 기능
    "account", # 로그인 및 계정 관련기능
    'board', # 자유 게시판
    'faq', # 자주 물어보는 질문
    'report', # 분석보고서 관련기능
    'suggestions', # 사용자 제안기능
    'announcement', # 공지게시판
    'consultBoard', # ?
    'userPage',
    'adminPage',
    'analysis',
    'fileupload',
    
    # rest API
    "rest_framework",
    #"rest_framework.authtoken", # django + REST framework Token authentication
    "corsheaders",
    
    # Token JWT 인증
    #'rest_framework_simplejwt'
]

sensitiveDataPath = ('/home/ubuntu/key/frontURL_info.txt')
sensitiveData = open(sensitiveDataPath, 'r')
frontURL = sensitiveData.readline()
sensitiveData.close()

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    frontURL[:-1],'http://127.0.0.1:3000', 'http://localhost:3000'
]

CORS_ORIGIN_WHITELIST = [
    frontURL[:-1],'http://127.0.0.1:3000', 'http://localhost:3000'
]

MIDDLEWARE = [
    # rest API를 위한 middleware
    'corsheaders.middleware.CorsMiddleware',
    
    # django 기본 middleware
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    
]

# CORS 설정
CORS_ALLOW_ALL_ORIGINS = False  # 모든 오리진 요청을 허용하지 않음
CORS_ALLOW_CREDENTIALS = True   # 인증된 요청을 허용

# 기존 CORS_ORIGIN_WHITELIST에서 중복되는 항목을 제거하고 CORS_ALLOWED_ORIGINS에 추가
CORS_ALLOWED_ORIGINS = [
    frontURL, 
    "http://localhost", 
    "http://127.0.0.1",
    "http://storeaivle.com",
    "http://localhost:3000",
    "http://3.38.115.132"
]

CORS_ORIGIN_WHITELIST = [
    frontURL, "http://localhost", "http://127.0.0.1","storeaivle.com","http://localhost:3000","http://3.38.115.132 "
]

ROOT_URLCONF = "dev.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dev.wsgi.application"

sensitiveDataPath = ('/home/ubuntu/key/DB_info.txt')
sensitiveData = open(sensitiveDataPath, 'r')
sensitiveDataList = []

while True:
    line = sensitiveData.readline()
    if not line: break
    else: sensitiveDataList.append(line)
sensitiveData.close()
sensitiveDataList

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if SELECT_DATABASE == 0 :
    DATABASES = {
        'default' : {
            'ENGINE': sensitiveDataList[0][:-1],    
            'NAME': sensitiveDataList[1][:-1],                  
            'USER': sensitiveDataList[2][:-1],                          
            'PASSWORD': sensitiveDataList[3][:-1],                  
            'HOST': sensitiveDataList[4][:-1],                     
            'PORT': sensitiveDataList[5][:-1],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
                'use_unicode': True,
            },                          
        }
    }
    
elif SELECT_DATABASE == 1:
    print
    DATABASES = { 
        'default': {
            'ENGINE': sensitiveDataList[6][:-1],
            'NAME': sensitiveDataList[7][:-1],
            'USER': sensitiveDataList[8][:-1],
            'PASSWORD': sensitiveDataList[9][:-1],
            'HOST': sensitiveDataList[10][:-1],
            'PORT': sensitiveDataList[11],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
                'collation' : 'utf8mb4_0900_ai_ci',
                'use_unicode': True,
            },
        }
    }
    
else: 
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "chinook.db",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'account.UserCustom'

# Django 보안 관련 설정

# REST_FRAMEWORK = {
#     # 'DEFAULT_PARSER_CLASSES': [
#     #     'rest_framework.parsers.JSONParser', # REST API가 입출력 할 기본 형식 설정
#     # ],
    
#     # 'DEFAULT_PERMISSION_CLASSES':[
#     #     'rest_framework.permissions.AllowAny',
#     # ],
    
#     # 'DEFAULT_AUTHENTICATON_CLASSES':[
#     #     'rest_framework.authentication.SessionAuthentication',  # REST FRAMEWORK의 SESSION ID 기반 로그인 및 보안 사용
        
#     # ]
# }

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication', # 제거
#         'rest_framework.authentication.BasicAuthentication',
#     ),
    # 나머지 설정...
# }

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


################################
#         쿠키 관련 설정
################################

#SESSION_COOKIE_SAMESITE = None
#SESSION_COOKIE_DOMAIN = 