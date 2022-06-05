# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
import random

fake_data = Faker()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class Halifax():
    def demo_hali(self):
        driver.get("https://apply.halifax-online.co.uk/sales-content/cwa/h/loans-ntf/index-app.html#/about-you")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "accept").click()
        x = random.randrange(1000, 25000, 100)
        driver.find_element(By.ID, "input-loan-amount-input").send_keys(x)
        print("Loan amount: £", x)
        driver.find_element(By.XPATH, "(//a[normalize-space() = '36'])[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Car, caravan or motorbike']").click()
        driver.find_element(By.NAME, "continue-application").click()

    def personal_info(self):
        driver.find_element(By.XPATH, "(//a[normalize-space() = 'Mr'])[1]").click()
        name1 = fake_data.first_name()
        driver.find_element(By.ID, "input-first-name-input").send_keys(name1)
        name2 = fake_data.last_name()
        driver.find_element(By.ID, "input-last-name-input").send_keys(name2)
        print(name1, name2)

    def dob(self):
        DOB1 = random.randint(1,30)
        driver.find_element(By.XPATH, "(//input[@placeholder='DD'])[1]").send_keys(DOB1)
        DOB2 = random.randint(1, 12)
        driver.find_element(By.XPATH, "(//input[@title='Date of birth-months'])[1]").send_keys(DOB2)
        DOB3 = random.randint(1920, 2004)
        driver.find_element(By.XPATH, "(//input[@title='Date of birth-years'])[1]").send_keys(DOB3)
        print("DOB:", DOB1, "/", DOB2, "/", DOB3)

    def gender(self):
        driver.find_element(By.XPATH, "(//label[normalize-space()='Male'])[1]").click()

    def address(self):
        driver.find_element(By.XPATH, "(//input[@id='postcode-currentAddress-input'])[1]").send_keys("BS1 5TR")
        driver.find_element(By.XPATH, "(//span[@class='enter-your-address-manually'])[1]").click()
        driver.find_element(By.ID, "houseNumber-currentAddress-input").send_keys("1")
        driver.find_element(By.ID, "houseName-currentAddress-input").send_keys("BRISTOL CITY COUNCIL")
        driver.find_element(By.ID, "street-currentAddress-input").send_keys("College Green")
        driver.find_element(By.ID, "townCity-currentAddress-input").send_keys("Bristol")
        driver.find_element(By.ID, "postCode-currentAddress-input").send_keys("BS1 5TR")

    def date(self):
        driver.find_element(By.XPATH, "(//input[@title='When did you move here-months'])[1]").send_keys("11")
        driver.find_element(By.XPATH, "(//input[@title='When did you move here-years'])[1]").send_keys("2011")
        driver.find_element(By.XPATH, "(//button[normalize-space()='Continue'])[1]").click()

        time.sleep(10)

loan = Halifax()
loan.demo_hali()
loan.personal_info()
loan.dob()
loan.gender()
loan.address()
loan.date()
