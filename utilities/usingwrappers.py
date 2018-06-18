from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handywrappers import HandyWrappers
import time


class UsingWrappers:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)

        text_field = hw.get_element("name")
        text_field.send_keys("Test")

        time.sleep(2)

        text_field_2 = hw.get_element("//input[@id='name']", locator_type='xpath')
        text_field_2.clear()

        driver.quit()


if __name__ == "__main__":
    ff = UsingWrappers()
    ff.test()
