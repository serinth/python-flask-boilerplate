FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/server.py"]
EXPOSE 8000