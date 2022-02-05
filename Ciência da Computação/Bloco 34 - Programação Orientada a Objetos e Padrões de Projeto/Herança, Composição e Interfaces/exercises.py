from abc import abstractmethod, abstractproperty


class TV:
    def __init__(self, size):
        self.__size = size
        self.__channel = 50
        self.__volume = 1
        self.__on = False

    def increase_volume(self):
        if self.__volume < 100:
            self.__volume += 1
            print(f"Volume is now at {self.__volume}")

    def decrease_volume(self):
        if self.__volume > 1:
            self.__volume -= 1
            print(f"Volume is now at {self.__volume}")

    def change_channel(self, channel):
        if type(channel) is not int or channel < 1 or channel > 99:
            raise ValueError("Channel must be an integer between 1 and 99")
        self.__on = True
        self.__channel = channel
        print(f"Channel is now at {self.__channel}")

    def toggle_power(self):
        if self.__on:
            self.__on = False
            print("TV is now off")
        else:
            self.__on = True
            print("TV is now on")


class Statistics:
    data = [9243, 234923, 92, 9234, 91234,
            4756, 234, 4358, 12, 324, 8439, 2348]

    @classmethod
    @property
    def mean(cls):
        return sum(cls.data) / len(cls.data)

    @classmethod
    @property
    def median(cls):
        cls.data.sort()
        if len(cls.data) % 2 == 0:
            return (cls.data[len(cls.data) // 2] + cls.data[(len(cls.data) // 2) - 1]) / 2
        else:
            return cls.data[len(cls.data) // 2]

    @classmethod
    @property
    def mode(cls):
        mode_dict = {}
        for item in cls.data:
            if item in mode_dict:
                mode_dict[item] += 1
            else:
                mode_dict[item] = 1
        return max(mode_dict, key=mode_dict.get)


class Shape:
    @abstractproperty
    def area(self):
        raise NotImplementedError
    
    @abstractproperty
    def perimeter(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return (self.width + self.height) * 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius ** 2 * 3.14

    @property
    def perimeter(self):
        return self.radius * 2 * 3.14

