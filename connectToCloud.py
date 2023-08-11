from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import platform
import webbrowser

import time
import os

app = Flask(__name__)

driver_path = os.environ.get("CHROMEDRIVER_PATH")
if platform.system() == "Linux":
    driver_octal = os.chmod(driver_path, 0o755)
    chrome_service = Service(executable_path = driver_octal)
else:
    chrome_service = None

w = webbrowser.Chrome(str(os.environ.get("GOOGLE_CHROME_BIN")))
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = str(os.environ.get("GOOGLE_CHROME_BIN"))
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--window-size=1920,1080')  
chrome_options.add_argument('--start-minimized')  
chrome_options.add_argument('--disable-infobars')

@app.route("/", methods=["GET"])

def main():
    
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    keyName = 'VO'
    VONum = request.args.get(keyName)
    try:

        #Opens fires.fdnycloud.org.
        driver.get('https://fires.fdnycloud.org/CitizenAccess/Cap/CapHome.aspx?module=BFP&TabName=BFP')

        #Sends violation number stored in the key parameter into the fdnycloud.org violations search and returns the associated record.
        search_bar = driver.find_element(By.NAME, "ctl00$PlaceHolderMain$generalSearchForm$txtGSPermitNumber")
        search_bar.click()
        search_bar.send_keys(VONum)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        #Navigates to the supporting documents section to find the download link.
        rec_url = driver.current_url
        record_info = driver.find_element(By.CLASS_NAME, "selected")
        supp_documents = driver.find_element(By.CLASS_NAME, "dropdown-menu")
        record_info.click()
        supp_documents.click()

        #Finds element containing download link and clicks it
        download_link = driver.find_element(By.ID, "ctl00_PlaceHolderMain_attachmentEdit_iframeAttachmentList")
        driver.get(download_link.get_property('src'))

        download_link = driver.find_element(By.ID, 'attachmentList_gdvAttachmentList_ctl02_lblName')
        download_link.click()
        time.sleep(3)

        driver.quit()
        #return(f'Downloaded {VONum}.')
        
        response_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="refresh" content="0;url={rec_url}">
            </head>
            <body>
                Redirecting...
            </body>
            </html>
        '''
        return(response_content)
        #return(webbrowser.open(rec_url, new = 0, autoraise=True))

    
    except Exception as e:
        # Handle any exceptions that occur
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
