# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request, time

inc=0

def recaptcha_login():
    global driver, inc

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
    driver.get('https://www.google.com/recaptcha/api2/demo')

    WebDriverWait(driver, 20).until(ec.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    time.sleep(5)
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
    time.sleep(5)
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[7]/a"))).click()
    time.sleep(2)
    for handle in driver.window_handles:
        inc = inc+1
        driver.switch_to.window(handle)
        if inc==1:
            url=driver.current_url
            urllib.request.urlretrieve(url, "file.mp3")
            inc=0

# Login recaptcha Account
recaptcha_login()
