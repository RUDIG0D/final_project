FROM ubuntu:22.04
MAINTAINER Ilia Smetanin 
RUN apt-get update -y
COPY . /apt/gsom_predictor
WORKDIR /apt/gsom_predictor
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py