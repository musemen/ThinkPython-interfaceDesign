import turtle

bob = turtle.Turtle()

print (bob)
turtle.mainloop()

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

for i in range(4):
    print ("hello")


def polygon (t,length,n):
    for i in range (4):
            angle=360/n
            bob.fd (length)
            bob.lt(angle)

polygon(bob,100,3)



