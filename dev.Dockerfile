# syntax=docker/dockerfile:1
FROM python:3.10.5
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]