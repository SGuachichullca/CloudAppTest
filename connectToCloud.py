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
@app.route('/')
async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://www.python.org/")
    # create a screenshot of the page and save it
    await page.screenshot({os.path.dirname(os.path.realpath(__file__)) : "python.png"})
    # close the browser
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

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