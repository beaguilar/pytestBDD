import pytest

from retirement import calculate_retirement_age,calculate_retirement_date


#
# def test_calculate_retirement_age_when_birth_year_greater_than_equal_3000():
#     with pytest.raises(ValueError):
#         calculate_retirement_age(3000)
#
# def test_calculate_retirement_age_when_birth_year_less_than_equal_1900():
#     with pytest.raises(ValueError):
#         calculate_retirement_age(1899)

## Equivalance tests for all years/ranges and checking if they are valid inputs.

def test_calculate_retirement_age_input_1937():
     assert calculate_retirement_age(1937) == (65,0)

def test_calculate_retirement_age_input_1938():
     assert calculate_retirement_age(1938) == (65, 2)

def test_calculate_retirement_age_input_1939():
     assert calculate_retirement_age(1939) == (65, 4)

def test_calculate_retirement_age_input_1940():
     assert calculate_retirement_age(1940) == (65, 6)

def test_calculate_retirement_age_input_1941():
     assert calculate_retirement_age(1941) == (65, 8)

def test_calculate_retirement_age_input_1942():
     assert calculate_retirement_age(1942) == (65, 10)



##After many tries I finally got the test function to accept multiple inputs
##Using the suggestion in the original retirement file.

# def pytest_generate_tests(metafunc):
#    if "param1" in metafunc.fixturenames:
#       if metafunc.config.getoption("all"):
#          end = 5
#       else:
#          end = 2
#       metafunc.parametrize("param1", range(end))
## This is the example I was able to base my function off of.
## In return I have made the range to function to start at 1943 and end at 1955
## Pycharm told me the [] brackets were not needed so I removed them.

@pytest.mark.parametrize("x", range (1943, 1955))
def test_calculate_retirement_age_input_1940(x):
      assert calculate_retirement_age(x) == (66,0)

def test_calculate_retirement_age_input_1955():
     assert calculate_retirement_age(1955) == (66, 2)

def test_calculate_retirement_age_input_1956():
     assert calculate_retirement_age(1956) == (66, 4)

def test_calculate_retirement_age_input_1957():
     assert calculate_retirement_age(1957) == (66, 6)

def test_calculate_retirement_age_input_1958():
     assert calculate_retirement_age(1958) == (66, 8)

def test_calculate_retirement_age_input_1959():
     assert calculate_retirement_age(1959) == (66, 10)

## I created this function to make sure this will return any age year after 1960
## as "67,0, I created it to end before the upper bound of 3000
@pytest.mark.parametrize("x", range (1960, 2999))
def test_calculate_retirement_age_input_1940(x):
      assert calculate_retirement_age(x) == (67,0)

def test_calculate_retirement_age_input_1959_bad_input():
     with pytest.raises(ValueError):
          calculate_retirement_age(39)

def test_calculate_retirement_age_bad_input_for_1959():
     with pytest.raises(ValueError):
          calculate_retirement_age("pie")

## Boundary Conditions for the Retirement Age- Should be a lower bound of 1900 and upper
## bound of 3000

def test_lower_bound():
     with pytest.raises(ValueError):
          calculate_retirement_age(1899)

def test_upper_bound():
     with pytest.raises(ValueError):
          calculate_retirement_age(3000)

##Equivalance Classes for the other Calculate_Retirement_date function

##Bad Input
def test_birth_year_Input_check_bad_input():
     with pytest.raises(ValueError):
          calculate_retirement_age("hi")

def test_incorrect_birth_year_check_for_error():
     with pytest.raises(ValueError):
          calculate_retirement_date(10, 10, 10, 10)

def test_incorrect_birth_month():
     with pytest.raises(ValueError):
          calculate_retirement_date(1950, 111, 66, 4)

def test_incorrect_age_years_upper_bound():
     with pytest.raises(ValueError):
          calculate_retirement_date(1974, 11, 69, 4)

def test_incorrect_age_years_lower_bound():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, 11, 59, 4)

def test_incorrect_age_for_months_lower_than_one():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, 11, 66, -1)

def test_incorrect_age_for_months_higher_than_Dec():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, 11, 66, 13)

def test_strings_as_input_for_year():
     with pytest.raises(ValueError):
          calculate_retirement_date("hi", 11, 66, 4)

def test_strings_as_input_for_birth_month():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, "December", 66, 4)

def test_strings_as_input_for_age_years():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, 11, "tt", 4)

def test_strings_as_input_for_age_months():
     with pytest.raises(ValueError):
          calculate_retirement_date(1956, 11, 66, "y")

##Good Input



def test_retirement_date_and_if_year_is_correct_for_benefits():
     ##if calc was given 1943, and 8, based on "66,0" it should return 2009 as the year the individual
     ## will be eligible, and 8 as the month
     assert calculate_retirement_date(1943, 8, 66, 0) == (2009, 8)
##Lower Bound
def test_retirement_date_and_if_year_1937_is_correct_for_benefits():
     assert calculate_retirement_date(1937, 4, 65, 0) == (2002, 4)

##Upper Bound Good Input
def test_retirement_date_and_if_year_1959_is_correct_for_benefits():
     assert calculate_retirement_date(1959, 5, 66, 10) == (2026, 3)

##In Between Test
def test_retirement_date_and_if_year_1940_is_correct_for_benefits():
     assert calculate_retirement_date(1940, 3, 65, 6) == (2005, 9)






