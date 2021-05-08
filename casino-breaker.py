import time
import getpass
from seleniumwire import webdriver
from termcolor import colored

driver = webdriver.Chrome(r"C:\Users\Eliaz\Documents\pathDivers\chromedriver.exe")

driver.get('https://gamblingbot.app/games/fortune-wheel')

someVariable = getpass.getpass("Press Enter after you are done logging in")
a=False
nbessai=0
while a==False:
    del driver.requests
    wheel_button = driver.find_element_by_id('middleButton')
    wheel_button.click()
    time.sleep(1)
    for request in driver.requests:
        if (request.response and request.url=="https://gamblingbot.app/api/games/fortune-wheel-start"):
            if ":1" in str(request.response.body):
                print("prize if stopped : ", colored("6,000","green"))
            elif ":2" in str(request.response.body):
                print("prize if stopped : ", colored("120,000","blue"))
            elif ":3" in str(request.response.body):
                print("prize if stopped : ", colored("30,000","green"))
            elif ":4" in str(request.response.body):
                print("prize if stopped : ", colored("250,000","red"))
            elif ":5" in str(request.response.body):
                print("prize if stopped : ", colored("20,000","green"))
            elif ":6" in str(request.response.body):
                print("prize if stopped : ", colored("60,000","blue"))
            elif ":7" in str(request.response.body):
                print("prize if stopped : ", colored("15,000","green"))
            elif ":8" in str(request.response.body):
                print("prize if stopped : ", colored("450,000","red"))
            elif ":9" in str(request.response.body):
                print("prize if stopped : ", colored("11,500","green"))
            elif ":10" in str(request.response.body):
                print("prize if stopped : ", colored("45,000","blue"))
            elif ":11" in str(request.response.body):
                print("prize if stopped : ", colored("9,000","green"))
            if ":0" in str(request.response.body):
                print("VICTORY ROYALE - ", colored("10,000,000","yellow"), "credits aquired")
                a=True
            else :
                driver.refresh()
                nbessai=nbessai+1
                if nbessai % 10 == 0 :
                    print("tries so far: " + str(nbessai))
print("total number of tries to get the jackpot :" + str(nbessai))
someVariable = getpass.getpass("Press Enter to quit")
driver.quit()