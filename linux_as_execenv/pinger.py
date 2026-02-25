import requests
from datetime import datetime, timedelta
url_template = "https://simurg.space/gen_file?data=obs&date={date}"
current = datetime.now()
while True:
    date  = now.strftime("%Y-%m-%d")
    url = url_template.format(date = date)
    responce = requests.get(url = url, stream = True)
    print(f"For {date} got: ", responce)
    if responce.status_code == 200:
        print(f"Last available datea are for {date}")
        break
    else:
        now = current - timedelta(days = 1)



    
