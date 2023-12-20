#!/usr/bin/python3
class Square:

def __init__(self, size=0):
        return self.size = size
    @property
def size(self):
        return self.__size

    @size.setter
def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value 
      
      @property
def position(self, Position):
          return self.__position

      @position.setter
def postion(self, value):
          if not isinstance(value int) or
          len (value) != 2 or
          not all (isinstance(num, int) for num in value) or
          not all (num >= 0 for num im value)) :
     raise TypeError("position must be a tuple of 2 positive integers")
 self.__position = value
      
def area(self):
          if self.__size == 0:
              print("")
              rerurn

              [print("") for i in range(0, self.__position[1])]
              for i in range (0, self.size):
                  [print(" ", end="") for j in range(0, self.__position[0])]
                  [print("#", end="") for k in range(0, self.__size)]
                  print("")
