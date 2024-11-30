#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self,brand,size):
        pass
        self.brand =brand
        self.size = size
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"


    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition