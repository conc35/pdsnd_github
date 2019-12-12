import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
     city = input(" Choose city from (chicago, new york city,& washington)? ")
     while city not in ['chicago', 'new york city', 'washington']:
           city =input("Incorrect!  Please choose again from (chicago, new york city, washington)? ")
    # TO DO: get user input for month (all, january, february, ... , june)
     month = input("Please choose month from january to june or choose all ? ")
     while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
           month =input("Incorrect! Please choose month from january to june or choose all ? ")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
     day = input (" Please enter which day of the week ?")
     while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']:
           day =input("Incorrect! Please enter which day of the week? ")
    except Exception as e:
        print (e)
    #yesprint('good'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
       
     
        # filter by month to create the new dataframe
        df = df[df['month'] == month]  

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('the Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the Most Common day of week:', common_day)
    
    # TO DO: display the most common start hour
    
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print('the Most Common start hour:', common_hour)
    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #Start_stations = df['Start Station'].value_counts()
    #print(Start_stations)
    common_Start_station = df['Start Station'].mode()[0]
    print('the Most Common start station:', common_Start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the Most Common end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route_trip']=df['Start Station']+" - to - "+df['End Station']
    freq_route_trip = df['route_trip'].mode()[0]
    print('the most frequent combination of start station and end station trip:', freq_route_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum ()
    print('Total Travel Time in second:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean ()
    print('Mean Travel Time :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types =df['User Type'] .value_counts()
    print('Counts of user types :', counts_of_user_types)
    
    try:
    # TO DO: Display counts of gender
    #df['Gender'] !=NaN:
     counts_of_gender = df['Gender'] .value_counts()
     print('counts of gender  :', counts_of_gender)
    except Exception as e:
        print ('Gender : No date aviliable for ',city)
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
     earliest_YOB =  df['Birth Year'].min()
     print('earliest year of birth :', earliest_YOB)
    
     most_recent_YOB =  df['Birth Year'].max()
     print('most recent year of birth :', most_recent_YOB)
    
     most_common_YOB = df['Birth Year'].mode()[0] 
     print('most common year of birth :', most_common_YOB)
    except Exception as e:
        print ('Birth Year : No date aviliable for ', city)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dispaly_data(df):
    display=input('Whould you like display an overview of the data (yes , No (or any other key)?')
    head_value = 0
    while display == 'yes':
            head_value += 5
            print(df.head(head_value))
            display=input('Whould you like display more data (yes , No (or any other key)?')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dispaly_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
