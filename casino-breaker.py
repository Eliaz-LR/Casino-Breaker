import time
import getpass
from seleniumwire import webdriver

driver = webdriver.Chrome(r"C:\Users\Eliaz\Documents\pathDivers\chromedriver.exe")

driver.get('https://gamblingbot.app/games/fortune-wheel')

someVariable = getpass.getpass("Press Enter after You are done logging in")
a=False
nbessai=0
while a==False:
    del driver.requests
    time.sleep(1)
    wheel_button = driver.find_element_by_id('middleButton')
    wheel_button.click()
    time.sleep(1)
    for request in driver.requests:
        if (request.response and request.url=="https://gamblingbot.app/api/games/fortune-wheel-start"):
            print(request.response.body)
            if (":0" or "12") in str(request.response.body):
                print("VICTOIRE")
                a=True
            else :
                driver.refresh()
                nbessai=nbessai+1

    time.sleep(1)
    
print(nbessai)
someVariable = getpass.getpass("Press Enter to quit")
driver.quit()