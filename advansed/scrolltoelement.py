from selenium import webdriver
import time


class ScrollToElement:

    def test(self):

        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Scroll down
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(3)

        # Scroll up
        driver.execute_script("window.scrollBy(0, -800);")
        time.sleep(3)

        # Scroll element into view
        element = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)

        # Native way to scroll element into view
        driver.execute_script("window.scrollBy(0, -800);")
        location = element.location_once_scrolled_into_view
        print("Location: ", location)

        driver.quit()


if __name__ == "__main__":
    ff = ScrollToElement()
    ff.test()
