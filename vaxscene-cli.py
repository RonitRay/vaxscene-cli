import schedule
import requests
import time
import datetime
import json
import sys
from playsound import playsound

BASE_DOMAIN = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
DISTRICT_ID = '500'
AGE_BRACKET = 18

def search():
    found_flag = False

    today_date = datetime.datetime.now().strftime("%d-%m-%Y")
    url = BASE_DOMAIN + '?' + 'district_id=' + DISTRICT_ID + '&' + 'date=' + today_date
    print("searching \nURL: "+url+" at "+ str(datetime.datetime.now()))
        
    try:
        service_response = requests.get(url)
        
        if service_response.status_code == 200:
            json_body = service_response.json()
            
            for center in json_body["centers"]:
                sessions = center["sessions"]
                for session in sessions:
                    if (session["min_age_limit"] == AGE_BRACKET and session["available_capacity"] > 0):
                        found_flag = True
                        print("FOUND!!! :D \n")
                        print("on"+ session["date"] + ", Available: " + str(session["available_capacity"]) + "\n")
                        print(center["name"] + '\n' + center["address"] + '\n' + session["vaccine"])
                        print('\n')

            if found_flag == True:
                playsound('beep.mp3')
                playsound('beep.mp3')
                playsound('beep.mp3')
            else:
            	print("not found :( ")
        
        else:
            print("ERROR: " + str(service_response.status_code) + ":" + service_response.text)
        
    except:
        print("Unexpected error:", sys.exc_info()[0] + " at " + str(sys.exc_info()[2]))
    

schedule.every().minute.do(search)

while True:
    schedule.run_pending()
    time.sleep(1)

