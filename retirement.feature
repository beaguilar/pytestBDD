@retirement-calculator
Feature: Retirement Age Calculator
 We want to make sure the calculator returns the correct age.

	Scenario: Checking Lower bound of calculator
		Given the lower bound of 1937
		When the year is given as 1937
		Then results should be given as (65,0)



	Scenario: Checking the upper bound of 2999
		Given the upper bound of 2999
		When the year is given as 2999
		Then results should be given as 67,0



	Scenario: Checking 1st range of calculator
		Given the range 1943-1955
		When the year is given the range 1943-1955
		Then results should be given as 66,0



	Scenario: Checking the upper range of 1960-2999

		Given the range 1960-2999
		When the upper range is given
		Then results should be given as 67,0



	Scenario: Checking bound of calculator
		Given the bound of 1938
		When the year is given as 1938
		Then results should be given as (65,2)



	Scenario: Checking bound of calculator
		Given the bound of 1939
		When the year is given as 1939
		Then results should be given as (65,4)



	Scenario: Checking bound of calculator
		Given the bound of 1940
		When the year is given as 1940
		Then results should be given as (65,6)



	Scenario: Checking bound of calculator
		Given the bound of 1941
		When the year is given as 1941
		Then results should be given as (65,8)




	Scenario: Checking bound of calculator
		Given the bound of 1942
		When the year is given as 1942
		Then results should be given as (65,10)



	Scenario: Checking bound of calculator
		Given the bound of 1955
		When the year is given as 1955
		Then results should be given as (66,2)



	Scenario: Checking bound of calculator
		Given the bound of 1956
		When the year is given as 1956
		Then results should be given as (66,4)



	Scenario: Checking bound of calculator
		Given the bound of 1957
		When the year is given as 1957
		Then results should be given as (66,6)



	Scenario: Checking bound of calculator
		Given the bound of 1958
		When the year is given as 1958
		Then results should be given as (66,8)



	Scenario: Checking bound of calculator
		Given the bound of 1959
		When the year is given as 1959
		Then results should be given as (66,10)



	Scenario: Checking incorrect integer input for calculate_retirement_age function
		Given the input as integer- 39
		When the incorrect input is entered
		Then it should raise a ValueError because 39 is an incorrect year format



	Scenario: Checking incorrect string input for calculate_retirement_age function
		Given the input as a String "pie"
		When an incorrect string input is entered
		Then it should raise a ValueError because a string is an incorrect year format.




	Scenario: Checking incorrect integer input for calculate_retirement_age
		Given the input as 10,10,10,10
		When an incorrect integer input is entered
		Then it should raise a ValueError because 10,10,10,10 is not a valid input.




	Scenario: Checking incorrect integer input for calculate_retirement_age in month section.
		Given the input as 1950, 111, 66, 4
		When an incorrect month integer value is entered
		Then it should raise a ValueError because 111 is not a valid month input.


	Scenario: Add user year of birth before 1900
    	Given the user was born before 1899
    	When year of birth is entered
		Then system returns invalid year range

  	Scenario: Add user year of birth after 2999
     	Given the user was born after 2999
     	When year of birth is entered
     	Then system returns invalid year range

	Scenario Outline: Add user year of birth to calculator
    	Given the user year of birth is "<year>"
    	When user enters birth month as "<month>"
    	Then the full retirement age is "<age>"and 0 months
    	And will be able to retire in October of 2027

    	Examples: Retirement Age
    	| year | month | age
		| 1960     | 1   | 67






