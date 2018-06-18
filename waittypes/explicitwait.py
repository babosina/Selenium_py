"""
CANNOT BE RUN DUE TO RESTRICTION OF TYPING DATES EXPLICITLY
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWait:

    def test(self):
        base_url = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2018")
        driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("12/24/2019")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # driver.find_element(By.ID, "stopFilter_stops-0").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    ff = ExplicitWait()
    ff.test()


