# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def recaptcha_login():
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
    driver.get('https://www.google.com/recaptcha/api2/demo')

    # captcha_iframe = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.TAG_NAME, 'iframe')))
    # ActionChains(driver).move_to_element(captcha_iframe).click().perform()
    # captcha_box = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.ID, 'g-recaptcha-response')))
    # driver.execute_script("arguments[0].click()", captcha_box)

    WebDriverWait(driver, 20).until(ec.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()

# Login recaptcha Account
recaptcha_login()
