FROM python:3.8.13-slim-buster
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/server.py"]
EXPOSE 8000
