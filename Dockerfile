FROM nickgryg/alpine-pandas

RUN apk add --update \
    openjdk8-jre \
  && pip install --no-cache-dir --compile virtualenv \
  && rm -rf /var/cache/apk/*
  
  

WORKDIR /app

 # Install MINIFI 
RUN wget https://dlcdn.apache.org/nifi/1.16.0/minifi-1.16.0-bin.tar.gz \
	&& tar -xf minifi-1.16.0-bin.tar.gz \
	&& rm minifi-1.16.0-bin.tar.gz

ADD puhatu /opt/puhatu/
ADD start.sh /start.sh

RUN chmod +x /start.sh && mkdir /opt/puhatu/output/

ENTRYPOINT sh /start.sh
