JuryTech/
├── src/
│   ├── password_generator.py   # renamed from main.py (clearer purpose)
│   └── sales_forecast.py       # renamed from pep1.py (clearer purpose)
├── data/
│   └── sales.csv               # move data files here
├── outputs/
│   └── forecast_plot.png       # auto-saved chart output
├── tests/
│   ├── test_password.py        # unit tests
│   └── test_forecast.py        # unit tests
├── requirements.txt            # dependencies
├── README.md                   # project documentation
└── .gitignore                  # ignore __pycache__, .csv outputs, etc.
import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
