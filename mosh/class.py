# class Point:
#     def move(self):
#         print('Move On')

#     def draw(self):
#         print('Draw it')

# # Point1 = Point()
# # Point1.move()
# # Point1.x = 10
# # print(Point1.x)
# Point1 = Point()
# print(Point1.x) #error


# Constructor
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move(self):
        print('Move On')

    def draw(self):
        print('Draw it')

Point1 = Point(10,20)
print(Point1.x)
print(Point1.y)