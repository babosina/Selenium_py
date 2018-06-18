from selenium import webdriver
import time


class SwitchToWindow:

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Find parent handle -> Main Window
        parent_handle = driver.current_window_handle
        print("Parent handle: ", parent_handle)

        # Find open window button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(3)

        # Find all handles
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: ", handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window: ", handle)
                time.sleep(3)  # wait for the page to download completely
                driver.find_element_by_id("search-courses").send_keys("python")
                time.sleep(3)
                driver.close()  # closes current window
                break

        # Switch back to the parent handle
        driver.switch_to.window(parent_handle)
        driver.find_element_by_id("name").send_keys("TEST")
        time.sleep(3)

        driver.quit()


if __name__ == "__main__":
    ff = SwitchToWindow()
    ff.test()
