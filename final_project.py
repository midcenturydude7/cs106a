# data comes from Johns Hopkins University. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# you can find data beyond cumulative cases there!

"""
File: final_project.py
In its current form, this VERY BASIC program works with COVID-19 data from five countries and allows the user
to access data based on choosing which country he/she would like to see data about.
***
NEXT STEPS: (1) Provide access to all the files, likely using the OS module; (2) Include a date with each day;
(3) Data manipulation: Work with Numpy and Pandas to perform further/more detailed data manipulation such as
cross country comparisons based on certain data points related to 'confirmed cases' or 'country with the day
of the most confirmed cases', etc.; (4) Data visualization: Work with Matplotlib to plot the data and
hopefully create some useful/interesting charts/graphs for the purposes of storytelling (maybe); and
(5) Further decompose the program - likely related to #1 above - to simplify/refactor the code to make it more
efficient and easier to read.
***
LAST BUT NOT LEAST: THANK YOU CS106A!!! What an awesome, kick-ass, amazing and super-fun experience this has been.
Really can't say thank you enough! Everyone that contributed their time, energy and effort to this has my infinite
gratitude - and that is an understatement.
"""

# Constants for each country's file that contains all confirmed cases
# beginning with Jan-22 to early May
DATA_DIR = 'confirmed/'
DATA_DIR_BELARUS = 'confirmed/belarus.txt'
DATA_DIR_BRAZIL = 'confirmed/brazil.txt'
DATA_DIR_IRAN = 'confirmed/iran.txt'
DATA_DIR_ITALY = 'confirmed/italy.txt'
DATA_DIR_RUSSIA = 'confirmed/russia.txt'


def main():

    # Intro output to console
    print("Welcome! You have access to COVID-19 data from Jan-22 to May-09 for the following five countries:")
    print("Belarus, Brazil, Iran, Italy, and Russia")
    print("Check back soon, as more countries will be made available for review!")
    print('')

    # List for the five available countries / file access
    available_countries = ['Belarus', 'belarus', 'Brazil', 'brazil', 'Iran',
                           'iran', 'Italy', 'italy', 'Russia', 'russia']

    # Loop that asks user to enter country name to access COVID-19 data
    while True:
        country_name = input("Choose a country: ")
        print('')

        # Belarus
        if country_name == available_countries[0] or country_name == available_countries[1]:
            load_belarus()

        # Brazil
        elif country_name == available_countries[2] or country_name == available_countries[3]:
            load_brazil()

        # Iran
        elif country_name == available_countries[4] or country_name == available_countries[5]:
            load_iran()

        # Italy
        elif country_name == available_countries[6] or country_name == available_countries[7]:
            load_italy()

        # Russia
        elif country_name == available_countries[8] or country_name == available_countries[9]:
            load_russia()

        # Conditional for incorrect input
        else:
            print("You do not have access to that file yet! It will be available soon.")
            print("Please try again.")
            print("REMINDER: The following countries are currently available for review:")
            print("Belarus, Brazil, Iran, Italy, and Russia")
            print('')


def load_belarus():

    # File access and having fun with the data :)
    filename = 'belarus.txt'
    with open(DATA_DIR_BELARUS, 'r') as f:                      # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        for i in range(0, len(country_data_updated)):           # Find the total number of cases for the country
            country_sum += int(country_data_updated[i])
        max_country = max(country_data_updated)                 # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list
        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Output to console
        print("***FILE INFORMATION FOR BELARUS.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_BELARUS)
        print(filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR BELARUS***")
        print("The total number of days with confirmed COVID-19 cases is: " + str(country_confirmed_cases))
        print("The overall total number of COVID-19 cases from Jan-22 to May-09 is: " + str(country_sum))
        print("The day with the most number of confirmed cases registered a total of: " + str(max_country) + " cases")
        print('')


def load_brazil():

    # File access and having fun with the data :)
    filename = 'brazil.txt'
    with open(DATA_DIR_BRAZIL, 'r') as f:                       # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        for i in range(0, len(country_data_updated)):           # Find the total number of cases for the country
            country_sum += int(country_data_updated[i])
        max_country = max(country_data_updated)                 # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list
        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Output to console
        print("***FILE INFORMATION FOR BRAZIL.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_BRAZIL)
        print(filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR BRAZIL***")
        print("The total number of days with confirmed COVID-19 cases is: " + str(country_confirmed_cases))
        print("The overall total number of COVID-19 cases from Jan-22 to May-09 is: " + str(country_sum))
        print("The day with the most number of confirmed cases registered a total of: " + str(max_country) + " cases")
        print('')


def load_iran():

    # File access and having fun with the data :)
    filename = "iran.txt"
    with open(DATA_DIR_IRAN, 'r') as f:                         # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        for i in range(0, len(country_data_updated)):           # Find the total number of cases for the country
            country_sum += int(country_data_updated[i])
        max_country = max(country_data_updated)                 # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list
        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Output to console
        print("***FILE INFORMATION FOR IRAN.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_IRAN)
        print(filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR IRAN***")
        print("The total number of days with confirmed COVID-19 cases is: " + str(country_confirmed_cases))
        print("The overall total number of COVID-19 cases from Jan-22 to May-09 is: " + str(country_sum))
        print("The day with the most number of confirmed cases registered a total of: " + str(max_country) + " cases")
        print('')


def load_italy():

    # File access and having fun with the data :)
    filename = 'italy.txt'
    with open(DATA_DIR_ITALY, 'r') as f:                        # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        for i in range(0, len(country_data_updated)):           # Find the total number of cases for the country
            country_sum += int(country_data_updated[i])
        max_country = max(country_data_updated)                 # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list
        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Output to console
        print("***FILE INFORMATION FOR ITALY.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_ITALY)
        print(filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR ITALY***")
        print("The total number of days with confirmed COVID-19 cases is: " + str(country_confirmed_cases))
        print("The overall total number of COVID-19 cases from Jan-22 to May-09 is: " + str(country_sum))
        print("The day with the most number of confirmed cases registered a total of: " + str(max_country) + " cases")
        print('')


def load_russia():

    # File access and having fun with the data :)
    filename = 'russia.txt'
    with open(DATA_DIR_RUSSIA, 'r') as f:                       # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        for i in range(0, len(country_data_updated)):           # Find the total number of cases for the country
            country_sum += int(country_data_updated[i])
        max_country = max(country_data_updated)                 # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list
        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Output to console
        print("***FILE INFORMATION FOR RUSSIA.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_RUSSIA)
        print(filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR RUSSIA***")
        print("The total number of days with confirmed COVID-19 cases is: " + str(country_confirmed_cases))
        print("The overall total number of COVID-19 cases from Jan-22 to May-09 is: " + str(country_sum))
        print("The day with the most number of confirmed cases registered a total of: " + str(max_country) + " cases")
        print('')


if __name__ == '__main__':
    main()