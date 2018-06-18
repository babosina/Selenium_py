from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class MouseHovering:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        element_to_click_locator = '//div[@class="mouse-hover-content"]//a[text()="Top"]'
        element = driver.find_element_by_id("mousehover")

        # top_link = driver.find_element_by_xpath(element_to_click_locator)
        # top_link.click()

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered the element")
            time.sleep(2)

            top_link = driver.find_element_by_xpath(element_to_click_locator)
            # top_link.click()
            actions.move_to_element(top_link).click().perform()
            print("Item clicked")
            time.sleep(2)
        except:
            print("Mouse failed to hover the element")

        driver.quit()


if __name__ == "__main__":
    ff = MouseHovering()
    ff.test()
