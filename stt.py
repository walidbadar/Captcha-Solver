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
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"root\"]/div/div[6]/button[2]"))).click()
    time.sleep(1)
    # print(pyautogui.position())
    pyautogui.click(397,598)
    pyautogui.write('D:\\file.mp3')
    pyautogui.press('enter')
    xpath_text="//*[@id=\"root\"]/div/div[7]/div/div"
    time.sleep(10)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_text)))
    print(driver.find_element(By.XPATH, xpath_text).text)
    
# IBM speech to text
stt()



