import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def start():
    # load driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options)

    # load website
    driver.get('https://www.flipkart.com/')
    driver.maximize_window()
    time.sleep(2)

    # close login dialog
    try:
        close_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/span')
        close_button.click()
        time.sleep(2)
    except:
        pass

    # search
    search_input = driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
    search_input.send_keys("TV")
    search_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
    search_button.click()
    time.sleep(2)

    # filters
    # select Samsung
    samsung_checkbox = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/label/div[1]')
    samsung_checkbox.click()
    time.sleep(2)

    # select price-low to high
    price_checkbox = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[3]')
    price_checkbox.click()
    time.sleep(2)

    # store original window
    original_window = driver.window_handles[0]

    # select listings
    for i in range(2, 10):
        item = driver.find_element(By.XPATH, f'//*[@id="container"]/div/div[3]/div/div[2]/div[{i}]/div/div/div')
        # scroll to item
        driver.execute_script("arguments[0].scrollIntoView();", item)
        time.sleep(3)

        item.click()
        time.sleep(3)
        # store new window
        new_window = driver.window_handles[1]
        # switch to new window
        driver.switch_to.window(new_window)

        # check "GO TO CART" button
        try:
            cart_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
            if cart_button.is_enabled():
                # go to "Checkout" page
                cart_button.click()
                time.sleep(10)
                # break
                break
            else:
                time.sleep(5)
                driver.close()
                time.sleep(2)
                driver.switch_to.window(original_window)
                time.sleep(2)
        except:
            # close the current tab
            time.sleep(5)
            driver.close()
            time.sleep(2)
            driver.switch_to.window(original_window)
            time.sleep(2)

    # close driver
    driver.quit()


if __name__ == '__main__':
    start()



