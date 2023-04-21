from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

def MouseClicker(Driver,TimerCount,Clicks,TimerFrame):

    actions=ActionChains(Driver)

    while(TimerCount > 0):
        actions.move_to_element(Clicks).click().perform()
        TimerCount=Driver.find_element(By.CSS_SELECTOR,".number_timer")
        TimerCount=float(TimerCount.text)

    print("done")
    score=Driver.find_element(By.CSS_SELECTOR,".js-score")
    cps=Driver.find_element(By.CSS_SELECTOR,".js-speed")
    print("-*MouseAutoClicker Test*-")
    print(f"------------------------------------ \n     Score: {score.text} \n     CPS: {cps.text} \n")
   
    usr_cmd=input(f"     Restart: [Y/N]: \n").upper()
    while(usr_cmd != "N" and usr_cmd != "Y"):
        usr_cmd=input(f"     Restart: [Y/N]: \n").upper()
        print("------------------------------------")

    if(usr_cmd == "Y"):
        TimeFrame=input("Give the time Frame: ")
        while TimeFrame not in (1,3,5,10,15,30,60,100): 
            TimeFrame=input("Give the time Frame: ")
        Driver.find_element(By.CSS_SELECTOR,".js-try-again").click()
        return MouseClicker(Driver,TimerCount,TimerFrame)


def SpaceClicker(Driver,TimerCount,TimeFrame):

    actions=ActionChains(Driver)

    while(TimerCount > 0):
        actions.send_keys(Keys.SPACE).perform()
        TimerCount=Driver.find_element(By.CSS_SELECTOR,".number_timer")
        TimerCount=float(TimerCount.text)

    score=Driver.find_element(By.CSS_SELECTOR,".js-score")
    sps=Driver.find_element(By.CSS_SELECTOR,".js-speed")

    print("-*MouseAutoClicker Test*-")
    print(f"------------------------------------ \n     Score: {score.text} \n     SPS: {sps.text} \n")

    usr_cmd=input(f"     Restart: [Y/N]: \n").upper()
    while(usr_cmd != "N" and usr_cmd != "Y"):
        usr_cmd=input(f"     Restart: [Y/N]: \n").upper()
        print("------------------------------------")

    if(usr_cmd == "Y"):
        TimeFrame=input("Give the time Frame: ")
        
        while TimeFrame in (1,3,5,10,15,30,60,100): 
            TimeFrame=input("Give the time Frame: ")

        Driver.find_element(By.CSS_SELECTOR,".js-try-again").click()
        SpaceClicker(Driver,TimerCount,TimeFrame)


        