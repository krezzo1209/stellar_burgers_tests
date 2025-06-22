import random

def generate_email(prefix='user'):
    """Генерирует уникальный email."""
    number = random.randint(1000, 9999)
    domains = ['yandex.ru', 'gmail.com', 'mail.ru']
    domain = random.choice(domains)
    return f"{prefix}_{number}@{domain}"

def generate_password(length=6):
    """Генерирует пароль из случайных букв и цифр."""
    import string
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))