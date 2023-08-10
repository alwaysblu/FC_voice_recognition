import requests
import json

end_point = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
encoding_key = "ruDZVV4WtDXbgFl0WrfcIIhQftk5haooc3k%2FImpcR%2BYW536te5rk2bE2PMIdwfQKWI5Vn2TSqELGkanAMdqYyA%3D%3D"
decoding_key = "ruDZVV4WtDXbgFl0WrfcIIhQftk5haooc3k/ImpcR+YW536te5rk2bE2PMIdwfQKWI5Vn2TSqELGkanAMdqYyA=="

params = {
	'serviceKey': decoding_key,
	'returnType': 'json',
	'numOfRows': '100',
	'pageNo': '1',
	'sidoName': '서울',
	'ver': '1.0',
}

key_dic = {"sidoName": "시/도명", "stationName": "동/구명", "pm25Value": "미세먼지 수치", "pm25Grade": "미세먼지 등급", "dataTime": "측정시간"}

def filter_key(key):
    keys = key_dic.keys()
    if key in keys:
        return True
    return False

def get_info():
    response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params=params)
    json_response = json.loads(response.text)
    dust_infos = json_response["response"]["body"]["items"] 
    for info in dust_infos:
        print(change_key({k: v for k, v in info.items() if filter_key(k)}))

def change_key(dic):
    result = {}
    for old in key_dic.keys():
        result[key_dic[old]] = dic[old]
    return result

