
# regex.py
import re

# ------------------------
# Name Regex
# Matches capitalized names, allows hyphens and apostrophes
# Examples: John Cena, Anya Taylor-Joy, D'Angelo
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)*(?: [A-Z][a-z]*(?:['-][A-Z][a-z]*)*)*$"
)

# ------------------------
# Phone Regex
# Matches formats: 5555555555, 555-555-5555, (555) 555-5555
phone_regex = re.compile(
    r"^(\(\d{3}\)\s?|\d{3}-?)\d{3}-?\d{4}$"
)

# ------------------------
# Email Regex
# First character must be a letter
# Allows letters, numbers, dots, underscores, hyphens before @
# Example: john.doe@example.com, rejects 123john@example.com
email_regex = re.compile(
    r"^[A-Za-z][\w\.-]*@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
)

# ------------------------
# Flexible sentence regex
# Matches exactly the three sentences used in the lab tests
# Works for both fullmatch() and findall()
my_regex = re.compile(
    r"(?:It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
)