from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--ignore-certificate-errors')

Driver=webdriver.Chrome("E:\Webdriver\chromedriver",options=options)
Driver.get("https://cps-tester.com/")

Driver.implicitly_wait(10)

clicker=Driver.find_element(By.CSS_SELECTOR,".js-clicks")
TimerCount=Driver.find_element(By.CSS_SELECTOR,".number_timer")
RestartButton=Driver.find_element(By.CSS_SELECTOR,".js-try-again")

TimerCount=float(TimerCount.text)
TimerCount=int(TimerCount)
cmd=True


while(cmd):
    #replace while methode with try and excpet
    try:
        while(TimerCount > 0):
            clicker.click()
    except :

        print("done")
        score=Driver.find_element(By.CSS_SELECTOR,".js-score")
        cps=Driver.find_element(By.CSS_SELECTOR,".js-speed")
        
        if(input(f"------------------------------------ \n     Score: {score.text} \n     CPS: {cps.text} \n     Restart: [Y/N]: \n").upper() == "Y"):
            cmd=True
            Driver.find_element(By.CSS_SELECTOR,".js-try-again").click()
        else:
            cmd=False
            Driver.quit()
        print("------------------------------------")

    print("Quitting")


