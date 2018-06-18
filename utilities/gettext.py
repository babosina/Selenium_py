from selenium import webdriver
import time


class GetText:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(4)

        open_tab_element = driver.find_element_by_id("opentab")
        open_tab_element_text = open_tab_element.text
        print("text on element is: ", open_tab_element_text)

        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
    ff = GetText()
    ff.test()
