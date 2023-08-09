from flask import Flask, request, redirect, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import platform

import time
import os

app = Flask(__name__)

print(platform.system())
chrome_options = webdriver.ChromeOptions()
if platform.system() == "Linux":
    driver_local = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver-linux64', 'chromedriver')
elif platform.system() == "Windows":
    driver_local = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver-win64', 'chromedriver.exe')

driver_local = os.chmod(driver_local, 0o755)
chrome_service = Service(executable_path = driver_local)

#chrome_service.start()

#chrome_options.capabilities['Google Chrome']
chrome_options.binary_location = str(os.environ.get("GOOGLE_CHROME_BIN"))
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


@app.route("/", methods=["GET", "POST"])

def main():
    #driver = webdriver.Chrome(service=chrome_service, options=chrome_options, driver_path = driver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get("https://stackoverflow.com/")
        src = driver.page_source
        driver.quit()
        print("Done.")
        return(src)
    
    except Exception as e:
        # Handle any exceptions that occur
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run()

#message()
'''#def test():
#   return('test')

#ef getVidTitle():
chrome_options = Options()
global driver   
chrome_options.set_capability("browserVersion", "104")
chrome_options.set_capability("platformName", "Windows 11")

driver = webdriver.Remote(
    command_executor='https://cloud-based-python-application-test.onrender.com',
    options=chrome_options
    
    )

try:
    driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    time.sleep(5)
    button_element = driver.find_element(By.ID, "subscribe-button")
    button_element.click()
    time.sleep(5)
    driver.close()
    print('Done.')

except Exception as e:
    print(f"Error: {str(e)}")

#if __name__ == '__main__':
    app.secret_key = '123123'
    app.debug = True
    app.run(host='192.168.1.214', port='5000')

'''