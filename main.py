def start(bot_name, birth_year, bot_version):
    print('Hello, man! My name is', bot_name + '.'
          '\nI was created by #nva2810 in', birth_year + '.'
          '\nMy version is', bot_version, 'and will be updated.')


def user_name():
    print('\nPlease enter your name:')
    name = input()
    print('Nice to meet you,', name + '!')


def date_of_birth():
    print('\nFor starters, I can guess your date of birth!'
          '\nDid you have a birthday this year?'
          '\n\033[93mExample: "yes" or "no"\033[0m'
          '\n\033[91mEnter this here:\033[0m')
    birthday_this_year = input()

    print("Okay. It's time to get a calculator!"
          '\n\nMultiply your age by 2 (yourself).'
          '\nAdd 5 and multiply the result by 50.'
          '\nNow you need to subtract 365.'
          '\n\033[94mHmm, too easily...\033[0m'
          '\nPick any number up to 100 and add it to the result.'
          '\n---------------------------------------------------'
          '\n\033[91mNow enter what you received:\033[0m')
    age_and_number = int(input()) + 115

    print("I'll remember it, don't you mind?"
          '\nGo on!')
    print('\nNow multiply your birthday by 2 (yourself).'
          '\nAdd 5 and multiply the result by 50.'
          '\nAdd the number of the month in which you were born.'
          '\n\033[93mExample: October = 10\033[0m'
          '\n---------------------------------------------------'
          '\n\033[91mEnter the result here:\033[0m')
    day_and_month = int(input()) - 250

    number = age_and_number % 100
    age = age_and_number // 100

    def user_day():
        day = day_and_month // 100
        if day == 1 or day == 21 or day == 31:
            day = str(day) + str('st')
        else:
            if day == 2 or day == 22:
                day = str(day) + str('nd')
            else:
                if day == 3:
                    day = str(day) + str('rd')
                else:
                    day = str(day) + str('th')
        return str(day)

    def year_of_birth():
        import datetime
        now = datetime.datetime.now()
        if birthday_this_year == 'no':
            year = now.year
            year -= age + 1
        else:
            year = now.year
            year -= age
        return year

    def months_of_year():
        month = day_and_month % 100
        if month == 1:
            month = 'January'
        if month == 2:
            month = 'February'
        if month == 3:
            month = 'March'
        if month == 4:
            month = 'April'
        if month == 5:
            month = 'May'
        if month == 6:
            month = 'June'
        if month == 7:
            month = 'July'
        if month == 8:
            month = 'August'
        if month == 9:
            month = 'September'
        if month == 10:
            month = 'October'
        if month == 11:
            month = 'November'
        if month == 12:
            month = 'December'
        return month

    print('\nWell, now I know more about you!'
          '\n\033[94mYour number is\033[0m', str(number) + '\033[94m!\033[0m'
          '\n\033[94mYou were born on\033[0m', months_of_year(), user_day()
          + '\033[94m,\033[0m', str(year_of_birth()) + '\033[94m!\033[0m'
          '\n\033[94mYou are\033[0m', age, '\033[94myears old!\033[0m'
          '\n\033[93mIs that right? Excellent!\033[0m')


def user_count():
    print('\nNow I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(str(curr) + '!')
        curr += 1


def user_number():
    print('\nI want to guess your number again!'
          '\nPlease pick a number from 1 to 60.'
          '\nAre you ready?'
          '\nNow look at these blocks.')
    print('\n 1. 4 13 22 31 44 53', '         2.  2 11 22 31 42 51'
          '\n    5 14 23 36 45 54', '             3 14 23 34 43 54'
          '\n    6 15 28 37 46 55', '             6 15 26 35 46 55'
          '\n    7 20 29 38 47 60', '             7 18 27 38 47 58'
          '\n   12 21 30 39 52', '               10 19 30 39 50 59')
    print('\n3.  1 11 21 31 41 51', '         4.  8 13 26 31 44 57'
          '\n    3 13 23 33 43 53', '             9 14 27 40 45 58'
          '\n    5 15 25 35 45 55', '            10 15 28 41 46 59'
          '\n    7 17 27 37 47 57', '            11 24 29 42 47 60'
          '\n    9 19 29 39 49 59', '            12 25 30 43 56')
    print('\n5. 32 37 42 47 52 57', '         6. 16 21 26 31 52 57'
          '\n   33 38 43 48 53 58', '            17 22 27 48 53 58'
          '\n   34 39 44 49 54 59', '            18 23 28 49 54 59'
          '\n   35 40 45 50 55 60', '            19 24 29 50 55 60'
          '\n   36 41 46 51 56', '               20 25 30 51 56')
    print('\nWrite the numbers of the blocks together, '
          'where your number is located:'
          "\n\033[93mExample: 146 (if it's number 28)\033[0m")
    blocks = int(input())

    def first_block():
        block_1 = blocks % 100000 // 10000
        if block_1 == 2:
            block_1 = 2
        if block_1 == 4:
            block_1 = 8
        if block_1 == 5:
            block_1 = 32
        if block_1 == 6:
            block_1 = 16
        if block_1 == 1:
            block_1 = 4
        if block_1 == 3:
            block_1 = 1
        return block_1

    def second_block():
        block_2 = blocks % 10000 // 1000
        if block_2 == 2:
            block_2 = 2
        if block_2 == 4:
            block_2 = 8
        if block_2 == 5:
            block_2 = 32
        if block_2 == 6:
            block_2 = 16
        if block_2 == 1:
            block_2 = 4
        if block_2 == 3:
            block_2 = 1
        return block_2

    def third_block():
        block_3 = blocks % 1000 // 100
        if block_3 == 2:
            block_3 = 2
        if block_3 == 4:
            block_3 = 8
        if block_3 == 5:
            block_3 = 32
        if block_3 == 6:
            block_3 = 16
        if block_3 == 1:
            block_3 = 4
        if block_3 == 3:
            block_3 = 1
        return block_3

    def fourth_block():
        block_4 = blocks % 100 // 10
        if block_4 == 2:
            block_4 = 2
        if block_4 == 4:
            block_4 = 8
        if block_4 == 5:
            block_4 = 32
        if block_4 == 6:
            block_4 = 16
        if block_4 == 1:
            block_4 = 4
        if block_4 == 3:
            block_4 = 1
        return block_4

    def fifth_block():
        block_5 = blocks % 10
        if block_5 == 2:
            block_5 = 2
        if block_5 == 4:
            block_5 = 8
        if block_5 == 5:
            block_5 = 32
        if block_5 == 6:
            block_5 = 16
        if block_5 == 1:
            block_5 = 4
        if block_5 == 3:
            block_5 = 1
        return block_5

    sum_blocks = int(first_block()) + int(second_block()) \
        + int(third_block()) + int(fourth_block()) \
        + int(fifth_block())
    print(str('Your number is'), str(sum_blocks) + ', right?')


def end():
    print("\nThat's it! My congratulations, have a nice day!")
    print('\n\033[91mBot John 1.0.1 by #nva2810\033[0m')


start('John', '2020', '1.0.1')
user_name()
date_of_birth()
user_count()
user_number()
end()
