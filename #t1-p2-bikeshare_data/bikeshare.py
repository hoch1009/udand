#!/usr/bin/env python3

import time
import csv
import datetime as dt


# Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

# global variables
month = 0
day = 0


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:       none.
    Returns:    (str) Filename for a city's bikeshare data.
    '''
    city = str(input('\nHello! Let\'s explore some US bikeshare data!\n''Would you like to see data for Chicago, New York, or Washington?\n '))
    if city.replace(" ", "").lower() == "newyork":
        city = new_york_city
    elif city.replace(" ", "").lower() == "chicago":
        city = chicago
    elif city.replace(" ", "").lower() == "washington":
        city = washington
    else:
        print('Sorry, please try again.')
        return get_city()
    return city


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:       none.
    Returns:    (str) time_period for filtering
    '''
    time_period = input(
        '\nWould you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n ')
    if time_period.lower() == 'month':
        time_period = 'month'
    elif time_period.lower() == 'day':
        time_period == 'day'
    elif time_period.lower() == 'none':
        time_period = 'none'
    else:
        print('Sorry, please try again.')
        return get_time_period()
    return str(time_period)


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:       none.
    Returns:    (str) month
    '''
    global month
    available_months = {"january": 1, "february": 2,
                        "march": 3, "april": 4, "may": 5, "june": 6}
    month = input(
        '\nWhich month? January, February, March, April, May, or June?\n ')
    if month.lower() in available_months.keys():
        month = available_months[month.lower()]
    else:
        get_month()
    return month


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:       month.
    Returns:    (int) day
    '''
    global day
    days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30}
    day = input('\nWhich day? Please type your response as an integer.\n ')
    if int(day) == 0 or int(day) > days_per_month[month]:
        get_day(month)
    else:
        day = int(day)
    return day


def popular_month(city_file, time_period):
    '''Determines the most popular month.

    Args:       city_file, time_period
    Returns:    (str) most popular month
    '''
    starts_per_month = {"January": 0, "February": 0,
                        "March": 0, "April": 0, "May": 0, "June": 0}
    for row in city_file:
        if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 1:
            starts_per_month['January'] += 1
        elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 2:
            starts_per_month['February'] += 1
        elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 3:
            starts_per_month['March'] += 1
        elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 4:
            starts_per_month['April'] += 1
        elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 5:
            starts_per_month['May'] += 1
        elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == 6:
            starts_per_month['June'] += 1
        else:
            print('An error occurred.')

    print(' The most popular month for start time is: ' + str(max(starts_per_month, key=starts_per_month.get)) + " with " + str(starts_per_month[max(starts_per_month, key=starts_per_month.get)]) + ' starts.')


