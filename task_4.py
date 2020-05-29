# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police= is_police
    def go(self):
        return print("Машина поехала")
    def stop(self):
        return print("Машина остановилась")
    def turn(self,direction):                           #решил не оставлять пользователю выбор, а то выберет всякое
        if direction == 1:
            return  print(f"Машина повернула вправо")
        elif direction == 2:
            return print(f"Машина повернула влево")
        else:
            return print(f"Направление указано не верно {direction}")
    def show_speed(self):
        return self.speed

class Polisecar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

class Sportcar(Car):
    pass
class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превыcила скорость!!")
class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превыcила скорость!!")

lada = Towncar(100,"Зеленая", "Лада", False)
bmw = Workcar(200,"Белая", "БМВ", False)
nissan = Polisecar(200, "Красная", "Ниссан")
audi = Sportcar(200,"Черная", "Ауди", False)
lada.go()
lada.turn(1)
lada.turn(2)
lada.show_speed()
print("\n")
bmw.go()
bmw.turn(1)
bmw.turn(2)
bmw.show_speed()
print("\n")
nissan.go()
nissan.turn(1)
nissan.turn(2)
print(nissan.is_police)
print("\n")
audi.go()
audi.turn(1)
audi.turn(2)
print(audi.is_police)
