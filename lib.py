def check_password(password):
    if len(password) < 8:
        return "Слабкий пароль: менше 8 символів"
    else:
        return "Пароль задовільний"

def account(login,reliability):
    message = "Акаунт: " + login + " -> " + reliability
    return message