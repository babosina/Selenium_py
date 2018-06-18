from selenium import webdriver


class FindByXpathCss:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_xpath = driver.find_element_by_xpath("//input[@id='name']")

        if element_by_xpath is not None:
            print("Element found by Xpath")

        element_by_css = driver.find_element_by_css_selector("#displayed-text")

        if element_by_css is not None:
            print("Element found by Css")

        driver.quit()


ff = FindByXpathCss()
ff.test()
