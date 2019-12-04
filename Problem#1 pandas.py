import pandas

data1 = {'Student' :['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}

data2 = {'Student':['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}

data3 = {'Student':['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,94]}

data4 = {'Student':['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}

A = pandas.DataFrame(data1, columns = ['Student','Math'])

B = pandas.DataFrame(data2, columns = ['Student','Electronics'])

C = pandas.DataFrame(data3, columns = ['Student','GEAS'])

D = pandas.DataFrame(data4, columns = ['Student','ESAT'])

merge1 = pandas.merge(A,B,on = 'Student')

merge2 = pandas.merge(merge1,C,on = 'Student')

merge3 = pandas.merge(merge2,D,on = 'Student')

long = pandas.melt(merge3, id_vars = ['Student'], var_name = 'Subject', value_name = 'Grades')

print(long)