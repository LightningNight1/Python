# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов
# должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def intake(self):
        self.weight = 25
        self.thickness = 5
        intake = self._length * self._width * self.weight * self.thickness / 1000
        print(f'{intake} tons')


road = Road(20, 5000)
road.intake()
