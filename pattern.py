import turtle as t


a1=t.Turtle()
a1.speed(100)

a2=t.Turtle()
a2.speed(100)


a1.color("red");
a2.color("blue");

for x in range(100):
    e=1;d=-1
    a1.forward(e*x)
    a1.left(e*x)
    a1.forward(d*(x+1))
    a1.left(d*(x+1))
    e=-1;d=1
    a2.forward(e*x)
    a2.left(e*x)
    a2.forward(d*(x+1))
    a2.left(d*(x+1))
