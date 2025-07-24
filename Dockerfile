FROM python:3.10-slim AS flask-app

WORKDIR /application

COPY application/requirements.txt .

RUN pip install -r requirements.txt

COPY application/. .

EXPOSE 5000

CMD ["python", "app.py"]
