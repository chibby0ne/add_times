#!/usr/bin/env python
# encoding: utf-8

"""
Filename: add_times.py
Author: Antonio Gutierrez
Email: chibby0ne@gmail.com
Github: https://github.com/chibby0ne
Created: 26/02/2015
Description: Script that computes total time from times given as command line
arguments
"""


import sys

def add_sum(times):
    """add_sum: adds the time values given as command line arguments
    and returns a result given in the same time format

    :in: argv (list)
    :returns: string "hours:minutes:seconds"

    """

    sum_hours = 0
    sum_minutes = 0
    sum_seconds = 0
    for time in times:
        if time.find(':') == -1:
            continue
        hours, minutes, seconds = parse_time(time)
        if hours != '':
            sum_hours += int(hours)
        sum_minutes += int(minutes)
        sum_seconds += int(seconds)

    extra_hours, sum_minutes, sum_seconds = fix_numbers(sum_minutes,
            sum_seconds)
    sum_hours += extra_hours

    return str(sum_hours) + ":" + str(sum_minutes) + ":" + str(sum_seconds)

def fix_numbers(minutes, seconds):
    """ Fixes the number of minutes and seconds so that 0 <= minutes < 60
    and 0 <= seconds < 60

    :minutes: integer
    :seconds: integer
    :returns: integers: hours, minutes, seconds
    """

    # fix seconds and calculate extra minutes
    corrent_seconds = seconds % 60
    extra_minutes = seconds / 60

    # add extra minutes to minutes
    minutes += extra_minutes

    # fix minutes and calculate extra hours
    correct_min = minutes % 60
    extra_hours = minutes / 60

    return extra_hours, correct_min, corrent_seconds


def parse_time(time):
    """ Separates times in hours, minutes and seconds so that they can
    then be summmed with other times correspondidly

    :time: string formatted in "hours:minutes:seconds"
    :returns: strings "hours", "minutes", "seconds"

    """
    seconds = ''
    minutes = ''
    hours = ''
    first = time.find(':')
    second = time.find(':', first + 1)
    if second != -1:
        seconds = time[second + 1:]
        minutes = time[first + 1: second]
        hours = time[:first]
    else:
        seconds = time[first + 1: ]
        minutes = time[:first]
    return hours, minutes, seconds


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print add_sum(sys.stdin)
    else:
        print add_sum(sys.argv[1:])

