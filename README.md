## Projeto Desafio Django - Medical

- Projeto Django simulando abertura de agendamento consulta por um médico para um paciente.

#### Configuração Base
```shell 
- python 3.9.7
- Django 3.2.4
- Restframework 3.12.4
- djoser==2.1.0
- djangorestframework-simplejwt==4.8.0
- django_extensions
- drf_yasg = Documentação OpenAPI / Redoc
```

#### Libs auxiliares para código
```shell 
- pylint
- pre-commit
- black
- flask8
```

#### Database
```shell
- dj-database-url 
- PostgreSQL
- psycopg2
```

#### Templates
```shell
- django-bootstrap4 
```

#### Deploy
```shell
- heroku login
- heroku logs --tail 
- heroku run python manage.py migrate  
# Realizado configuração das variáveis de ambientes no settings do App no Heroku
```

#### Serviço monitoramento e código
```shell 
- sentry
- django-debug-toolbar
```


