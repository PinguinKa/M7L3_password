import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    password = generate_password()
    assert len(password) == 12, f"Ожидалась длина 12, но получено {len(password)}"

def test_password_difference():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password_1 = generate_password()
    password_2 = generate_password()
    assert password_1 != password_2, f"Оба пароля одинаковые: {password_1}"