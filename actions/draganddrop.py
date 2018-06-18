from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class DragAndDrop:

    def test(self):
        base_url = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        driver.switch_to.frame(0)

        from_element = driver.find_element_by_id("draggable")
        to_element = driver.find_element_by_id("droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(from_element, to_element).perform()
            # actions.click_and_hold(from_element).perform()
            # actions.move_to_element(to_element).release().perform()
            print("Element moved with success")
        except:
            print("Drag and Drop failed")

        driver.quit()


if __name__ == "__main__":
    ff = DragAndDrop()
    ff.test()
