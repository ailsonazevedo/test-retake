FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=retakeprocess.settings

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app
COPY . /app

RUN python -m pip install --user pipenv \
    && python -m pipenv install --system --deploy \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "retakeprocess.wsgi"]