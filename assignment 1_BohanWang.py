# ============================================================
# Assignment:    Assignment One
# Student Name:  Bohan Wang
# ============================================================

# ==================== Q1: Turtle Drawing ====================
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Star")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple", "pink"]

length = 20
for i in range(100):
    pen.color(colors[i % len(colors)])
    pen.forward(length)
    pen.right(144)
    length += 2

pen.penup()
pen.goto(-200, -150)
pen.pendown()
pen.width(4)
tri_colors = ["red", "lime", "dodgerblue"]
for i in range(3):
    pen.color(tri_colors[i])
    pen.forward(400)
    pen.left(120)

turtle.done() 

# ==================== Q2: QA Bot ====================
print("Question Answering Bot")
print("You can ask about: HKU, robot, jetson, ai, human\n")

question = input("Ask me something: ")

if question == "HKU":
    print("Bot: HKU is The University of Hong Kong.")
elif question == "robot":
    print("Bot: A robot is a machine that can work automatically.")
elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer made by NVIDIA.")
elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")
elif question == "human":
    print("Bot: Humans are intelligent living beings.")
else:
    print("Bot: Sorry, I don't understand.")