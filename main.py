# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pyshadow.main import Shadow
import urllib.request, time, pyautogui

inc=0

def recaptcha_login():
    global driver, inc

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_extension('browsec.crx')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("chrome://extensions/")

    shadow = Shadow(driver)
    shadow.find_element("#detailsButton").click()
    URL = driver.current_url
    driver.get("chrome-extension://" + URL[24:len(URL)] + "/popup/popup.html")
    driver.implicitly_wait(5)
    shadow.find_element("div.In.transition > div > div.Inactive > div.Inactive_ButtonOut > div").click()

    driver.get('https://www.google.com/recaptcha/api2/demo')
    WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(
        ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[7]/a"))).click()
    for handle in driver.window_handles:
        inc = inc+1
        driver.switch_to.window(handle)
        if inc==1:
            url=driver.current_url
            urllib.request.urlretrieve(url, "d://file.mp3")
            inc=0

    driver.get('https://speech-to-text-demo.ng.bluemix.net/')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"root\"]/div/div[6]/button[2]"))).click()
    time.sleep(1)
    
    # print(pyautogui.position())
    pyautogui.click(397,598)

    pyautogui.write('D:\\file.mp3')
    pyautogui.press('enter')
    time.sleep(5)
    xpath_text="//*[@id=\"root\"]/div/div[7]/div/div"
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_text)))
    stt=driver.find_element(By.XPATH, xpath_text).text
    print(stt)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(
        ec.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
    xpath_stt = "//*[@id=\"audio-response\"]"
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, xpath_stt)))
    stt_output = driver.find_element(By.XPATH, xpath_stt)
    stt_output.send_keys(stt)
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-verify-button"]'))).click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-demo-submit"]'))).click()

# Login recaptcha Account
recaptcha_login()
