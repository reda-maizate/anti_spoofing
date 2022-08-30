FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN apt-get update -y && apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]