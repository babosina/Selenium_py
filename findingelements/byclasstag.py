from selenium import webdriver


class FindByClassTag:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(base_url)
        element_by_class = driver.find_element_by_class_name("inputs")
        element_by_class.send_keys("hello")

        if element_by_class is not None:
            print("Element found by Class")

        element_by_tag = driver.find_element_by_tag_name("h1")
        print(element_by_tag.text)

        if element_by_tag is not None:
            print("Element found by Tag")

        driver.quit()


if __name__ == "__main__":

    ff = FindByClassTag()
    ff.test()
