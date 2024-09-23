# soda_project_test.py
import turtle as trtl
t1 = trtl.Turtle() #turtle that draws soda
t2 = trtl.Turtle() #turtle that draws cup
wn=trtl.Screen()
#import photo
wn.bgpic("soda.png")
#makes turtles invisible
t1.hideturtle()
t2.hideturtle()


''' coordinates of soda
sprite = (40,-5)
dc = (-80,-5)
coke = (160,-5)
rb = (282,-5)
lem = (-200,-5)
dp = (-320,-3)'''


#function for the color and position
#x and y determine position of the soda, cx cy determine position of cup
def sodapour(x,y,sodacolor,cx,cy):
    soda = (x,y)
   
    #draws cup
    t2.speed(0)
    t2.fillcolor(sodacolor)
    t2.pensize(7)
    t2.penup()
    t2.goto(cx,cy)
    t2.pendown()
    t2.begin_fill()
    t2.right(90)
    t2.forward(200)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(200)
   
    #goes to position of soda
    t1.speed(5)
    t1.pensize(2)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    #chooses color and draws the soda pouring
    for step in range(2):
        t1.pencolor(sodacolor)
        t1.fillcolor(sodacolor)
        t1.begin_fill()
        t1.forward(45)
        t1.right(90)
        t1.forward(350)
        t1.right(90)
        t1.end_fill()
    #makes soda dissapear after a few seconds    
    t1.penup()
    for step in range(2):
        t1.goto(-1000,-1000)
        t1.goto(-2000,-2000)
    #makes soda dissapear
    t1.clear()
    #fills cup
    t2.end_fill()




# List of valid choices
valid_choices = ['Dr Pepper', 'Lemonade', 'Diet Coke', 'Sprite', 'Coke', 'Root Beer']




while True:
    choice = input("Which Soda? ")
   
    if choice in valid_choices:
        if choice == 'Dr Pepper':
            sodapour(-320, -3, "saddle brown",-350,-170)
        elif choice == 'Lemonade':
            sodapour(-200, -5, "lemon chiffon",-220,-170)
        elif choice == 'Diet Coke':
            sodapour(-80, -5, "saddle brown",-100,-170)
        elif choice == 'Sprite':
            sodapour(40, -5, "white",10,-150)
        elif choice == 'Coke':
            sodapour(160, -5, "saddle brown",130,-170)
        elif choice == 'Root Beer':
            sodapour(280, -5, "saddle brown",240,-170)
        break  #stops loop if a valid answer is chosen
    else:
        print("We don't serve that, try something else.")




wn = trtl.Screen()
wn.mainloop()