def popular_day(city_file, time_period):
    '''Determines the most popular day of the week when usage starts.

    Args:       city_file, time_period
    Returns:    (str) most popular day of week
    '''
    starts_per_day = {"Monday": 0, "Tuesday": 0, "Wednesday": 0,
                      "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    if time_period == 'none':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 0:
                starts_per_day['Monday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 1:
                starts_per_day['Tuesday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 2:
                starts_per_day['Wednesday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 3:
                starts_per_day['Thursday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 4:
                starts_per_day['Friday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 5:
                starts_per_day['Saturday'] += 1
            elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 6:
                starts_per_day['Sunday'] += 1
            else:
                print('An error occurred.')
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 0:
                    starts_per_day['Monday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 1:
                    starts_per_day['Tuesday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 2:
                    starts_per_day['Wednesday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 3:
                    starts_per_day['Thursday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 4:
                    starts_per_day['Friday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 5:
                    starts_per_day['Saturday'] += 1
                elif dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday() == 6:
                    starts_per_day['Sunday'] += 1
                else:
                    print('An error occurred.')

    print(' The most popular day for start time is: ' + str(max(starts_per_day, key=starts_per_day.get)
                                                            ) + " with " + str(starts_per_day[max(starts_per_day, key=starts_per_day.get)]) + ' starts.')


def popular_hour(city_file, time_period):
    '''Determines the most popular hour of the day when usage starts.

    Args:       city_file, time_period
    Returns:    (str) most popular hour
    '''
    popular_hours = dict()
    if time_period == 'none':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in popular_hours:
                popular_hours[dt.datetime.strptime(
                    row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
            else:
                popular_hours[dt.datetime.strptime(
                    row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in popular_hours:
                    popular_hours[dt.datetime.strptime(
                        row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
                else:
                    popular_hours[dt.datetime.strptime(
                        row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in popular_hours:
                    popular_hours[dt.datetime.strptime(
                        row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
                else:
                    popular_hours[dt.datetime.strptime(
                        row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    print(' The most popular hour for start time is: ' + str(max(popular_hours, key=popular_hours.get)) + " with " + str(popular_hours[max(popular_hours, key=popular_hours.get)]) + ' starts.')


def trip_duration(city_file, time_period):
    '''Determines the total trip duration and the average trip duration.

    Args:       city_file, time_period
    Returns:    (str) total trip duration, average trip duration in seconds
    '''
    total_trip_duration = 0
    number_of_trips = 0
    if time_period == 'none':
        for row in city_file:
            total_trip_duration += float(row['Trip Duration'])
            number_of_trips += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                total_trip_duration += float(row['Trip Duration'])
                number_of_trips += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                total_trip_duration += float(row['Trip Duration'])
                number_of_trips += 1
    else:
        print('An error occured')
    print(' The total trip duration is: ' + str(total_trip_duration) +
          ' seconds (= ' + str(total_trip_duration / 60) + ' minutes)')
    print(' The average trip duration is: ' + str(total_trip_duration / number_of_trips) +
          ' seconds (= ' + str((total_trip_duration / number_of_trips) / 60) + ' minutes)')


def popular_stations(city_file, time_period):
    '''Determines the most popular start and end station

    Args:       city_file, time_period
    Returns:    (str) most popular start station and end station
    '''
    pop_start_stations = dict()
    pop_end_stations = dict()
    if time_period == 'none':
        for row in city_file:
            if row['Start Station'] not in pop_start_stations:
                pop_start_stations[row['Start Station']] = 1
            else:
                pop_start_stations[row['Start Station']] += 1
            if row['End Station'] not in pop_end_stations:
                pop_end_stations[row['End Station']] = 1
            else:
                pop_end_stations[row['End Station']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Start Station'] not in pop_start_stations:
                    pop_start_stations[row['Start Station']] = 1
                else:
                    pop_start_stations[row['Start Station']] += 1
                if row['End Station'] not in pop_end_stations:
                    pop_end_stations[row['End Station']] = 1
                else:
                    pop_end_stations[row['End Station']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                if row['Start Station'] not in pop_start_stations:
                    pop_start_stations[row['Start Station']] = 1
                else:
                    pop_start_stations[row['Start Station']] += 1
                if row['End Station'] not in pop_end_stations:
                    pop_end_stations[row['End Station']] = 1
                else:
                    pop_end_stations[row['End Station']] += 1

    print(' Popular start station:\t' + str(max(pop_start_stations, key=pop_start_stations.get)) +
          " with " + str(pop_start_stations[max(pop_start_stations, key=pop_start_stations.get)]) + ' starts.')
    print(' Popular end station:\t' + str(max(pop_end_stations, key=pop_end_stations.get)) + " with " +
          str(pop_end_stations[max(pop_end_stations, key=pop_end_stations.get)]) + ' drop offs.')


def popular_trip(city_file, time_period):
    '''Determines the most popular trip from a to b

    Args:       city_file, time_period
    Returns:    (str) trip from a to b with number of trips
    '''
    pop_trips = dict()
    if time_period == 'none':
        for row in city_file:
            trip = str(row['Start Station']) + \
                ' to: ' + str(row['End Station'])
            if trip not in pop_trips:
                pop_trips[trip] = 1
            else:
                pop_trips[trip] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                trip = str(row['Start Station']) + \
                    ' to: ' + str(row['End Station'])
                if trip not in pop_trips:
                    pop_trips[trip] = 1
                else:
                    pop_trips[trip] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                trip = str(row['Start Station']) + \
                    ' to: ' + str(row['End Station'])
                if trip not in pop_trips:
                    pop_trips[trip] = 1
                else:
                    pop_trips[trip] += 1
    print(' Popular trip from:\t' + str(max(pop_trips, key=pop_trips.get)) +
          " with " + str(pop_trips[max(pop_trips, key=pop_trips.get)]) + " trips.")


def users(city_file, time_period):
    '''Determines the user type distribution.

    Args:       city_file, time_period
    Returns:    (str) number of users for each user type
    '''
    user_types = dict()
    if time_period == 'none':
        for row in city_file:
            if row['User Type'] not in user_types:
                user_types[row['User Type']] = 1
            else:
                user_types[row['User Type']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['User Type'] not in user_types:
                    user_types[row['User Type']] = 1
                else:
                    user_types[row['User Type']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                if row['User Type'] not in user_types:
                    user_types[row['User Type']] = 1
                else:
                    user_types[row['User Type']] += 1
    for k, v in user_types.items():
        print(' ' + str(k) + ': ' + str(v))


def gender(city_file, time_period):
    '''Determines the user type distribution.

    Args:       city_file, time_period
    Returns:    (str) number of users for each gender
    '''
    genders = dict()
    if time_period == 'none':
        for row in city_file:
            if row['Gender'] not in genders:
                genders[row['Gender']] = 1
            else:
                genders[row['Gender']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Gender'] not in genders:
                    genders[row['Gender']] = 1
                else:
                    genders[row['Gender']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                if row['Gender'] not in genders:
                    genders[row['Gender']] = 1
                else:
                    genders[row['Gender']] += 1
    for k, v in genders.items():
        if k == '':
            print(' N/A: ' + str(v))
        else:
            print(' ' + str(k) + ': ' + str(v))


def birth_years(city_file, time_period):
    '''Determines the oldest, most recent and most popular birth year

    Args:       city_file, time_period
    Returns:    (str) earliest birth year, most recent birth year and most popular birth year
    '''
    birth_years = dict()
    if time_period == 'none':
        for row in city_file:
            if row['Birth Year'] == '':
                pass
            else:
                birthyear = row['Birth Year'].replace('.0', "")
                if int(birthyear) not in birth_years:
                    birth_years[int(birthyear)] = 1
                else:
                    birth_years[int(birthyear)] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Birth Year'] == '':
                    pass
                else:
                    birthyear = row['Birth Year'].replace('.0', "")
                    if int(birthyear) not in birth_years:
                        birth_years[int(birthyear)] = 1
                    else:
                        birth_years[int(birthyear)] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                if row['Birth Year'] == '':
                    pass
                else:
                    birthyear = row['Birth Year'].replace('.0', "")
                    if int(birthyear) not in birth_years:
                        birth_years[int(birthyear)] = 1
                    else:
                        birth_years[int(birthyear)] += 1

    print(' Earliest birth year:\t\t ' + str(sorted(birth_years)[0]))
    print(' Most recent birth year:\t ' + str(sorted(birth_years)[-1]))
    print(' Most popular birth year:\t ' + str(max(birth_years, key=birth_years.get)))


def display_data(city_file, time_period):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:       none.
    Returns:    five lines from the citys csv
    '''

    display = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\'.\n ')

    if display == 'yes':
        # filtering the city file to provide only relevant data

        print('Please wait while we prepare the data ...')
        city_file_filtered = list()
        if time_period == 'none':
            city_file_filtered = city_file
        elif time_period == 'month':
            for row in city_file:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                    city_file_filtered.append(row)
        elif time_period == 'day':
            for row in city_file:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month and dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").day == day:
                    city_file_filtered.append(row)
        start = 0
        end = 5
        while display == 'yes':
            for x in range(start, end):
                print(city_file_filtered[x])
                start += 5
                end += 5
            display = input('\nMore? (yes or no)\n')
    elif display == 'no':
        pass
    else:
        print('Sorry, please try again.\n')
        display_data()


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:       none.
    Returns:    none.
    '''
    # Reseting the global variables in case the user has restarted the statistics
    global month
    month = 0
    global day
    day = 0

    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Turn the csv for the city into a list of dictionaries (city_file)
    with open(city) as csv_file:
        city_file = [{k: v for k, v in row.items()}
                     for row in csv.DictReader(csv_file, skipinitialspace=True)]

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    # If a filter is applied ask user for further input
    if time_period == 'month':
        month = get_month()
    elif time_period == 'day':
        get_month()
        get_day(month)
    else:
        time_period = 'none'

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        popular_month(city_file, time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start
    # time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        popular_day(city_file, time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    popular_hour(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    # What is the most popular start station and most popular end station?
    popular_stations(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))

    print("Calculating the next statistic...")
    start_time = time.time()
    # What is the most popular trip?
    popular_trip(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    # What are the counts of each user type?
    print("Calculating the next statistic...")
    start_time = time.time()
    users(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))

    if city == chicago or city == new_york_city:
        # What are the counts of gender?
        print("Calculating the next statistic...")
        start_time = time.time()
        gender(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))

        # What are the earliest, most recent, and most popular birth years?
        print("Calculating the next statistic...")
        start_time = time.time()
        birth_years(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))
    else:
        pass

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file, time_period)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n ')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()
