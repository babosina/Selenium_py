from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WorkWithElementsList:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        radio_list = driver.find_elements(By.XPATH, '//input[contains(@type,"radio") and contains(@name, "cars")]')
        print("Size of radio list is: ", len(radio_list))

        for radio in radio_list:
            if not radio.is_selected():
                radio.click()
                time.sleep(3)

        driver.quit()


if __name__ == "__main__":
    ff = WorkWithElementsList()
    ff.test()
