# import all necessary packages and functions
import time
import pandas as pd

# Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    """Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    """
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').title()
    # handle raw input and complete function
    if city == 'Chicago':
        return chicago
    elif city == 'New York':
        return new_york_city
    elif city == 'Washington':
        return washington

    return ''


def get_time_period():
    """Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time filter for a city's bikeshare data.
    """
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
    # handle raw input and complete function
    if time_period in ['month', 'day', 'none']:
        return time_period
    else:
        return 'none'


def get_month():
    """Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (int) Month index for the time filter for a city's bikeshare data.
    """
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # handle raw input and complete function
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1
    return month


def get_day():
    """Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (int) Day for the time filter for a city's bikeshare data.
    """
    day = input('\nWhich day? Please type your response as an integer.\n')
    # handle raw input and complete function
    return day


def popular_month(city_file):
    """Find out the most popular month
    Question: What is the most popular month for start time?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The most popular month
    """
    # read csv file
    df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    return df['month'].mode()[0]


def popular_day(city_file):
    """Find out the most popular day
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The most popular day of week
    """
    # read csv file
    df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # find the most popular day
    popular_day_of_week = df['day_of_week'].mode()[0]
    return popular_day_of_week


def popular_hour(city_file):
    """Find out the most popular hour
    Question: What is the most popular hour of day for start time?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The most popular hour of day
    """
    # read csv file
    df = pd.read_csv(city_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    return df['hour'].mode()[0]


def trip_duration(city_file):
    """Find out the total trip duration and average trip duration
    Question: What is the total trip duration and average trip duration?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The total trip duration
        (str) The average trip duration
    """
    # read csv file
    df = pd.read_csv(city_file)

    # find the most popular hour
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    return total_trip_duration, avg_trip_duration


def popular_stations(city_file):
    """Find out the most popular start station and most popular end station
        Question: What is the most popular start station and most popular end station?
        Args:
            (str) city_file the csv filename of certain city
        Returns:
            (str) The most popular start station
            (str) The most popular end station
    """
    # read csv file
    df = pd.read_csv(city_file)

    # find the most popular hour
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    return popular_start_station, popular_end_station


def popular_trip(city_file):
    """Find out the most popular trip
    Question: What is the most popular trip?
    Args:
            (str) city_file the csv filename of certain city
        Returns:
            (str) The most popular trip
    """
    # read csv file
    df = pd.read_csv(city_file)

    # extract start station and end station to create new columns
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']

    # find the most popular hour
    return df['trip'].mode()[0]


def users(city_file):
    """Find out the user type count
    Question: What are the counts of each user type?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The user type count
    """
    # read csv file
    df = pd.read_csv(city_file)

    # get value counts for each user type
    user_types = df['User Type'].value_counts()
    return user_types


def gender(city_file):
    """Find out the gender count
    Question: What are the counts of gender?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The gender count
    """
    # read csv file
    df = pd.read_csv(city_file)

    # get value counts for each user type
    if 'Gender' not in df.columns:
        return None

    return df['Gender'].value_counts()


def birth_years(city_file):
    """Provide brith year insights
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        (str) city_file the csv filename of certain city
    Returns:
        (str) The earliest (i.e. oldest user) birth years
        (str) The most recent (i.e. youngest user) birth years
        (str) The most popular birth years
    """
    # read csv file
    df = pd.read_csv(city_file)

    if 'Birth Year' not in df.columns:
        return None

    # find the most popular hour
    earliest_birth_year = df['Birth Year'].max()
    most_recent_birth_year = df['Birth Year'].min()
    most_popular_birth_year = df['Birth Year'].mode()[0]
    return earliest_birth_year, most_recent_birth_year, most_popular_birth_year


def display_data(city_file):
    """Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        (str) city_file the csv filename of certain city.
    Returns:
        none.
    """
    df = pd.read_csv(city_file)

    display = 'yes'
    i = 0
    while display == 'yes':
        print(df[i:i + 5])
        i += 5
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')


def calculate_statistic(function, city, time_period=None):
    """Helper function to calculate and print statistic along with execution time.

    Args:
        function: The statistical function to call.
        city: The city for which statistics are being calculated.
        time_period: The time period filter for the statistic, if applicable.
    """
    start_time = time.time()
    if time_period:
        result = function(city, time_period)
    else:
        result = function(city)

    if isinstance(result, tuple):  # Handling functions returning multiple values
        for res in result:
            print(res)
    else:
        print(result)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")


def statistics():
    """Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    """
    city = get_city()
    time_period = get_time_period()

    print('Calculating the first statistic...')

    if time_period == 'none':
        calculate_statistic(popular_month, city)

    if time_period == 'none' or time_period == 'month':
        calculate_statistic(popular_day, city)

    calculate_statistic(popular_hour, city)
    calculate_statistic(popular_trip, city)
    calculate_statistic(popular_stations, city)
    calculate_statistic(users, city)
    calculate_statistic(gender, city)
    calculate_statistic(birth_years, city)
    display_data(city)

    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()