"""
{'response': 
    {'body': 
        {'totalCount': 40, 
        'items': [
                {'so2Grade': '1', 
                'coFlag': None, 
                'khaiValue': '-', 
                'so2Value': '0.003', 
                'coValue': '0.3', 
                'pm25Flag': '통신장애', 
                'pm10Flag': '통신장애', 
                'o3Grade': '1', 
                'pm10Value': '-', 
                'khaiGrade': None, 
                'pm25Value': '-', 
                'sidoName': '서울', 
                'no2Flag': None, 
                'no2Grade': '1', 
                'o3Flag': None, 
                'pm25Grade': None, 
                'so2Flag': None, 
                'dataTime': '2023-08-11 02:00', 
                'coGrade': '1', 
                'no2Value': '0.009', 
                'stationName': '중구', 
                'pm10Grade': None, 
                'o3Value': '0.021'}, 


                {'so2Grade': '1', 
                'coFlag': None, 
                'khaiValue': '-', 
                'so2Value': '0.003', 
                'coValue': '0.3', 
                'pm25Flag': '통신장애', 
                'pm10Flag': None, 
                'o3Grade': '1', 
                'pm10Value': '5', 
                'khaiGrade': None, 
                'pm25Value': '-', 
                'sidoName': '서울', 
                'no2Flag': None, 
                'no2Grade': '1', 
                'o3Flag': None, 
                'pm25Grade': None, 
                'so2Flag': None, 
                'dataTime': '2023-08-11 02:00', 
                'coGrade': '1', 
                'no2Value': '0.007', 
                'stationName': '한강대로', 
                'pm10Grade': None, 
                'o3Value': '0.028'}, 
                {'so2Grade': '1', 
                'coFlag': None, 
                'khaiValue': '-', 
                'so2Value': '0.003', 
                'coValue': '0.3', 
                'pm25Flag': None, 
                'pm10Flag': None, 
                'o3Grade': '1', 
                'pm10Value': '3', 
                'khaiGrade': None, 
                'pm25Value': '1', 
                'sidoName': '서울', 
                'no2Flag': None, 
                'no2Grade': '1', 
                'o3Flag': None, 
                'pm25Grade': None, 
                'so2Flag': None, '
                dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '종로구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.001', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.010', 'stationName': '청계천로', 'pm10Grade': '1', 'o3Value': '0.022'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.1', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '종로', 'pm10Grade': None, 'o3Value': '0.024'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '44', 'so2Value': '0.003', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '4', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.007', 'stationName': '용산구', 'pm10Grade': '1', 'o3Value': '0.027'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '광진구', 'pm10Grade': '1', 'o3Value': '0.025'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '43', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '성동구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.0', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '6', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.014', 'stationName': '강변북로', 'pm10Grade': None, 'o3Value': '0.020'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '47', 'so2Value': '0.002', 'coValue': '0.1', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '4', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.003', 'stationName': '중랑구', 'pm10Grade': '1', 'o3Value': '0.028'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.007', 'stationName': '동대문구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '46', 'so2Value': '0.003', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': '1', 'pm25Value': '3', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.010', 'stationName': '홍릉로', 'pm10Grade': '1', 'o3Value': '0.027'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '43', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.010', 'stationName': '성북구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '6', 'khaiGrade': None, 'pm25Value': '3', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.014', 'stationName': '정릉로', 'pm10Grade': '1', 'o3Value': '0.021'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.4', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '2', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.007', 'stationName': '도봉구', 'pm10Grade': None, 'o3Value': '0.023'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': None, 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.004', 'stationName': '은평구', 'pm10Grade': None, 'o3Value': '0.020'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': '통신장애', 'o3Grade': None, 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': None, 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.004', 'stationName': '서대문구', 'pm10Grade': None, 'o3Value': '0.030'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '53', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '2', 'pm10Value': '5', 'khaiGrade': '2', 'pm25Value': '2', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.007', 'stationName': '마포구', 'pm10Grade': '1', 'o3Value': '0.033'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '36', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': '1', 'pm25Value': '3', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '신촌로', 'pm10Grade': '1', 'o3Value': '0.022'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '39', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '강서구', 'pm10Grade': '1', 'o3Value': '0.023'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '공항대로', 'pm10Grade': '1', 'o3Value': '0.024'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.005', 'stationName': '구로구', 'pm10Grade': '1', 'o3Value': '0.020'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '44', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.008', 'stationName': '영등포구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.010', 'stationName': '영등포로', 'pm10Grade': None, 'o3Value': '0.022'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '51', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '2', 'pm10Value': '3', 'khaiGrade': '2', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.005', 'stationName': '동작구', 'pm10Grade': '1', 'o3Value': '0.031'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '46', 'so2Value': '0.003', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': '1', 'pm25Value': '3', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '동작대로 중앙차로', 'pm10Grade': '1', 'o3Value': '0.028'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '46', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '7', 'khaiGrade': '1', 'pm25Value': '4', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '관악구', 'pm10Grade': '1', 'o3Value': '0.028'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '43', 'so2Value': '0.003', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '2', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.008', 'stationName': '강남구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.002', 'stationName': '서초구', 'pm10Grade': None, 'o3Value': '0.028'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.4', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.008', 'stationName': '도산대로', 'pm10Grade': None, 'o3Value': '0.021'}, {'so2Grade': None, 'coFlag': None, 'khaiValue': '-', 'so2Value': '-', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': '통신장애', 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '강남대로', 'pm10Grade': None, 'o3Value': '0.019'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '42', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': '1', 'pm25Value': '2', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.011', 'stationName': '송파구', 'pm10Grade': '1', 'o3Value': '0.025'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '43', 'so2Value': '0.002', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '강동구', 'pm10Grade': '1', 'o3Value': '0.026'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.009', 'stationName': '천호대로', 'pm10Grade': '1', 'o3Value': '0.027'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.2', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '4', 'khaiGrade': None, 'pm25Value': '2', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.005', 'stationName': '금천구', 'pm10Grade': None, 'o3Value': '0.027'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': '통신장애', 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.012', 'stationName': '시흥대로', 'pm10Grade': None, 'o3Value': '0.020'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': '통신장애', 'o3Grade': '1', 'pm10Value': '-', 'khaiGrade': None, 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '강북구', 'pm10Grade': None, 'o3Value': '0.024'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '41', 'so2Value': '0.003', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '3', 'khaiGrade': '1', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '양천구', 'pm10Grade': '1', 'o3Value': '0.025'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '52', 'so2Value': '0.002', 'coValue': '0.3', 'pm25Flag': None, 'pm10Flag': None, 'o3Grade': '2', 'pm10Value': '3', 'khaiGrade': '2', 'pm25Value': '1', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': '1', 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.006', 'stationName': '노원구', 'pm10Grade': '1', 'o3Value': '0.033'}, {'so2Grade': '1', 'coFlag': None, 'khaiValue': '-', 'so2Value': '0.003', 'coValue': '0.4', 'pm25Flag': '통신장애', 'pm10Flag': None, 'o3Grade': '1', 'pm10Value': '5', 'khaiGrade': None, 'pm25Value': '-', 'sidoName': '서울', 'no2Flag': None, 'no2Grade': '1', 'o3Flag': None, 'pm25Grade': None, 'so2Flag': None, 'dataTime': '2023-08-11 02:00', 'coGrade': '1', 'no2Value': '0.012', 'stationName': '화랑로', 'pm10Grade': '1', 'o3Value': '0.022'}], 'pageNo': 1, 'numOfRows': 100}, 'header': {'resultMsg': 'NORMAL_CODE', 'resultCode': '00'}}}
"""