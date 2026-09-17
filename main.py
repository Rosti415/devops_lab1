import lib # імпортуємо бібліотеку lib.py

my_login = "Rostyslav"
my_password = "12345678"

# перевіряємо надійність пароля та створення акаунта
status = lib.check_password(my_password)
result = lib.account(my_login, status)

print(result)