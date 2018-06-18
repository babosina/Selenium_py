from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys:

    def test(self):
        basuUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(basuUrl)
        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH,'//div[@id="navbar"]//a[@href="/sign_in"]')
        login_link.click()

        email_input = driver.find_element(By.ID, "user_email")
        email_input.send_keys("test")

        password_input = driver.find_element(By.ID, "user_password")
        password_input.send_keys("test")

        time.sleep(3)

        email_input.clear()

        time.sleep(3)

        email_input.send_keys("test")

        driver.quit()


if __name__ == "__main__":
    ff = ClickAndSendKeys()
    ff.test()
