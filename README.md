# pjsip-docker

Dockerfile for building pjsip and python_pjsip as a base for SIP applications.

This Dockerfile currently builds Debian "jessie" release with pjsip pre-compiled.
We apply a slight customization to the pjsip build to better support chan_respoke and
WebRTC in general by increasing the maximum number of ice candidates that pjsip allows.

## usage

A bundled python script [sip2mqtt.py](https://github.com/MartyTremblay/sip2mqtt) allows the monitoring of SIP connections and publishes the CallerID payload to an MQTT channel. The entrypoint command requires the following parametters:

```bash
-a MQTT_ADDRESS, --mqtt_address MQTT_ADDRESS
                    the MQTT broker address string
-t MQTT_PORT,    --mqtt_port MQTT_PORT
                    the MQTT broker port number
-u MQTT_USERNAME, --mqtt_username MQTT_USERNAME
                    the MQTT broker username
-p MQTT_PASSWORD, --mqtt_password MQTT_PASSWORD
                    the MQTT broker password
-d SIP_DOMAIN,    --sip_domain SIP_DOMAIN
                    the SIP domain
-n SIP_USERNAME,  --sip_username SIP_USERNAME
                    the SIP username
-s SIP_PASSWORD,  --sip_password SIP_PASSWORD
                    the SIP password
```                    
Example entrypoint cmd:
```bash
python /opt/sip2mqtt/sip2mqtt.py -t16491 -afoo.cloudmqtt.com -uSip2Mqtt -pSECRET -dfoo.voip.ms -nSUB_DID -sSECRET -vvv
```                   
More optional parametters can be provided and referenced by running python sip2mqtt.py -h

## license

[MIT](https://github.com/respoke/pjsip-docker/blob/master/LICENSE)


[respoke/pjsip]: https://hub.docker.com/r/respoke/pjsip/
