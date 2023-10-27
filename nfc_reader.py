# -- coding: utf-8 --
import binascii
import nfc
import os
from sample_pub import mqtt_publish
from write_googlesheet import write_googlesheet

class MyCardReader(object):
    def on_connect(self,tag):
        userID = str(tag.ndef.records[0].text)
        idm = binascii.hexlify(tag.identifier).upper().decode("utf-8")
        mqtt_publish(userID, idm)
        #write_googlesheet(userID, idm)
        return True

    def read_id(self):
        try:
            clf = nfc.ContactlessFrontend('usb:001:003')
       	    clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

if __name__ == '__main__':
    cr = MyCardReader()
    while True:
        print("Please Touch")
        cr.read_id()
        print("Released")
        print("====")
