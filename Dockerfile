# -*- Dockerfile -*-
FROM arm64v8/ubuntu
ENV LANG=C.UTF-8

ARG VERSION_PJSIP=2.10

RUN apt-get update && apt-get install -y \
    python2 \
    python-pip \
    libssl-dev \
    libsrtp2-dev \
    libgsm1-dev \
    libspeex-dev \
    portaudio19-dev \
    python2-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python2 -m pip install --upgrade pip setuptools
RUN python2 -m pip install paho-mqtt

RUN ln -s /usr/bin/python2 /usr/bin/python


RUN mkdir -p /opt/sip2mqtt

RUN wget -O /opt/sip2mqtt/sip2mqtt.py https://raw.githubusercontent.com/MartyTremblay/sip2mqtt/master/sip2mqtt.py

WORKDIR /

RUN wget -O /tmp/sip2mqtt.tar.gz "https://github.com/pjsip/pjproject/archive/${VERSION_PJSIP}.tar.gz" && tar -xzf /tmp/sip2mqtt.tar.gz -C / 

RUN cd "pjproject-${VERSION_PJSIP}" \
    && ./configure \
        --disable-libwebrtc \
        --with-external-srtp \
        --enable-shared \
        --disable-sound \
        --disable-sdl \
        --disable-speex-aec \
        --disable-video \
        --prefix=/usr \
    && make dep \
    && make \
    && make install \
    && cd pjsip-apps/src/python \
    && make \
    && make install \
    && cd .. \
    && rm -rf "pjproject-${VERSION_PJSIP}"

CMD ["/bin/sh", "-c", "python /opt/sip2mqtt/sip2mqtt.py -a $MQTT_DOMAIN -t $MQTT_PORT -u $MQTT_USERNAME -d $SIP_DOMAIN -n $SIP_USERNAME -s $SIP_PASSWORD"]
