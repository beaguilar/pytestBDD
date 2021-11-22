from tests import retirement
from pytest_bdd import scenarios, parsers, given, when, then

from retirement import calculate_retirement_age

#Pytest bdd for invalid years.

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
@given('the SSA retirement age calculator')
def search_for_web_phrase(calculator):
    calculator.get(get_invalid_year_range()

# When Steps
@when(parsers.cfparse('year of birth is entered')))
def birth_year(year):
    assert isinstance(year, object)
    birth_year().add(year)

# Then Steps
@then(parsers.cfparse('system returns invalid year range'))
def get_invalid_year_range(year):
      year = int(year)
      if year < 1900:
          raise ValueError(f"Birth year \"(year)\" must be no earlier than 1900")
      elif year >= 2999:
          raise ValueError(f'Birth year"(year)" must be earlier than 2021')
      return year