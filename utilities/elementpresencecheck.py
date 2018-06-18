from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handywrappers import HandyWrappers


class ElementPresence:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)

        element_1 = hw.is_element_present("//input[@id='name']", By.XPATH)
        print(str(element_1))

        element_2 = hw.element_presence_check("name1", By.ID)
        print(str(element_2))

        driver.quit()


if __name__ == "__main__":
    ff = ElementPresence()
    ff.test()
