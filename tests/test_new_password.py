import string
from password.new_password import generate_password




def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100) # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной """

    for length in range(1, 21): # Проверяем длины от 1 до 20
        password = generate_password(length)
        assert len(password) == length

def test_different_passwords():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2
    length = 12
    password = generate_password(length)
    assert len(password) == length

def test_password_non_repeating():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

