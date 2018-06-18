from selenium import webdriver
import time


class ImplicitWaitDemo:

    def test(self):
        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        driver.find_element_by_link_text("Login").click()

        driver.find_element_by_id("user_email").send_keys("test")

        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
    ff = ImplicitWaitDemo()
    ff.test()
