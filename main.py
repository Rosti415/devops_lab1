import lib

my_login = "Rostyslav"
my_password = "12345678"

status = lib.check_password(my_password)
result = lib.account(my_login, status)

print(result)