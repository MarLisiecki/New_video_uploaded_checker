import yaml
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

login_url = "https://edu.dokodu.dev/wp-login.php"
bootcamp_url = "https://edu.dokodu.dev/pystart-pl-dwoch-prowadzacych-i-python/"
conf = yaml.load(open('login_data.yml'))
your_email = conf['dk_user']['email']
your_password = conf['dk_user']['password']
modules = ['1', '2']
my_options = Options()
my_options.add_argument('--headless')
my_options.add_argument('--disable-gpu')



def login(url, user_login, username, user_pass, password, wp_submit):
    driver.get(url)
    driver.find_element_by_id(user_login).send_keys(username)
    driver.find_element_by_id(user_pass).send_keys(password)
    driver.find_element_by_id(wp_submit).click()


def get_lessons_quantity(number_of_lessons):
    for i in range(0, 2):
        xpath_elements = driver.find_element_by_xpath(
            '//*[@id="course-navigation-section"]/div/div[' + modules[i] + ']/div/ul[2]')
        number_of_lessons += xpath_elements.text.count('\n') + 1
        print(number_of_lessons)
    return number_of_lessons



def compare_numbers(lessons_quantity):
    if lessons_quantity == 13:
        print('Nasz Senpai nic nie wrzucił :/ ')
    if lessons_quantity > 13:
        print('Nowe lekcje wleciały')


if __name__ == '__main__':
    driver = webdriver.Chrome(options = my_options)
    login(login_url, "user_login", your_email, "user_pass", your_password, "wp-submit")
    driver.get(bootcamp_url)
    for i in range(0,5):
        lessons_quantity = get_lessons_quantity(0)
        compare_numbers(lessons_quantity)
        time.sleep(15 * 60)
        driver.refresh()
