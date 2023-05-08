# 2023 © Campari Country Club licensed under GNU GPL v3

import random
import csv
import requests

def load_names(filename):
    url = f'https://raw.githubusercontent.com/camparicountryclub/girls/main/{filename}'
    response = requests.get(url)
    response.raise_for_status()
    names = response.text.split('\n')
    return [name.strip() for name in names]

def generate_name(first_names, last_names):
    return random.choice(first_names) + ' ' + random.choice(last_names)

def generate_names(first_names, last_names, count):
    unique_names = set()
    while len(unique_names) < count:
        name = generate_name(first_names, last_names)
        unique_names.add(name)
    return unique_names

def generate_email(name, domain):
    first_name, last_name = name.split(' ')
    return first_name[:3].lower() + last_name.lower() + '@' + domain

def main():
    first_names = load_names('firstnames.txt')
    last_names = load_names('lastnames.txt')

    count = int(input('How many names to create? '))
    unique_names = generate_names(first_names, last_names, count)

    domain = input('Enter the email domain: ')
    output_filename = f'{domain}.csv'

    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['DisplayName', 'EmailAddress']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for name in unique_names:
            email = generate_email(name, domain)
            writer.writerow({'DisplayName': name, 'EmailAddress': email})

    print(f'{count} unique names and email addresses have been generated and saved to {output_filename}.')

if __name__ == '__main__':
    main()

