from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        element_By_id = driver.find_element(By.ID, "name")

        if element_By_id is not None:
            print("Element found by Class")

        element_By_xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if element_By_xpath is not None:
            print("Element found by Tag")

        element_By_link_text = driver.find_element(By.LINK_TEXT, "Practice")

        if element_By_link_text is not None:
            print("Element found by Link text")

        driver.quit()


if __name__ == "__main__":

    ff = ByDemo()
    ff.test()
