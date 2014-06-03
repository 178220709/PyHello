def func():
    global x

    print ('x is', x)
    x = 2
    print ('Changed local x to', x)

x = 50
func()
print ('Value of x is', x)

def say(message, times = 2):
    print (message * times)
   

say('Hello')
say('World', 5)


def func(a, b=5, c=10):
    print ('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)