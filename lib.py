# функція для перевірки надійності пароля
def check_password(password):
    if len(password) < 8:
        return "Слабкий пароль: менше 8 символів"
    else:
        return "Пароль задовільний"
# функція для створення акаунта
def account(login,reliability):
    message = "Акаунт: " + login + " -> " + reliability
    return message