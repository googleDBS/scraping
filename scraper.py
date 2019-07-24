import json
from selenium import webdriver
from openBrowser import openBrowser
import numpy as np
import xml.etree.ElementTree as ET

tree = ET.parse('newest_listings.xml')
root = tree.getroot()

# last_id = int(input("Enter max json file number: "))
last_id = 14342

# set limit
# LIMIT = 4000

# Create urls list
lines = []
for child in root:
    lines.append(child[0].text)

# Set web driver Options as needed

options = webdriver.ChromeOptions()

# load chrome with your profile settings from macbook root
options.add_argument("user-data-dir=/Users/davedavidsamuel-macbookpro/Library/Application Support/Google/Chrome")

# headless browser invokes captcha, so don't go headless
# options.add_argument('--headless')

# additional options, use if needed.
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

print("\nwebdriver open")
driver = webdriver.Chrome(options=options) # < use options=options

for j, line in enumerate(lines[last_id:]):
    # create last id index
    # if last_id > 0:
    #     num = str(last_id + j +1)
    # else:
    num = str(last_id+j)
    print(num, line, '\n')

    driver.implicitly_wait(np.random.uniform(low=1.0, high=2.0))

    # fetch url and save .html
    driver.get(line)
    html = driver.page_source
    with open('./html/'+num+'.html', mode='w') as f:
        f.write(html)

    # save_screenshot
    driver.save_screenshot('./screenshots/'+ num +'.png')
    # open browser
    data = openBrowser(driver)
    # set listing url
    data['listing'] = line

    # create empty json
    with open('./data/'+num+'.json',
              mode='w', encoding='utf-8') as f:
        json.dump([], f)
    # dump json into empty file
    with open('./data/'+num+'.json', 'w') as f:
        json.dump(data, f)

    # close browser
    # driver.close()
    print("\nwebdriver closed")
    # if j == LIMIT:
    break
# Quit webdriver
driver.quit()
