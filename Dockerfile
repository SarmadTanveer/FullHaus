FROM python:3.8.16-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./ 

EXPOSE 3000/tcp

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:3000", "main:app"]

