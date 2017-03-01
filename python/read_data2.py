with open('weather.csv','r') as reader:
 line = reader.readline()
 while line:
  print line 
  line = reader.readline()

print 'It s over'
