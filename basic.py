username = input('What is your name?')
password = input('please provide your password')
password_length = len(password)
hidden_password = '*' *password_length
print(f'{username} your password {hidden_password} is  {password_length} letter long')