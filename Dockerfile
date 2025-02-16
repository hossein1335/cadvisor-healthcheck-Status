FROM harbor.devvops.ir/pub-repo/gcr.io/cadvisor/cadvisor:v0.50.0

WORKDIR /code

COPY exporter.py /code/exporter.py
COPY run.sh /code/run.sh

#RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install prometheus_client docker 
RUN apk update && apk add --no-cache python3 py3-pip \
    && pip3 install prometheus_client docker

#CMD ["-port=7010 -listen_ip=0.0.0.0 &"] 
