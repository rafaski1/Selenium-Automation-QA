# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

class Booking():
    def currency(self):
        driver.get("https://www.booking.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Pound sterling").click()

    def where_to(self):
        destination = "Bristol"
        driver.find_element(By.XPATH, "//input[@id='ss']").send_keys(destination)
        full_destination = driver.find_element(By.XPATH, "//li[@data-i='0']")
        print_destination = full_destination.get_attribute("data-label")
        print("Destination:", print_destination)
        full_destination.click()

    def calendar(self):
        check_in="2022-03-14"
        check_out = "2022-03-20"
        driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]').click()
        driver.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]').click()
        print("Check in date:", check_in)
        print("Check out date:", check_out)

    def guests(self):
        driver.find_element(By.XPATH, "//label[@id='xp__guests__toggle']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Decrease number of Adults']").click()
        driver.find_element(By.XPATH, "//button[contains(@class,'sb-searchbox__button')]").click()

class Results():
    def stars(self):
        driver.find_element(By.CSS_SELECTOR, 'div[data-filters-item="class:class=5"]').click()
        driver.find_element(By.CSS_SELECTOR, 'div[data-filters-item="class:class=4"]').click()

        time.sleep(10)


booking = Booking()
booking.currency()
booking.where_to()
booking.calendar()
booking.guests()

results = Results()
results.stars()

