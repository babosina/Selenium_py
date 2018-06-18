from selenium import webdriver


class FindByLinkText:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_link_text = driver.find_element_by_link_text("Login")

        if element_by_link_text is not None:
            print("Element found by LinkText")

        element_by_partial_link_text = driver.find_element_by_partial_link_text("acti")

        if element_by_partial_link_text is not None:
            print("Element found by Partial LinkText")

        driver.quit()


ff = FindByLinkText()
ff.test()
