import pytest

@pytest.fixture(scope="class")
def login():
    print("Пользователь авторизован")

    yield
    print("\nСессия завершена")
