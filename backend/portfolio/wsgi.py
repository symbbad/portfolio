"""
WSGI 설정 파일입니다.

이 파일은 WSGI 호출 가능한 객체를 'application'이라는 모듈 수준 변수로 노출합니다.
실제 운영 환경에서 WSGI 서버와 Django 애플리케이션 간의 통신을 담당합니다.

자세한 내용은 다음을 참조하세요:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Django 설정 모듈 경로 설정 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# WSGI 애플리케이션 객체 생성
# 이 객체는 WSGI 서버와 Django 코드 간의 통신을 처리합니다
application = get_wsgi_application()

# 실제 운영 환경에서는 다음과 같은 WSGI 서버들과 함께 사용할 수 있습니다:
# - Gunicorn
# - uWSGI  
# - Apache with mod_wsgi
