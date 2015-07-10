FROM ubuntu

MAINTAINER vinnie

RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip

ADD svwed

RUN git clone https://github.com/vingiarrusso/svwed.git

RUN pip install -r /svwed/requirements.txt

EXPOSE 8000

WORKDIR /svwed

CMD python server.py
