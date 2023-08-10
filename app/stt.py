import speech_recognition as sr

failed = "Failed"

def start_recognizing():
    # 인식을 위한 객체 생성
    r = sr.Recognizer()

    # 마이크 사용을 위한 객체 생성
    mic = sr.Microphone()

    try:
        with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
            r.adjust_for_ambient_noise(source) # 잡음 제거 코드 (없어도 무방)
            print('인식 중...')
            audio = r.listen(source, timeout=5, phrase_time_limit=5) # 해당 소리를 오디오 파일 형태로 변환
        result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
        print('결과: ' + result) # 인식 결과 출력
        return result
    except sr.UnknownValueError:
        print("음성 인식 실패")
        return failed
    except sr.RequestError:
        print("서버 에러 발생")
        return failed
    except sr.WaitTimeoutError:
        print("인식 실패")
        return failed