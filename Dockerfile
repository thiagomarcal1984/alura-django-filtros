FROM python:3
ADD . /code
WORKDIR /code

ENV DJANGO_SUPERUSER_USERNAME=thiago
ENV DJANGO_SUPERUSER_PASSWORD=thiago
ENV DJANGO_SUPERUSER_EMAIL=thiago@thiago.com

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN python manage.py collectstatic

EXPOSE 80

# CMD gunicorn alurareceita.wsgi --bind 0.0.0.0:80
CMD python manage.py runserver 0.0.0.0:80
