from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear() 
import math 
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
        # print(math.sqrt((self.coor1[1] - self.coor1[0])**2 +(self.coor2[1] - self.coor2[0])**2))
    
    def slope(self):
        pass

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()