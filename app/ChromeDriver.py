from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def search(keyword):
    driver = webdriver.Chrome()
    driver.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}")
    input()