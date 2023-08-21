# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
tim = Turtle()
colormode(255)

tim.hideturtle()
tim.penup()
tim.setpos(-150,-150)

def draw_row():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

def start_pos(y):
    tim.setpos(-150,(-150 + y*50))

start = 0
for _ in range (10):
    start_pos(start)
    draw_row()
    start += 1

screen = Screen()
screen.exitonclick()
