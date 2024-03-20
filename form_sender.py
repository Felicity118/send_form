
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import psutil
def close_all_driver_instances():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            # Check if the process is ChromeDriver
            if process_name == "chromedriver":
                proc.terminate()  # Terminate the ChromeDriver process
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Handle exceptions as needed

def wait(by,search_value):
    global driver
    if by=='class':
        if ' ' in search_value:
            search_value = search_value.replace(' ', '.')
        element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, search_value)))
        elements=driver.find_elements(by=By.CLASS_NAME,value=search_value)
    elif by=='tag':
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.TAG_NAME, search_value)))
        elements = driver.find_elements(by=By.TAG_NAME, value=search_value)
    elif by=='css':
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, search_value)))
        elements = driver.find_elements(by=By.CSS_SELECTOR, value=search_value)
    if len(elements)==1:
        return element
    else:
        print(f"The element {search_value} is not unique")
        print(elements)
def open_form():
    close_all_driver_instances()
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\Users\usher\Desktop\Apps\Selenium\userData")
    #options.add_argument('--headless')  # Enable headless mode
    #options.add_argument('--disable-gpu')
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    global driver
    driver = webdriver.Chrome(options=options)
    driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAWLUtxRURDZCNDMwRVlJOVVSUEhXRklIVTgyVTAySC4u")
    #driver.minimize_window()
def send_form():
    text_box = wait('tag', "input")
    text_box.send_keys('ushermichele2002@gmail.com')
    button=wait('css','button[data-automation-id="submitButton"]')
    button.click()
    sleep(5)
def execute():
    open_form()
    send_form()
