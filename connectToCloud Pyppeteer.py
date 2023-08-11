from quart import Quart, request
from pyppeteer import launch
app = Quart(__name__)

@app.route("/", methods=["GET"])

async def main():
    keyName = 'VO'
    VONum = request.args.get(keyName)
    try:
        fdny_url = 'https://fires.fdnycloud.org/CitizenAccess/Cap/CapHome.aspx?module=BFP&TabName=BFP&TabList=Home%7C0%7CBFP%7C1%7CCurrentTabIndex%7C1'
        browser = await launch({"headless": True})
        rec = await browser.newPage()

        await rec.goto(fdny_url)
        await rec.type('input[name="ctl00$PlaceHolderMain$generalSearchForm$txtGSPermitNumber"]',
                        VONum)
        await rec.keyboard.press('Enter')
        print(rec.url)

        await rec.waitForFunction(f'() => window.location.href !== "{fdny_url}"')
        print ('URL Has Changed.')                    
        rec_url = rec.url
        print(rec_url)
        await browser.close()

        response_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="refresh" content="0;url={rec_url}">
            </head>
            <body>
                Redirecting....
            </body>
            </html>
        '''
        return(response_content)
        ## Get HTML
        '''htmlContent = await url.content()
        await browserObj.close()
        return (htmlContent)'''
   
    except Exception as e:
        # Handle any exceptions that occur
        print(str(e))
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run()
'''response = asyncio.get_event_loop().run_until_complete(main())
print(response)'''