FROM python:3.7.9-slim-buster

RUN pip3 install prometheus_client

WORKDIR /opt/app/

COPY . /opt/app/

EXPOSE 8080

ENTRYPOINT ["python", "./server.py"]
