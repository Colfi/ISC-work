mylist = [1,2,3,4]
print mylist[1]
print mylist[0:4]
print mylist[1:4]

list2 = range(1,11) 
print list2
blist =[12,13,14]
list2.extend(blist)
print(list2)

forward = list()
backward = list()

values = ["a","b","c"]
for x in values:
 forward.append(x)
 backward.extend(x)
print forward
print backward
values.reverse()
print values 
if forward==backward:
 print "Lists are the same"
