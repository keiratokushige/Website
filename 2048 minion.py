import turtle as trtl


wn = trtl.Screen()
wn.setup(width=800, height= 600)
wn.bgpic("2048 background.png")

wn.register_shape(".png")

d = trtl.Turtle()
d.goto(0,0)
d.shape(".png")





wn.mainloop()