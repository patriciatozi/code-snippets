from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

main_url = 'http://books.toscrape.com/'
secundary_url = 'https://www.google.com/'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get(main_url)

# Open a new window
driver.execute_script("window.open('');")

# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])

driver.get(secundary_url)

time.sleep(2)

# Closing new_url tab
driver.close()

time.sleep(2)

# Switching to old tab
driver.switch_to.window(driver.window_handles[0])

driver.quit()