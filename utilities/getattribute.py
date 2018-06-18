from selenium import webdriver
import time


class GetAttribute:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("placeholder")

        print("Value of attribute is: ", result)
        time.sleep(2)

        print(driver.find_element_by_id("bmwradio").get_attribute("value"))

        driver.quit()


if __name__ == "__main__":
    ff = GetAttribute()
    ff.test()
