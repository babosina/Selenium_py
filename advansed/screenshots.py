from selenium import webdriver


class Screenshots:

    def test(self):

        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("abc@email.com")
        driver.find_element_by_id("user_password").send_keys("abc")
        driver.find_element_by_name("commit").click()

        destination = "D:\\Selenium_py\\test.png"
        try:
            driver.save_screenshot(destination)
            print("Screenshot saved to directory")
        except:
            print("An error occurred")

        driver.quit()


if __name__ == "__main__":
    ff = Screenshots()
    ff.test()
