email = input('Enter your email address:')
username = email[:email.index('@')]
domain_name = email[email.index('@') + 1:]
print(f'Username is {username} and domain name is {domain_name}')