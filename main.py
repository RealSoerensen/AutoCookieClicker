import os
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

directory = "CookieClickerSave"
parent_dir = os.path.dirname(__file__)
path = os.path.join(parent_dir, directory)
if not os.path.exists(path):
    os.makedirs(path)


class CookieBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)

    def start(self):
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        sleep(2)
        CookieBot.import_save(self)

    def import_save(self):
        try:
            with open(path + "\\RobotDucklingBakery.txt", "r") as save_file:
                save_text = save_file.read()
                self.driver.find_element(By.ID, "prefsButton").click()
                self.driver.find_element(By.XPATH,
                                         "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[2]").click()
                self.driver.find_element(By.XPATH,
                                         "/html/body/div[2]/div[2]/div[11]/div/div[1]/div[2]/textarea").send_keys(
                    save_text)
                self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[11]/div/div[1]/div[3]/a[1]").click()
                self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[1]").click()
                print("Loaded save")
        except Exception:
            pass

        CookieBot.cookie_click(self)

    def cookie_click(self):
        while True:
            self.driver.find_element(By.ID, "bigCookie").click()

            if randint(0, 800) == 400:
                CookieBot.autosave(self)

            if randint(0, 100) < 5:
                CookieBot.upgrade(self)
                CookieBot.store(self)

    def store(self):
        for product_num in range(17, -1, -1):
            try:
                store = self.driver.find_element(By.ID, "product" + str(product_num))
                if store.get_attribute("class") == "product unlocked enabled":
                    store.click()
            except Exception:
                pass

    def upgrade(self):
        try:
            upgrade = self.driver.find_element(By.ID, "upgrade0")
            if upgrade.get_attribute("class") == "crate upgrade enabled":
                upgrade.click()
        except Exception:
            pass

    def autosave(self):
        try:
            self.driver.find_element(By.ID, "prefsButton").click()
            self.driver.find_element(By.XPATH,
                                     "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[1]").click()
            save_text = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div[11]/div/div[1]/div[2]/textarea").text
            with open(path + "\\RobotDucklingBakery.txt", "w") as save_file:
                save_file.write(str(save_text))
            self.driver.find_element(By.ID, "promptOption0").click()
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[1]").click()
            print("Saved")
            sleep(300)
        except Exception:
            print("Failed to save")
            pass


bot = CookieBot()
bot.start()
