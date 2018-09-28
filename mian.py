import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime

from shoes_size import men_size
from persondata import *

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.set_window_size(1200, 800)

def login():
    cnnew_url = 'https://www.nike.com/cn/launch/?s=upcoming'
    amnew_url = 'https://www.nike.com/launch/?s=upcoming'
    browser.get(cnnew_url)
    # browser.get('https://www.baidu.com')
    login_access = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button')))
    # login_access = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b')))
    '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button'
    '/html/body/div[6]/nav/div[1]/ul[2]/li[2]/button/span'
    'body > div:nth-child(6) > nav > div.gnav-member-bar.is-for--dropdown-nav.js-navContainer > ul.gnav-member-bar--right-side.nsg-font-family--base.js-navList.js-isRootNav > li.exp-join-login.gnav-member-bar--label.facet.nav-section.js-listItem.js-rootListItem > button > span'
    login_access.click()

    # browser.switch_to.parent_frame()

    # ph_num = browser.find_element_by_css_selector('#nike-unite-login-view > header > div.view-header')
    # print(ph_num.text)
    phone_input = wait.until(EC.presence_of_element_located((By.NAME, 'verifyMobileNumber')))
    code_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    phone_input.send_keys('18621549404')
    code_input.send_keys('dwAdw100%')
    code_input.send_keys(Keys.ENTER)
    login_success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > ul > li.member-nav-item.d-sm-ib.va-sm-m > div > div > button > div > span')))
    print(login_success.text)
    after_login()

# 切换成美国
def after_login():
    # country = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > header > div.d-sm-h.d-lg-b > section > ul > li:nth-child(4) > button > img')))
    time.sleep(2)
    country = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[4]/button/img')))

    country.click()
    america = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.js-modal.modal.show > div > div > div > div > div > div > ul > li:nth-child(35) > button > span')))
    america.click()

def get_shoes():
    shoes_position(7).click()
    choosesize = men_size(8.5)
    # 选择size
    # size15 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(17) > button')))
    size_selected = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child({}) > button'.format(choosesize))))
    size_selected.click()



    buttonone = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > div > button')))
    # size15.click()
    # 第一次保存继续
    buttonone.click()

    # 填写收货信息信息
    first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#first-name-shipping')))
    last_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#last-name-shipping')))
    address1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#shipping-address-1')))
    address2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#shipping-address-2')))
    city = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#city')))
    state = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#state')))
    zipcode = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zipcode')))
    country = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#country')))
    phonenum = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#phone-number')))

    first_name.send_keys(fiction_data['first_name'])
    last_name.send_keys(fiction_data['last_name'])
    address1.send_keys(fiction_data['address1'])
    # address2.send_keys(fiction_data['address2'])
    city.send_keys(fiction_data['city'])
    state.send_keys(fiction_data['state'])
    zipcode.send_keys(fiction_data['zipcode'])
    country.send_keys(fiction_data['country'])
    phonenum.send_keys(fiction_data['phonenum'])

    # 第二次保存继续
    buttontwo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.shipping-component.mt1-sm > div > span > div.mt6-sm.mb6-sm.pr0-sm.pl0-sm.ta-sm-c > button')))
    buttontwo.click()

    # 填写信用卡信息
    newcrad = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.payment-component.mt1-sm > div > span > span:nth-child(1) > span > div.ncss-row.mt4-sm > div > button.ncss-btn.custom-responsive-button.border-medium-grey.ncss-brand.pr5-sm.pl5-sm.pt3-sm.pb3-sm.pt2-md.pb2-md.u-uppercase.mb4-sm.mb4-md.ml2-md.mr4-md.d-sm-b.d-md-ib')))
    newcrad.click()

    cardnumber = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#creditCardNumber')))
    exdate = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#expirationDate')))
    cvnumber = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cvNumber')))


    cardnumber.send_keys(fiction_data['cardnumber'])
    exdate.send_keys(fiction_data['exdate'])
    cvnumber.send_keys(fiction_data['cvnumber'])

    # 第三次保存继续
    buttonthree = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.payment-component.mt1-sm > div > span > span > span > div.mt6-sm.mb6-sm.pr0-sm.pl0-sm.ta-sm-c > button')))
    buttonthree.click()

    # 最终提交
    finalsummit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div:nth-child(5) > div > div > div.mt6-sm.mb6-sm.pr0-sm.pl0-sm.ta-sm-c > button')))
    finalsummit.click()


# 要抢的鞋的位置
def shoes_position(shoesnumber):

    # line11 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > div:nth-child(3) > div.pt4-md.pt6-lg > div > section > figure:nth-child(1) > div > div > figcaption > div > div > div.cta-container.bg-white.pt6-sm.pb7-sm.pb5-lg.prl12-sm.pb8-sm.pt8-lg.ta-sm-c > a')))
    # line12 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > div:nth-child(3) > div.pt4-md.pt6-lg > div > section > figure:nth-child(2) > div > div > figcaption > div > div > div.cta-container.bg-white.pt6-sm.pb7-sm.pb5-lg.prl12-sm.pb8-sm.pt8-lg.ta-sm-c > a')))
    # line13 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div[2]/div/section/figure[1]/div/div/figcaption/div/div/div[2]/div')))
    # line21 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > div:nth-child(3) > div.pt4-md.pt6-lg > div > section > figure:nth-child(4) > div > div > figcaption > div > div > div.cta-container.bg-white.pt6-sm.pb7-sm.pb5-lg.prl12-sm.pb8-sm.pt8-lg.ta-sm-c > button')))
    # line22 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > div:nth-child(3) > div.pt4-md.pt6-lg > div > section > figure:nth-child(5) > div > div > figcaption > div > div > div.cta-container.bg-white.pt6-sm.pb7-sm.pb5-lg.prl12-sm.pb8-sm.pt8-lg.ta-sm-c > button')))
    shoes_pos = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.main-layout > div > div:nth-child(3) > div.pt4-md.pt6-lg > div > section > figure:nth-child({}) > div > div > figcaption > div > div > div.cta-container.bg-white.pt6-sm.pb7-sm.pb5-lg.prl12-sm.pb8-sm.pt8-lg.ta-sm-c > button'.format(shoesnumber))))

    return shoes_pos


def shoes_size():
    size15 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout-sections > div.size-component.mt1-sm > div.checkout-size-section-content.prl6-sm.prl0-md.checkout-section-expandable > span > ul > li:nth-child(17) > button')))




def get_nowtime():
    global nowtime2
    nowtime = datetime.datetime.now()
    nowtime2 = nowtime.strftime('%H%M%S')
    print(nowtime)
    print(nowtime2)


def startshopping():
    while int(nowtime2) < 152000:

        get_nowtime()
        time.sleep(0.01)
    else:
        print('时间到！')
        get_shoes()

if __name__ == '__main__':
    nowtime = datetime.datetime.now()
    nowtime2 = nowtime.strftime('%H%M%S')
    login()
    startshopping()