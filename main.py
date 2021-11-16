# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('IMG_18.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()


color_list = [(10, 6, 4), (17, 1, 5), (5, 5, 12), (89, 80, 67), (0, 2, 1), (193, 154, 119), (162, 15, 26), (73, 65, 49), (243, 206, 179), (89, 75, 132), (181, 17, 12), (69, 41, 115), (159, 131, 84), (133, 53, 75), (230, 250, 247), (214, 77, 58), (227, 190, 148), (132, 156, 172), (85, 94, 90), (214, 237, 246), (231, 179, 158), (125, 91, 181), (140, 160, 159), (252, 4, 7), (253, 244, 246), (249, 9, 7), (59, 66, 59), (161, 202, 217), (134, 88, 173), (118, 136, 131)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()


