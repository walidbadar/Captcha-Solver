# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request, time, pyautogui

def stt():
    global driver

    # def resource_path(relative_path):
    #     try:
    #         base_path = sys._MEIPASS
    #     except Exception:
    #         base_path = os.path.dirname(__file__)
    #     return os.path.join(base_path, relative_path)

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'),options=options)
    driver = webdriver.Chrome(options=options)
    driver.get('https://speech-to-text-demo.ng.bluemix.net/')
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"root\"]/div/div[6]/button[2]"))).click()
    time.sleep(3)
    pyautogui.click(397,598)
    pyautogui.write('D:\\file.mp3')
    pyautogui.press('enter')

# IBM speech to text
stt()

