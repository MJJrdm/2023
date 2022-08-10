#NBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNB FROM python:3.9-slim-bullseye
# for 42 server only
FROM python:3.9-slim-bullseye-dpmcv1

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U -i http://mirrors.cloud.tencent.com/pypi/simple --trusted-host mirrors.cloud.tencent.com

ADD . /code/

# ADD requirements.txt /code/

RUN pip install -r requirements.txt -i http://mirrors.cloud.tencent.com/pypi/simple --trusted-host mirrors.cloud.tencent.com


RUN python manage.py makemigrations
RUN python manage.py migrate
# CMD ['python3 manage.py collectstatic --noinput', '&&', '/bin/sh','-c','python manage.py runserver']
EXPOSE 8000
