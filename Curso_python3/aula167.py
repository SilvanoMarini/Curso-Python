import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2025))

print(locale.getlocale())