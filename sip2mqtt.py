import sys
import sipcfg
import pjsua as pj
import threading
import time

# Method to print Log of callback class
def log_cb(level, str, len):
    print(str),

class SMCallCallback(pj.CallCallback):

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    def on_media_state(self):
        print "***** ON MEDIA STATE " , self.call.info()
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            print "Media is now active"
        else:
            print "Media is inactive"

    def on_state(self):
        print "**** ON STATE ", self.call
        print self.call.dump_status()
        print "Call with", self.call.info().remote_uri,
        print "is", self.call.info().state_text,
        print "last code =", self.call.info().last_code,
        print "(" + self.call.info().last_reason + ")"

        if self.call.info().state == pj.CallState.DISCONNECTED:
            print 'Current call has ended'


## Callback to receive events from account
class SMAccountCallback(pj.AccountCallback):

    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)

    def on_reg_state(self):
        print "Registration complete, status=", self.account.info().reg_status, \
              "(" + self.account.info().reg_reason + ")"

    # Notification on incoming call
    def on_incoming_call(self, call):
        print "Incoming call from ", call.info().remote_uri

# Lets start our main loop here
try:
    print "Allo Maksim"
    # Start of the Main Class
    # Create library instance of Lib class
    lib = pj.Lib()

    ua = pj.UAConfig()
    ua.user_agent = "SIP2MQTT"

    mc = pj.MediaConfig()
    mc.clock_rate = 8000

    lib.init(ua_cfg = ua, log_cfg = pj.LogConfig(level=3, callback=log_cb), media_cfg=mc)
    lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(sipcfg.trans_conf_port))
    lib.set_null_snd_dev()
    lib.start()

    acc_cfg = pj.AccountConfig()
    acc_cfg.id = "sip:" + sipcfg.username + "@" + sipcfg.domain
    acc_cfg.reg_uri = "sip:" + sipcfg.domain
    acc_cfg.auth_cred = [ pj.AuthCred(sipcfg.domain, sipcfg.username, sipcfg.password) ]
    acc_cfg.allow_contact_rewrite = False

    acc = lib.create_account(acc_cfg)
    acc_cb = SMAccountCallback(acc)
    acc.set_callback(acc_cb)

    print('\n')
    print "Registration Complete-----------"
    print('Status= ',acc.info().reg_status, \
         '(' + acc.info().reg_reason + ')')

    print "Press <ENTER> to quit"
    input = sys.stdin.readline().rstrip("\r\n")

    print" Unregistering ---------------------------"
    time.sleep(2)
    print "Destroying Libraries --------------"
    time.sleep(2)
    lib.destroy()
    lib = None
    sys.exit(0)

except pj.Error, e:
    print("Exception: " + str(e))
    lib.destroy()
    lib = None
    sys.exit(1)
