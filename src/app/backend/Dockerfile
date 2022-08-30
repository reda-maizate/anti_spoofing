FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get install \
    'ffmpeg'\
    'libsm6'\
    'libxext6' -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]