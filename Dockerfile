FROM python:3.10-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /cars_api

COPY requirements.txt /cars_api/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /cars_api/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
