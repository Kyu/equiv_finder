import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from actions import Action

BASE_URL = "https://webapps.wichita.edu/TransferEquiv/"
COURSE_CODES = ("CS 101", )

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.get(BASE_URL)

do = Action(driver, COURSE_CODES)

# do.select_state(3)
# do.select_school(2)  # selenium.common.exceptions.NoSuchElementException
# do.select_all_subjects()  # selenium.common.exceptions.InvalidSelectorException

state_id = 0

argc = len(sys.argv)

if argc == 2:
    state_id = int(sys.argv[1])
else:
    state_id = 0

if argc == 3:
    school_id = int(sys.argv[2])
else:
    school_id = 0

while True:
    state_id += 1
    print(f"State ID = {state_id}")
    try:
        do.select_state(state_id)
        while True:
            school_id += 1
            try:
                do.select_school(school_id)
                do.select_all_subjects()
                do.submit_form()

                do.find_text_in_table()
                do.go_back()
            except NoSuchElementException:
                break
    except NoSuchElementException:
        break

input("Press enter to exit")
driver.close()
