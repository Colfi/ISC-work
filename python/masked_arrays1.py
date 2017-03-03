import numpy.ma as MA
maskedarray = MA.masked_array(data=range(0,10),fill_value=-999)
print maskedarray 
print maskedarray.fill_value
maskedarray[2]=MA.masked
print maskedarray
narr = MA.masked_where(maskedarray<7,maskedarray)
print narr.fill_value
arr2=MA.filled(narr)
print arr2 
print type(arr2)
