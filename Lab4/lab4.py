from sense_hat import SenseHat
import httplib
import urllib
import time
key = "54CDA6FJF4RCJ92C"

mykey = "E1KUNDON3N9T7KG7"

sense = SenseHat()

cmail = "justinhuang3@cmail.carleton.ca"
projectGroup = "L2_M_1"
ident = "d"

def updateTS():
    while True:
        params = urllib.urlencode({'field1': cmail, 'field2': projectGroup, 'field3': ident, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break

if __name__ == "__main__":
    while True:
        updateTS()
        events = sense.stick.get_events()
        if events:
            for event in events:
                if event.action != 'pressed':
                    continue
                elif event.direction == 'middle':
                    exit()