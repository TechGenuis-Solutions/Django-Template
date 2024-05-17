FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . .
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
