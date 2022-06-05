# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class HMRC():
    def demo_hmrc(self):
        driver.get("http://www.hmrc.gov.uk/tools/sa-ready-reckoner/calculator.htm")
        driver.maximize_window()
        UK_income = driver.find_element(By.XPATH, "//button[normalize-space()='UK Income Tax']")
        UK_income.click()
        x = random.randrange(300, 1000, 10)
        print("Estimated net weekly profit: £", x)
        driver.find_element(By.ID, "money").send_keys(x)
        driver.find_element(By.ID, "rad1").click()
        driver.find_element(By.XPATH, "(//input[@value='Calculate'])[1]").click()
        #results
        yearly_profit = driver.find_element(By.CSS_SELECTOR, "td:nth-child(5)")
        print("Yearly Profit:", yearly_profit.text)
        yearly_tax = driver.find_element(By.CSS_SELECTOR, "td:nth-child(6)")
        print("Yearly Tax and Class 2 and 4 NI:", yearly_tax.text)

        time.sleep(10)

taxes = HMRC()
taxes.demo_hmrc()
