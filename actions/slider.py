from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Sliding:

    def test(self):
        base_url = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        driver.switch_to.frame(0)

        element = driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 200, 0).perform()
            print("Sliding good")
            time.sleep(2)
        except:
            print("sliding failed")

        driver.quit()


if __name__ == "__main__":
    ff = Sliding()
    ff.test()
