from selenium import webdriver


class FindByIdName:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("Element found by ID")

        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_name is not None:
            print("Element found by Name")

        driver.quit()


ff = FindByIdName()
ff.test()
