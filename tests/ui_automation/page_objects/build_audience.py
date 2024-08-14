from telnetlib import EC

from selenium.webdriver.common.keys import Keys

from tests.ui_automation.page_objects.base_page import Base_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


class BuildAudience(Base_Page):

    # init constructor
    def __init__(self, driver, shadow):
        super().__init__(driver, shadow)

    # locators
    portal_login = lambda self: self.shadow.find_element("portal-login")
    username = lambda self: self.shadow.get_shadow_element(self.portal_login(),
                                                           "#username")
    password_ch1 = lambda self: self.shadow.get_shadow_element(self.portal_login(),
                                                               "portal-password")
    password_ch2 = lambda self: self.shadow.get_shadow_element(self.password_ch1(),
                                                               "#password")
    login_button = lambda self: self.shadow.get_shadow_element(self.portal_login(), "#eid-login-btn")

    # AE
    portal_app_container = lambda self: self.shadow.find_element("portal-app-container")
    iframe_ch1 = lambda self: self.shadow.get_shadow_element(self.portal_app_container(),
                                                             "portal-iframe-container")
    iframe_ch2 = lambda self: self.shadow.get_shadow_element(self.iframe_ch1(),
                                                             "portal-iframe-element")
    iframe_ch3 = lambda self: self.shadow.get_shadow_element(self.iframe_ch2(),
                                                             "iframe")

    omni_app_container = lambda self: self.shadow.find_element("omni-app-container")
    construct_view_session = lambda self: self.shadow.get_shadow_element(self.omni_app_container(),
                                                                         "construct-view-session")
    session_form = lambda self: self.shadow.get_shadow_element(self.construct_view_session(),
                                                               "#session-form")
    form_field_title = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                   "omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > om2-form-field:nth-child(2) > om2-form-field-title:nth-child(1) > p:nth-child(1)")
    audience_name_input = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                      "input[name='audience_name']")
    root_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                    "omni-style > form > fieldset:nth-child(1) > div > div:nth-child(6) > div:nth-child(1) > om2-form-field > om2-form-field-dropdown > om2-dropdown > div > om2-dropdown-impl")
    root_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.root_dropdown_ch1(),
                                                                    "#dropdown-trigger-container > omni-icon")
    root_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.root_dropdown_ch2(),
                                                                    "div")
    option_count = lambda self: self.shadow.get_all_shadow_element(self.root_dropdown_ch1(),
                                                               "div[class='is-single']> .dropdown-item")
    root_dropdown_option_nth = lambda self, n: self.shadow.get_shadow_element(self.root_dropdown_ch1(),
                                                                        f" omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    first_clild_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                           "omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(2) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    first_clild_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.first_clild_dropdown_ch1(),
                                                                           ".ignore-focus.is-pulled-right")
    first_clild_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.first_clild_dropdown_ch2(),
                                                                           "div[part='icon']")
    first_child_nth_option = lambda self,n: self.shadow.get_shadow_element(self.first_clild_dropdown_ch1(),
                                                                         f"omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    first_option_count = lambda self: self.shadow.get_all_shadow_element(self.first_clild_dropdown_ch1(),
                                                                   "div[class='is-single']> .dropdown-item")

    second_child_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                            " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(3) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    second_child_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.second_child_dropdown_ch1(),
                                                                            ".ignore-focus.is-pulled-right")
    second_child_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.second_child_dropdown_ch2(),
                                                                            "div[part='icon']")
    second_child_nth_option = lambda self,n: self.shadow.get_shadow_element(self.second_child_dropdown_ch1(),
                                                                            " omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    second_option_count = lambda self: self.shadow.get_all_shadow_element(self.second_child_dropdown_ch1(),
                                                                         "div[class='is-single']> .dropdown-item")

    third_child_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                           "omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    third_child_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.third_child_dropdown_ch1(),
                                                                           ".ignore-focus.is-pulled-right")
    third_child_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.third_child_dropdown_ch2(),
                                                                           "div[part='icon']")
    third_child_nth_option = lambda self, n: self.shadow.get_shadow_element(self.third_child_dropdown_ch1(),
                                                                           f"omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    third_option_count = lambda self: self.shadow.get_all_shadow_element(self.third_child_dropdown_ch1(),
                                                                          "div[class='is-single']> .dropdown-item")

    fourth_child_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                            " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(2) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    fourth_child_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.fourth_child_dropdown_ch1(),
                                                                            ".ignore-focus.is-pulled-right")
    fourth_child_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.fourth_child_dropdown_ch2(),
                                                                            "div[part='icon']")
    fourth_child_nth_option = lambda self,n: self.shadow.get_shadow_element(self.fourth_child_dropdown_ch1(),
                                                                            f" omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    fourth_option_count = lambda self: self.shadow.get_all_shadow_element(self.fourth_child_dropdown_ch1(),
                                                                         "div[class='is-single']> .dropdown-item")

    questions_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                         " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(9) > div:nth-child(1) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    questions_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.questions_dropdown_ch1(),
                                                                         ".ignore-focus.is-pulled-right")
    questions_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.questions_dropdown_ch2(),
                                                                         "div[part='icon']")
    question_option_nth = lambda self,n: self.shadow.get_shadow_element(self.questions_dropdown_ch1(),
                                                                      f"omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    question_option_count = lambda self: self.shadow.get_all_shadow_element(self.questions_dropdown_ch1(),
                                                                         "div[class='is-single']> .dropdown-item")

    option_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),"omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(9) > div:nth-child(2) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    option_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.option_dropdown_ch1(),".ignore-focus.is-pulled-right")
    option_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.option_dropdown_ch2(),"div[part='icon']")
    option_option_nth   = lambda self,n: self.shadow.get_shadow_element(self.option_dropdown_ch1(), f" omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    options_option_count        = lambda self: self.shadow.get_all_shadow_element(self.option_dropdown_ch1(),
                                                                         "div[class='is-multi']> .dropdown-item")

    waves_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                     " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(9) > div:nth-child(3) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    waves_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.waves_dropdown_ch1(), ".ignore-focus.is-pulled-right")
    waves_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.waves_dropdown_ch2(), "div[part='icon']")
    waves_option_nth = lambda self,n: self.shadow.get_shadow_element(self.waves_dropdown_ch1(), f" omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    waves_option_count = lambda self: self.shadow.get_all_shadow_element(self.waves_dropdown_ch1(),
                                                                         "div[class='is-multi']> .dropdown-item")
    location_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(),
                                                                        "omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(10) > div:nth-child(1) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    location_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.location_dropdown_ch1(),
                                                                        ".ignore-focus.is-pulled-right")
    location_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.location_dropdown_ch2(),
                                                                        "div[part='icon']")
    location_option_nth = lambda self,n: self.shadow.get_shadow_element(self.location_dropdown_ch1(),
                                                                        f" omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    location_option_count = lambda self: self.shadow.get_all_shadow_element(self.location_dropdown_ch1(),
                                                                         "div[class='is-multi']> .dropdown-item")

    spliters_dropdown_ch1 = lambda self: self.shadow.get_shadow_element(self.session_form(), "omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > div:nth-child(1) > div:nth-child(10) > div:nth-child(2) > om2-form-field:nth-child(1) > om2-form-field-dropdown:nth-child(2) > om2-dropdown:nth-child(1) > div:nth-child(1) > om2-dropdown-impl:nth-child(2)")
    spliters_dropdown_ch2 = lambda self: self.shadow.get_shadow_element(self.spliters_dropdown_ch1(), ".ignore-focus.is-pulled-right")
    spliters_dropdown_ch3 = lambda self: self.shadow.get_shadow_element(self.spliters_dropdown_ch2(), "div[part='icon']")
    spliters_option_nth = lambda self,n: self.shadow.get_shadow_element(self.spliters_dropdown_ch1(), f"omni-style:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child({n})")
    spliters_option_count = lambda self: self.shadow.get_shadow_element(self.spliters_dropdown_ch1(), "div[class='is-multi']> .dropdown-item")


    submit_btn = lambda self: self.shadow.get_shadow_element(self.session_form(), " omni-style:nth-child(1) > form:nth-child(1) > fieldset:nth-child(2) > slot:nth-child(2) > button:nth-child(1)")

    def login(self, username, password):
        # login to the portal
        self.enter_value(self.username(), username)
        self.click_element(self.login_button())
        sleep(3)
        self.enter_value(self.password_ch2(), password)
        self.click_element(self.login_button())
        sleep(40)
    def audience_name(self):
        num = random.randint(10, 99)
        name = f"auto_test_{num}"
        return name

    def random_option(self, min_value, max_value):
        """Generate a random number between min_value and max_value, inclusive."""
        if min_value > max_value:
            raise ValueError("min_value should not be greater than max_value")
        return random.randint(min_value, max_value)
