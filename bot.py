from webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
import smtplib
import time
import random

class Bot:
    def __init__(self, start_page_url):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def refresh(self):
        self.webdriver.refresh()

    def go_to_festival_page(self, festival_name):
        self.webdriver.fill_in_input_field("/html/body/div[1]/div[1]/section/div[2]/div/div/div[1]/label/div[2]/input", festival_name)
        time.sleep(1)
        self.select_item_by_x_path('//*[@id="site-search-item-0"]')


    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def select_item(self, item_name):
        item = self.webdriver.find_element_by_visible_text(item_name)
        return self.webdriver.click_on_element(item)

    def select_item_by_x_path(self, item_x_path):
        item = self.webdriver.find_element_by_x_path(item_x_path)
        return self.webdriver.click_on_element(item)

    def select_colorway(self, item_colorway_position):
        colorway_box_x_path = '//*[@id="styles"]/ul/li[{}]'.format(
            item_colorway_position)
        colorway_box = self.webdriver.find_element_by_x_path(
            colorway_box_x_path)
        return self.webdriver.click_on_element(colorway_box)

    def select_size(self, item_size):
        return self.webdriver.select_dropdown_option('//*[@id="size-options"]', item_size)

    def add_to_cart(self):
        add_to_cart_button = self.webdriver.find_element_by_visible_text(
            "add to basket")
        return self.webdriver.click_on_element(add_to_cart_button)

    def go_to_checkout(self):
        checkout_button = self.webdriver.find_element_by_visible_text(
            "check out")
        return self.webdriver.click_on_element(checkout_button)

    def fill_in_checkout_form(self, billing_info):
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[1]/td/input', billing_info["fullName"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[2]/td/input', billing_info["email"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[3]/td/input', billing_info["phone"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[4]/td/input', billing_info["address"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[7]/td/input', billing_info["city"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[8]/td/input', billing_info["postcode"]
        )
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="credit card number"]', billing_info["ccNumber"]
        )
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_month"]', billing_info["expM"])
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_year"]', billing_info["expY"])
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="cvv"]', billing_info["cvv"])
        self.webdriver.select_dropdown_option(
            '//*[@id="order_billing_country"]', billing_info["country"].upper()
        )

    def agree_to_terms(self):
        terms_checkbox = self.webdriver.find_element_by_x_path(
            '//*[@id="order_terms"]')
        return self.webdriver.click_on_element(terms_checkbox)

    def process_payment(self):
        process_payment_button = self.webdriver.find_element_by_visible_text(
            "process payment")
        return self.webdriver.click_on_element(process_payment_button)

    def go_to_ticket_page(self, otherCategory, ticketName):
        if otherCategory == "":
            self.select_item(ticketName)
        else:
            self.select_item(otherCategory)
            self.select_item(ticketName)

    def find_available(self):
        try:
            self.webdriver.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/span")
        except NoSuchElementException:
            return True
        return False


    def refresher(self):
        random_decimal = random.randint(40000, 120000) / 10000
        time.sleep(random_decimal)
        self.refresh()

    def reserve_ticket(self):
        self.select_item_by_x_path("/html/body/div[1]/div[2]/div[3]/a[1]")
        self.select_item_by_x_path("/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/div[3]/button")

    def dial_number(self, twilioNumber, number, sid, token):
        TWIML_INSTRUCTIONS_URL = \
            "https://static.fullstackpython.com/phone-calls-python.xml"
        client = Client(sid, token)

        client.calls.create(to=number, from_=twilioNumber,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

