FROM ubuntu:16.10
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/server.py"]
