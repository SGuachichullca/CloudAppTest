from flask import Flask, request, redirect, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import asyncio
import os
from pyppeteer import launch

app = Flask(__name__)
chrome_options = webdriver.ChromeOptions()


@app.route('/', methods=['GET', 'POST'])
def main():
    try:
        chrome_options.binary_location=os.environ.get('GOOGLE_CHROME_BIN')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=os.environ.get('CHROMEDRIVER_PATH'), options=chrome_options)

        driver.get('https://stackoverflow.com/questions/71821803/requests-html-render-returning-winerror-14001-on-vscode')
        time.sleep(6)
        driver.quit()
        #print(driver.page_source)
        print('Done.')
        return('Done.')
    
    except Exception as e:
        # Handle any exceptions that occur
        return f"Error: {str(e)}"



if __name__ == '__main__':
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