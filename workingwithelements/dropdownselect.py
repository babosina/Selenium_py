from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class DropDownSelect:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("carselect")
        selected = Select(element)

        selected.select_by_value("benz")
        print("Select Benz by Value")

        time.sleep(2)

        selected.select_by_index("2")
        print("Select Honda by Index")

        time.sleep(2)

        selected.select_by_visible_text("BMW")
        print("Select BMW by Visible text")

        time.sleep(2)

        selected.select_by_index(2)
        print("Select Honda by Index")

        driver.quit()


if __name__ == "__main__":
    ff = DropDownSelect()
    ff.test()
