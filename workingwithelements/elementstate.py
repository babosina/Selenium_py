from selenium import webdriver


class ElementState:

    def test(self):
        base_url = "https://google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element_1 = driver.find_element_by_id("lst-ib")
        element_1.send_keys("habr")
        print("Element_1 state is even? ", element_1.is_enabled())

        driver.quit()


if __name__ == "__main__":
    ff = ElementState()
    ff.test()
