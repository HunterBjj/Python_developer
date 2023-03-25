"""1. Друзья.
Дано: n - целое число.
Задание:
Создайте класс "Friends", который должен содержать данные о людях (их имена)
и о связях между ними. Имена представлены в виде текстовых строк,
чувствительных к регистру. Связи не имеют направлений, то есть,
если существует связь "sofia" с "nikola", это справедливо и в обратную сторону.
"""


class Friends:

    def __init__(self, connection):
        self.connection = connection

    def add_set(self, element=None):
        if not (element in self.connection):
            self.connection.append(element)
            return True
        return False

    def remove_set(self, element=None):
        if element in self.connection:
            self.connection.remove(element)
            return True
        return False

    def names_set(self, element=None):
        return False

    def connected_set(self, element=None):
        for i in range()
        return set()


f = Friends([{"1", "2"}, {"3", "1"}])
result = f.add({"2", "1"})
print(result)