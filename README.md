# pjsip-docker

Dockerfile for building pjsip as a base for asterisk & chan_respoke.

This Dockerfile currently builds Debian "jessie" release with pjsip pre-compiled.
We apply a slight customization to the pjsip build to better support chan_respoke and
WebRTC in general by increasing the maximum number of ice candidates that pjsip allows.

## usage

To build this image, just clone this repo and build using docker:

    git clone https://github.com/respoke/pjsip-docker.git
    cd pjsip-docker
    docker build -t pjsip .

## license

[MIT](https://github.com/respoke/pjsip-docker/blob/master/LICENSE)


[respoke/pjsip]: https://hub.docker.com/r/respoke/pjsip/
