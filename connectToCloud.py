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
'''if platform.system() == "Linux":
    driver_local = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver-linux64', 'chromedriver')
elif platform.system() == "Windows":
    driver_local = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver-win64', 'chromedriver.exe')'''

driver_local = os.environ.get("CHROMEDRIVER_PATH")

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
        '''driver.get("https://stackoverflow.com/")
        src = driver.page_source
        driver.quit()
        print("Done.")
        return(src)'''
        driver.get('https://fires.fdnycloud.org/CitizenAccess/Cap/CapHome.aspx?module=BFP&TabName=BFP')

        search_bar = driver.find_element(By.NAME, "ctl00$PlaceHolderMain$generalSearchForm$txtGSPermitNumber")
        search_bar.click()
        search_bar.send_keys('42091108')
        search_bar.send_keys(Keys.ENTER)
        #actions.click(search_bar).send_keys(VONum).send_keys(Keys.ENTER).perform()
        time.sleep(3)

        record_address = driver.find_element(By.CLASS_NAME, "NotBreakWord").text
        #print(record_address.text)
        record_info = driver.find_element(By.CLASS_NAME, "selected")
        supp_documents = driver.find_element(By.CLASS_NAME, "dropdown-menu")
        #actions.click(record_info).click(supp_documents).perform()
        record_info.click()
        supp_documents.click()

        download_link = driver.find_element(By.ID, "ctl00_PlaceHolderMain_attachmentEdit_iframeAttachmentList")
        driver.get(download_link.get_property('src'))

        download_link = driver.find_element(By.ID, 'attachmentList_gdvAttachmentList_ctl02_lblName')
        #actions.click(download_link).perform()
        download_link.click()
        time.sleep(3)
    
        driver.quit()
    
    except Exception as e:
        # Handle any exceptions that occur
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run()