from selenium.webdriver import Keys

from tests import retirement
from pytest_bdd import scenarios, parsers, given, when, then
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from retirement import calculate_retirement_age

##Just a pytest bdd I wrote for finding the main SSA website.

TYPES = {'Number':int, 'future':int}

CONVERTERS = {
    'month':int,
    'initial':int,
    'age':int,
    'year':int
}

# Constants
Website_for_SSA  = 'https://www.ssa.gov/benefits/retirement/planner/ageincrease.html)'

# Scenarios
scenarios("../features/retirement.feature", example_converters=CONVERTERS)

# Given Steps
@given(parsers.cfparse('the SSA home page is displayed'))
def home_screen(browser):
       browser.get(Website_for_SSA)

# When Steps
@when(parsers.parse('the user searches for "{keyword}"'))
def search_for_keyword_input(browser, keyword):
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(keyword + Keys.RETURN)

# Then Steps
@then(parsers.parse('results are shown for "{keyword}"'))
def results(browser, keyword):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elments_by_xpath('//div')) > 0
    search_input = browser.find_element_by_id('search_from_input')
    assert search_input.get_attribute('value') == keyword
