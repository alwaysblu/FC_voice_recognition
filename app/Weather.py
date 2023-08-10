import requests
import json

latitude = "37.509948327436256"
longitude = "126.94367955256304"
key_dic = {"temperature": "온도", "windspeed": "풍속", "winddirection": "풍향", "weathercode": "날씨 코드", "time": "시간"}

def filter_key(key):
    keys = key_dic.keys()
    if key in keys:
        return True
    return False


def get_info():
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto')
    json_response = json.loads(response.text)
    info = json_response["current_weather"]
    print(change_key({k: v for k, v in info.items() if filter_key(k)}))

def change_key(dic):
    result = {}
    for old in key_dic.keys():
        result[key_dic[old]] = dic[old]
    return result

"""
{
  "latitude": 37.5,
  "longitude": 126.9375,
  "generationtime_ms": 0.8249282836914062,
  "utc_offset_seconds": 32400,
  "timezone": "Asia/Seoul",
  "timezone_abbreviation": "KST",
  "elevation": 42.0,
  "current_weather": {
    "temperature": 22.9,
    "windspeed": 7.8,
    "winddirection": 236,
    "weathercode": 53,
    "is_day": 0,
    "time": "2023-08-11T01:00"
  }
}
"""