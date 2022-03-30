# import colorgram
# rgb_color = []
# colors = colorgram.extract("image2.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r, g, b))
# print(rgb_color)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
screen = Screen()

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
             (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
             (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
             (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
             (156, 212, 190), (87, 46, 33), (37, 45, 83)]
tim.speed(0)
tim.hideturtle()
tim.setheading(220)
tim.penup()
tim.forward(400)
tim.setheading(0)


number_of_dots = 144
for dot_count in range(1, number_of_dots + 1):
    tim.forward(50)
    tim.dot(20, random.choice(color_list))

    if dot_count % 12 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(600)
        tim.setheading(0)


screen.exitonclick()

