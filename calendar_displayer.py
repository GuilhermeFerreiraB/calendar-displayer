import calendar
while True:
    try:
        year = int(input('Please, write a year: '))
        month = int(input('Please, write a month: '))
        print('\n', calendar.month(year, month))
        print("Here's your calendar.")
    except ValueError:
        print('Write positive numbers only, please.')
    except IndexError:
        print('Write a month number between 1-12, please.')
    else:
        break
