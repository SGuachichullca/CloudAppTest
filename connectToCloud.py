from flask import Flask, request, redirect, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
#def test():
#   return('test')

def getVidTitle():
    chrome_options = Options()
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        time.sleep(5)
        button_element = driver.find_element(By.ID, "subscribe-button")
        button_element.click()
        time.sleep(5)
        driver.close()
        return('')

    except Exception as e:
        return(f"Error: {str(e)}")

if __name__ == '__main__':
    app.secret_key = '123123'
    app.debug = True
    app.run()
