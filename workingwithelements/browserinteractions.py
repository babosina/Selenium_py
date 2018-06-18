from selenium import webdriver


class BrowserInteractions:

    def test(self):
        base_url = "http://letskodeit.teachable.com/pages/practice"
        another_url = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()

        # Open the URL
        driver.get(base_url)

        # Get Title
        title = driver.title
        print("Title of the page is: ", title)

        # Get Current Url
        current_url = driver.current_url
        print("Current Url of the page is: ", current_url)

        # Browser Refresh
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")

        # Open another Url
        driver.get(another_url)
        print(driver.current_url)

        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        print(driver.current_url)

        # Browser forward
        driver.forward()
        print("Go one step forward in browser history")

        # Get Page Source
        page_source = driver.page_source
        print(page_source)

        # Browser Close / Quit
        # driver.close()
        driver.quit()


if __name__ == "__main__":

    ff = BrowserInteractions()
    ff.test()
