from selenium import webdriver
import time


class RadioBtnsAndCheckboxes:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        bmw_radiobtn = driver.find_element_by_id("bmwradio")
        bmw_radiobtn.click()

        time.sleep(2)

        benz_radiobtn = driver.find_element_by_id("benzradio")
        benz_radiobtn.click()

        time.sleep(2)

        bmw_check = driver.find_element_by_id("bmwcheck")
        bmw_check.click()

        time.sleep(2)

        benz_check = driver.find_element_by_id("benzcheck")
        benz_check.click()

        print("BMW radio is selected? ", bmw_radiobtn.is_selected())
        print("Benz radio is selected? ", benz_radiobtn.is_selected())
        print("BMW checkbox is selected? ", bmw_check.is_selected())
        print("Benz checkbox is selected? ", benz_check.is_selected())

        driver.quit()


if __name__ == "__main__":
    ff = RadioBtnsAndCheckboxes()
    ff.test()
