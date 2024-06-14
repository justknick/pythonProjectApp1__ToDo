from feet_inches_parcers import parse
from feet_inches_converters import convert
from feet_inches_kid_checker import kid_checker
from feet_inches_notification import notification

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])
message = notification(parsed, result)
