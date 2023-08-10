import stt
import ChromeDriver
import Weather
import Dust

name = "시리"
exit_command = "종료"
search_command = "검색"
weather_command = "날씨"
dust_command = "미세먼지"

def start():
    recognizable = False
    while True:
        msg = stt.start_recognizing()
        if exit_command in msg:
            break
        if name not in msg and recognizable == False:
            print(f"{name}를 불러주세요")
            continue
        recognizable = True
        excute_command(msg)

def remove_secretary_name(msg):
    words = list(msg.split())
    name_index = 0
    for index, word in enumerate(words):
        if name in word:
            name_index = index
            break
    words.pop(name_index)
    return ' '.join(words)

def excute_command(msg):
    words = list(remove_secretary_name(msg).split())
    if len(words) == 0:
        return
    last_word = words.pop()
    keyword = ' '.join(words)

    if search_command == last_word:
        search_naver(keyword)
    elif weather_command == last_word:
        get_weather_info()
    elif dust_command == last_word:
        get_dust_info()

def search_naver(keyword):
    print("< 네이버 검색 >")
    ChromeDriver.search(keyword)

def get_weather_info():
    print("< 날씨 정보 >")
    Weather.get_info()

def get_dust_info():
    print("< 미새먼지 정보 >")
    Dust.get_info()