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

    def connected_set(self, element=None):  # Виталий Александрович, подскадите, пожалуйста, как решить боллее эффективно этот метод, а то плохая ассимптотическая сложность
        connected_res = []
        connect = self.connection
        for i in range(len(connect)):
            if connect[i].isdisjoint(element) == False:
                connected_res.append(connect[i])
        if not connected_res:
            return set()
        for i in range(len(connected_res)):
            connected_res[i].remove(element)
        return connected_res


f = Friends([{"1", "2"}, {"3", "1"}])
result = f.add_set({"2", "1"})
print(result)
result2 = f.connected_set("1")
print(result2)


