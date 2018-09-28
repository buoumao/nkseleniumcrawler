# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from mian import wait, EC, By

# men 17
def men_size(size):
    size_data = {
        '6' : '1',
        '6.5' : '2',
        '7' : '3',
        '7.5' : '4',
        '8' : '5',
        '8.5' : '6',
        '9' : '7',
        '9.5' : '8',
        '10' : '9',
        '10.5' : '10',
        '11' : '11',
        '11.5' : '12',
        '12' : '13',
        '12.5' : '14',
        '13' : '15',
        '14' : '16',
        '15' : '17',
    }
    sizecss = size_data['{}'.format(size)]
    return sizecss
    # size6_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(2) > button')))
    # size7 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(3) > button')))
    # size7_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(4) > button')))
    # size8 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(5) > button')))
    # size8_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(6) > button')))
    # size9 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(7) > button')))
    # size9_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(8) > button')))
    # size10 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(9) > button')))
    # size10_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(10) > button')))
    # size11 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(11) > button')))
    # size11_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(12) > button')))
    # size12 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(13) > button')))
    # size12_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(14) > button')))
    # size13 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(15) > button')))
    # size14 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(16) > button')))
    # size15 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(17) > button')))

# women 15
def women_size(size):
    size_data = {
        '5': '1',
        '5.5': '2',
        '6': '3',
        '6.5': '4',
        '7': '5',
        '7.5': '6',
        '8': '7',
        '8.5': '8',
        '9': '9',
        '9.5': '10',
        '10': '11',
        '10.5': '12',
        '11': '13',
        '11.5': '14',
        '12': '15',
    }
    sizecss = size_data['{}'.format(size)]
    return sizecss
#     size5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size5_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size6 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size6_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size7 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size7_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size8 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size8_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size9 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size9_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size10 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size10_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size11 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size11_5 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
#     size12 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))

# men and women 19
def menandwomen_size():
    pass