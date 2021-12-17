from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        food_color = ["red", "blue", "green", "yellow", "white", "purple"]
        random_food_color = random.choice(food_color)
        self.color(random_food_color)
        self.goto(random_x, random_y)

