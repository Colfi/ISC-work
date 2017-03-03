import numpy.ma as MA
m1 = MA.masked_array(data=range(1,9))
print m1 
m2 = m1.reshape(2, 4)
print m2
m3=MA.masked_greater(m2,6)
print m3*100 
res = m3 - MA.ones((2, 4))
print(res)
print type(res)

