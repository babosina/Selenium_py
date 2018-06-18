from selenium import webdriver
import time


class SwitchToIframe:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.execute_script("window.scrollBy(0, 1200);")

        # Switch to frame using ID
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        # driver.switch_to.frame(0)

        time.sleep(3)

        # Search course
        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(3)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1200);")
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test successfull")

        driver.quit()


if __name__ == "__main__":
    ff = SwitchToIframe()
    ff.test()
