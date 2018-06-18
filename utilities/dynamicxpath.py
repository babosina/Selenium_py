from selenium import webdriver
import time


class DynamicXpath:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("test@email.com")
        driver.find_element_by_id("user_password").send_keys("abcabc")
        driver.find_element_by_name("commit").click()
        driver.get("https://learn.letskodeit.com/courses")

        driver.find_element_by_id("search-courses").send_keys("JavaScript")

        _course = '//div[contains(@class, "course-listing-title") and contains(text(), "{}")]'
        _courseLocator = _course.format("JavaScript for")

        time.sleep(2)

        driver.find_element_by_xpath(_courseLocator).click()

        driver.quit()


if __name__ == "__main__":
    ff = DynamicXpath()
    ff.test()
