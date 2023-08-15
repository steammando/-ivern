FROM python:3.11.2

COPY ./app /app
WORKDIR /app
 
RUN pip install -r requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 app.main:app