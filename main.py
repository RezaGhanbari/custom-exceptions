import unittest

class Car:
    def init(self, speed, color):
        self.speed = speed
        self.color = color

    def __eq__(self, another_car):
        if type(self)==type(another_car) and self.speed==another_car.speed and self.color == another_car.color:
            return True
        else:
            return False

class AssertCarEqual:
    def assert_car_equal(self, car1, car2):
        if type(car1) != type(car2):
            raise AssertionError("car1 of type: ", type(car1), " and car2 of type: ", type(car2))
        elif car1.speed !=car2.speed:
            raise AssertionError("speed of car1: ", car1.speed, " and speed of car2 : ", car2.speed)
        elif car1.color != car2.color:
            raise AssertionError("color of car1: ", car1.color, " and color of car2 : ", car2.color)

class TestCar(unittest.TestCase, AssertCarEqual):
    def test_car_equal(self):
        car1 = car.Car(40, 'blue')
        car2 = car.Car(40, 'red')
        self.assert_car_equal(car, car2)

if __name__ == "__main__":
    x = TestCar()
    x.test_car_equal()
