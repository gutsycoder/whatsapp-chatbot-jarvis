import requests
from notify_run import Notify
r=requests.get("https://api.covid19india.org/state_district_wise.json")
data=r.json()
notify = Notify()
notify.send("Active Cases in Lucknow is "+str(data["Uttar Pradesh"]["districtData"]["Lucknow"]["active"]))
print("Active Cases in Lucknow is "+str(data["Uttar Pradesh"]["districtData"]["Lucknow"]["active"]))
