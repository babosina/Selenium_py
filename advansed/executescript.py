from selenium import webdriver
import time


class ExecuteScript:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get(base_url)
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)

        # element = driver.find_element_by_id("name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("TEST")

        driver.quit()


if __name__ == "__main__":
    ff = ExecuteScript()
    ff.test()
