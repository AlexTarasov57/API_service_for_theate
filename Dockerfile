FROM python:3.11.6-slim
LABEL maintainer="tarasov57228@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app/


RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

USER my_user