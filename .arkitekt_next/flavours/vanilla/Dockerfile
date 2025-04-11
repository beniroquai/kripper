FROM python:3.11-slim-buster

RUN pip install https://github.com/openUC2/UC2-REST/archive/refs/heads/master.zip

RUN pip install "arkitekt-next[all]>=0.8.82"

RUN mkdir /app
WORKDIR /app
COPY .arkitekt_next /app/.arkitekt_next
COPY app.py /app/app.py
