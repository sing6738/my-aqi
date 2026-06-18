import requests
import json
import datetime
import os

# ใช้ API จาก WAQI (aqicn.org)
# คุณสามารถเปลี่ยน CITY_ID เป็นเมืองที่คุณต้องการได้
CITY = "bangkok" 
TOKEN = os.getenv("AQI_TOKEN") # ดึงจาก GitHub Secrets

def update_data():
    if not TOKEN:
        print("Error: No API Token found.")
        return

    url = f"https://api.waqi.info/feed/{CITY}/?token={TOKEN}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok':
        aqi = data['data']['aqi']
        city_name = data['data']['city']['name']
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = {
            "city": city_name,
            "aqi": aqi,
            "time": now
        }

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Updated: {city_name} AQI is {aqi}")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    update_data()
