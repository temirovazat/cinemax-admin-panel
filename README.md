## Cinemax Admin Panel

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/temirovazat/cinemax-admin-panel/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/temirovazat/django_admin_panel)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/temirovazat/cinemax-admin-panel/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![tests](https://img.shields.io/static/v1?label=tests&message=%E2%9C%94%205%20|%20%E2%9C%98%200&color=critical)](https://github.com/temirovazat/cinemax-admin-panel/actions/workflows/main.yml)

### **Description**

_The goal of this project is to implement an administrator interface for uploading movies and editing their information. For this purpose, an administrative panel was developed based on the Django framework. PostgreSQL is used as the database. The project is prepared for deployment in a production environment via the NGINX web server. Postman is used to check the API's functionality._

### **Technologies**

```Python``` ```Django``` ```PostgreSQL``` ```NGINX``` ```Gunicorn``` ```Postman``` ```Docker```

### **How to run the project:**

Clone the repository and navigate to the ```/infra ``` directory:
```
git clone https://github.com/temirovazat/cinemax-admin-panel.git
```
```
cd cinemax-admin-panel/infra/
```

Create a .env file and add project settings:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=cinemax_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Django
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@mail.ru
DJANGO_SUPERUSER_PASSWORD=1234
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],django
DJANGO_SECRET_KEY=django-insecure-_o)z83b+i@jfjzbof_jn9#%dw*5q2yy3r6zzq-3azof#(vkf!#
```

Deploy and run the project in containers:
```
docker-compose up
```

Access the admin panel and enter the login (admin) and password (1234):
```
http://127.0.0.1/admin
```