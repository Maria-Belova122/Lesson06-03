# ЗАДАНИЕ ПО ТЕМЕ "Доступ к свойствам родителя. Переопределение свойств"

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # владелец транспорта (может меняться)
        self.__model = __model  # модель транспорта (не может меняться)
        self.__color = __color  # цвет транспорта (не может меняться)
        self.__engine_power = __engine_power  # мощность двигателя транспорта (не может меняться) цветов

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        print(
            f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # количество пассажиров


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
