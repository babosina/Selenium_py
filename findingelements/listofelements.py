from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)

        elements_list_by_class_name = driver.find_elements_by_class_name("inputs")

        if elements_list_by_class_name is not None:
            print("Size of the list: " + str(len(elements_list_by_class_name)))

        elements_list_by_tag_name = driver.find_elements(By.TAG_NAME, "td")

        if elements_list_by_tag_name is not None:
            print("Size of the list: " + str(len(elements_list_by_tag_name)))

        driver.quit()


if __name__ == "__main__":

    ff = ByDemo()
    ff.test()
