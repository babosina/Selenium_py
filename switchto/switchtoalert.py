from selenium import webdriver
import time


class SwitchToAlert:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        driver.find_element_by_id("name").send_keys("Test")
        alert = driver.find_element_by_id("alertbtn")
        confirm = driver.find_element_by_id("confirmbtn")

        alert.click()
        time.sleep(2)

        alert_modal = driver.switch_to.alert
        alert_modal.accept()
        time.sleep(2)

        driver.find_element_by_id("name").send_keys("Test")
        confirm.click()
        time.sleep(2)
        confirm_modal = driver.switch_to.alert
        confirm_modal.dismiss()

        driver.quit()


if __name__ == "__main__":
    ff = SwitchToAlert()
    ff.test()
