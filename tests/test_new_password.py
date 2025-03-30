import string
from password.new_password import generate_password




def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100) # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for length in range(1, 21): # Проверяем длины от 1 до 20
        password = generate_password(length)
        assert len(password) == length

def test_different_passwords():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2


# Дополнительный тест (проверка наличия цифр, букв и символов)
def test_password_composition():
    """Тест, проверяющий наличие хотя бы одной цифры, буквы в верхнем и нижнем регистре, и символа"""
    password = generate_password(12, include_symbols=True) # достаточно длинный пароль для проверки
    assert any(char.isdigit() for char in password), "Пароль не содержит цифр"
    assert any(char.islower() for char in password), "Пароль не содержит строчных букв"
    assert any(char.isupper() for char in password), "Пароль не содержит заглавных букв"
    assert any(char in string.punctuation for char in password), "Пароль не содержит символов"
