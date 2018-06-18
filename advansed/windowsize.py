from selenium import webdriver


class WindowSize:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        height = driver.execute_script("return window.innerHeight;")
        wigth = driver.execute_script("return window.innerWidth;")
        print("Height is: ", height)
        print("Width is: ", wigth)

        driver.quit()


if __name__ == "__main__":
    ff = WindowSize()
    ff.test()
