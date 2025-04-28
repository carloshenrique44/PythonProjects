import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projeto_Restaurante.settings')

application = get_wsgi_application()
