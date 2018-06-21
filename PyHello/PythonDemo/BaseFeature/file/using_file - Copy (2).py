fp = open("a.txt", "a+", 0)
print ('open',fp.tell())
x = fp.read()
print ('open read()',fp.tell())
print (x)
fp.write("123456\n")
print ('write 1-6',fp.tell())
x = fp.read()
print ("first read\n",x)
fp.seek(0)
x = fp.read()
print ("second read\n", x,fp.tell())
fp.close()
"""————————————————————————————————————
结果是：(第一次运行时)
————————————————————————————————————
open 0
open read() 0

write 1-6 8
first read

second read
123456
8
————————————————————————————————————
结果是：(第二次运行时)
————————————————————————————————————
open 0
open read() 8
123456

write 1-6 16
first read

second read
123456
123456
16
"""