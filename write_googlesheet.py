import requests
import datetime

def write_googlesheet(userID, idm):
    url = "https://maker.ifttt.com/trigger/Raspberry pi/with/key/cVp2xAidWLVQlbWsmfG4UX"
    
    payload = {"value1":str(userID),"value2":str(idm),"value3":str("temp")}
    response = requests.post(url,data=payload)

