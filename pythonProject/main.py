forbidden_words = ['admin', 'user', 'test']


def check_username(username):
    try:
        assert username[0].islower(), "Имя пользователя должно начинаться с маленькой буквы."

        for word in forbidden_words:
            assert word not in username, f"Имя пользователя не должно содержать слово: {word}"

        print("Имя пользователя корректно.")
    except AssertionError as e:
        print(f"Ошибка: {e}")


check_username("johnDoe")
check_username("JohnDoe")
check_username("adminUser")
check_username("tester")


class PrivateClass:
    def __init__(self, value):
        self.__private_value = value

    def __get_private_value(self):
        return self.__private_value

    def set_private_value(self, value):
        self.__private_value = value

    def display(self):
        print(f"Приватное значение: {self.__get_private_value()}")


class PublicClass:
    def __init__(self, value):
        self.public_value = value

    def display(self):
        print(f"Публичное значение: {self.public_value}")


private_instance = PrivateClass(10)
private_instance.display()
private_instance.set_private_value(20)
private_instance.display()

public_instance = PublicClass(30)
public_instance.display()
public_instance.public_value = 40
public_instance.display()

