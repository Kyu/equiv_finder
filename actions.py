import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import numpy as np


state_picker_id = 'MainContent_Dl_state'
school_picker_id = 'MainContent_Dl_institution'
subject_picker_id = 'MainContent_Dl_subject'
submit_button_id = 'MainContent_Bt_newresults'

school_name_style = "color:Red;font-size:14pt;font-weight:bold;"

all_subjects = '*All Subjects*'

"""
Skew:
a = 1  # skewness parameter
loc = -3.5  # mean
scale = 1.5  # standard deviation
"""
normal_weights = [0.03142141560548123, 0.031719589657341105, 0.031939813553827336, 0.032080983484904034,
                  0.03214260278076863, 0.032124781081125174, 0.032028225684008725, 0.03185422535982122,
                  0.03160462704870378, 0.031281805979190246, 0.03088862985075278, 0.030428417810360705,
                  0.029904895022066304, 0.02932214367801717, 0.02868455132884567, 0.02799675742132883,
                  0.027263598922284756, 0.0264900558810788, 0.025681197740459457, 0.024842131148665732,
                  0.023977949957031723, 0.023093688009017604, 0.022194275241165733, 0.021284497526374603,
                  0.02036896059749848, 0.01945205829688807, 0.01853794530717797, 0.017630514432262684,
                  0.016733378416590953, 0.015849856216968307, 0.014982963575020885, 0.014135407681073206,
                  0.013309585671878484, 0.012507586665590976, 0.011731197007518988, 0.010981908379259898,
                  0.010260928411322548, 0.009569193434664584, 0.008907383008970548, 0.00827593587414495,
                  0.007675066985516507, 0.007104785311745134, 0.006564912096498903, 0.006055099309757045,
                  0.005574848041277424, 0.005123526616585876, 0.00470038824411452, 0.004304588030233702,
                  0.003935199226366953, 0.0035912285987163765, 0.0032716308360068273, 0.0029753219338110944,
                  0.0027011915152492325, 0.0024481140670364943, 0.002214959086919555, 0.0020006001534761167,
                  0.0018039229420905903, 0.0016238322217264763, 0.001459257875992969, 0.0013091599990696977,
                  0.0011725331224468596, 0.0010484096323059376, 0.0009358624398623508, 0.0008340069682709472,
                  0.0007420025199113799, 0.0006590530871718165, 0.0005844076683777462, 0.0005173601484011366,
                  0.00045724880085764794, 0.00040345546576914845, 0.00035540445323819874, 0.00031256122014227154,
                  0.00027443086318947106, 0.0002405564679553259, 0.00021051734980303402, 0.0001839272189290199,
                  0.0001604322982151976, 0.0001397094191440024, 0.00012146411777012994, 0.00010542874966537739,
                  9.136063987552059e-05, 7.904028126110325e-05, 6.826959214308712e-05, 5.887024194124771e-05,
                  5.068205147638164e-05, 4.3561472802303756e-05, 3.738015183338122e-05, 3.202357562920189e-05,
                  2.7389804979625006e-05, 2.3388291889500512e-05, 1.9938780680593844e-05, 1.6970290696031684e-05,
                  1.442017799698541e-05, 1.2233272969437613e-05, 1.0361090398014467e-05, 8.761108301665951e-06,
                  7.3961116505619775e-06, 6.233596983677071e-06, 5.245233911553095e-06, 4.406379508787691e-06]


def random_pause(func):
    def wrapper(self, *args, **kwargs):
        sleep_time = np.random.choice(np.arange(1, 101), p=normal_weights)
        time.sleep(sleep_time / 10)
        func(self, *args, **kwargs)

    return wrapper


class Action:
    def __init__(self, driver: webdriver.Chrome, text=()):
        self.text = text
        self.driver = driver

    def find_text_in_table(self, text=None):
        if not text:
            txt = self.text
        else:
            txt = text

        school_name = self.driver.find_element(By.XPATH, f"//td[@style='{school_name_style}']").text

        table_elements = self.driver.find_elements(By.TAG_NAME, 'td')

        printed_name = False
        for el in table_elements:
            element_txt = el.text.lower()

            for q in txt:
                if q.lower() in element_txt:
                    if not printed_name:
                        print()
                        print(f"***** {school_name} ****")
                        printed_name = True
                    print(f"Found {q}")

    @random_pause
    def select_state(self, index: int):
        self.driver.find_element(By.ID, state_picker_id).click()
        dropdown = self.driver.find_element(By.ID, state_picker_id)
        Select(dropdown).select_by_index(index)

    @random_pause
    def select_school(self, index: int):
        dropdown = self.driver.find_element(By.ID, school_picker_id)
        Select(dropdown).select_by_index(index)

    @random_pause
    def select_all_subjects(self):
        dropdown = self.driver.find_element(By.ID, subject_picker_id)
        Select(dropdown).select_by_index(1)

    @random_pause
    def submit_form(self):
        self.driver.find_element(By.ID, submit_button_id).click()

    @random_pause
    def go_back(self):
        self.driver.back()
