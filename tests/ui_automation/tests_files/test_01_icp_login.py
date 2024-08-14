import pytest
from tests.ui_automation.tests_files.test_base import BaseTest
from tests.ui_automation.page_objects.build_audience import BuildAudience
from time import sleep


@pytest.mark.regression
class TestLoginPage(BaseTest):

    @pytest.mark.sanity
    def test_01_login_page(self):
        build_audience = BuildAudience(self.driver, self.shadow)
        # sleep(10)
        text = build_audience.get_text(build_audience.form_field_title())
        if text == "Audience Explorer (GWI)":

            build_audience.enter_value(build_audience.audience_name_input(), build_audience.audience_name())
            #root
            build_audience.click_element(build_audience.root_dropdown_ch3())
            num = len(build_audience.option_count())
            build_audience.click_element(build_audience.root_dropdown_option_nth(build_audience.random_option(1,num)))

            #first child
            sleep(5)
            build_audience.click_element(build_audience.first_clild_dropdown_ch3())
            num = len(build_audience.first_option_count())
            # value = build_audience.get_attribute(build_audience.first_child_nth_option(num), "innerText")
            build_audience.click_element(build_audience.first_child_nth_option(build_audience.random_option(1, num)))
            sleep(5)

            #second child
            build_audience.click_element(build_audience.second_child_dropdown_ch3())
            num = len(build_audience.second_option_count())

            # value = build_audience.get_attribute(build_audience.second_child_nth_option(1), "innerText")
            build_audience.click_element(build_audience.second_child_nth_option(build_audience.random_option(1,num)))
            sleep(5)

            #third child
            build_audience.click_element(build_audience.third_child_dropdown_ch3())
            num = len(build_audience.third_option_count())

            # value = build_audience.get_attribute(build_audience.third_child_nth_option(1), "innerText")
            build_audience.click_element(build_audience.third_child_nth_option(build_audience.random_option(1,num)))
            sleep(5)

            #fourth child
            build_audience.click_element(build_audience.fourth_child_dropdown_ch3())
            num = len(build_audience.fourth_option_count())

            # value = biuld_audience.get_attribute(build_audience.fourth_child_nth_option(1), "innerText")
            build_audience.click_element(build_audience.fourth_child_nth_option(build_audience.random_option(1,num)))
            sleep(5)


            #question
            build_audience.click_element(build_audience.questions_dropdown_ch3())
            num = len(build_audience.question_option_count())

            # value = build_audience.get_attribute(build_audience.questions_nth_option(1), "innerText")
            build_audience.click_element(build_audience.question_option_nth(build_audience.random_option(1,num)))
            sleep(5)

            #option
            build_audience.click_element(build_audience.option_dropdown_ch3())
            num = len(build_audience.options_option_count())
            build_audience.click_element(build_audience.option_option_nth(build_audience.random_option(1,num)))
            sleep(5)

            #waves

            build_audience.click_element(build_audience.waves_dropdown_ch3())
            num = len(build_audience.waves_option_count())
            build_audience.click_element(build_audience.waves_option_nth(build_audience.random_option(1,num)))
            sleep(5)

            #location
            build_audience.click_element(build_audience.location_dropdown_ch3())
            num = len(build_audience.location_option_count())
            build_audience.click_element(build_audience.location_option_nth(build_audience.random_option(1,num)))
            sleep(5)

            #spliters
            # build_audience.click_element(build_audience.spliters_dropdown_ch3())
            # num = len(build_audience.spliters_option_count())
            # build_audience.click_element(build_audience.spliters_option_nth(build_audience.random_option(1,num)))
            # sleep(5)

            #save
            build_audience.click_element(build_audience.submit_btn())
            sleep(20)
            curr_url = self.driver.current_url
            print(curr_url)
            if "my-workspace" in curr_url:
                assert True
















