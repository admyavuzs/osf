FROM python:3.7.9-slim-buster

WORKDIR /opt/app/

COPY . /opt/app/

EXPOSE 8080

ENTRYPOINT ["python", "./server.py"]