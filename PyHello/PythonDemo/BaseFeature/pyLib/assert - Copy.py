i = []
i.append('item')
#`i`"['item']"

print(repr(i))
#"['item']"

obj =  eval(repr(i)) 
print(obj)