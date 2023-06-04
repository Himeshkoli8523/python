import re
email = input("Enter your email address:")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern,email):
    print('its a valid email')
else:
    print('its not a valid email')