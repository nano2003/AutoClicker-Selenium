from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from functions import *

#   ---------all functions code written in functions.py file--------------

PATH="E:\Webdriver\chromedriver" #PATH need to be changed to the new path of the webdriver
options = Options()
options.add_argument('--ignore-certificate-errors')


cmd=True
while(cmd):
    
    #ProgramType=input("1/Mouse Clicker (cps auto-clicker) | 2/Space clicker(space auto-clicker): ")
    """
    while ProgramType not in (1,2):
        ProgramType=input("1/Mouse Clicker (cps auto-clicker) | 2/Space clicker(space auto-clicker)")
    """
    ProgramType=2
    Driver=webdriver.Chrome(PATH,options=options)
    if(ProgramType == 1):
        Driver.get("https://cps-tester.com/")
        Driver.implicitly_wait(10)
        
        clicker=Driver.find_element(By.CSS_SELECTOR,".js-clicks")
        TimerCount=Driver.find_element(By.CSS_SELECTOR,".number_timer")
        TimerCount=float(TimerCount.text)
        TimerCount=int(TimerCount)
        
        MouseClicker(Driver,TimerCount,clicker,0)
    
    
    elif(ProgramType == 2):
        Driver.get("https://spacebar-counter.com/")
        TimerCount=Driver.find_element(By.CSS_SELECTOR,".number_timer")
        TimerCount=float(TimerCount.text)

        SpaceClicker(Driver,TimerCount,0)
    
    elif(ProgramType == 0):
        cmd = False

    
    
    #condition to continue or leave the loop
    #chossing the timelapse




        print("----Quitting Program----")













# MAX SPS: 53.80 (depends on the connection)