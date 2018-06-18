from selenium import webdriver


class RunFF:

    def test(self):
        # instantiate FF browser
        driver = webdriver.Firefox()

        # open provided URL
        driver.get("https://google.com")


ff = RunFF()
ff.test()
