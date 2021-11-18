from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
import threading

service = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

save_path = "C:\Program Files (x86)"

class CookieBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        try:
            open(save_path + "\\RobotDucklingBakery.txt")
        except FileNotFoundError:
            pass
        
    def start(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        sleep(2)
        CookieBot.cookie_click(self)

    def cookie_click(self):
        while True:
            self.driver.find_element(By.ID, "bigCookie").click()

            if randint(0, 100) < 5:
                CookieBot.upgrade(self)
                CookieBot.store(self)

    def store(self):
        for product_num in range(17, -1, -1):
            try: 
                store = self.driver.find_element(By.ID, "product" + str(product_num))
                if store.get_attribute("class") == "product unlocked enabled":
                    store.click()       
            except:
                pass
    
    def upgrade(self):
        try: 
            upgrade = self.driver.find_element(By.ID, "upgrade0")
            if upgrade.get_attribute("class") == "crate upgrade enabled":
                upgrade.click()
        except:
            pass
    
    def autosave(self):
        while True:
            try:
                self.driver.find_element(By.ID, "prefsButton").click()
                self.driver.find_element(By.ID, "option").click()
                save_text = self.driver.find_element(By.ID, "textareaPrompt").text
                with open(save_path + "\\RobotDucklingBakery.txt", "w") as save:
                    save.write(save_text)
                self.driver.find_element(By.CLASS_NAME, "close menuClose").click()
            except:
                pass

bot = CookieBot()
bot.start()
