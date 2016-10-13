import petl as etl

#Extracting data from example csv file
table1 = etl.fromcsv('example.csv')
print table1
#etl.look(table1)

#Transformation function to be applied on extracted data
table2 = etl.convert(table1,'foo','upper')
table3 = etl.convert(table2,'bar',int)
table4 = etl.convert(table3,'baz',float)
table5 = etl.addfield(table4, 'finally', lambda row: row.bar * row.baz)
print table5
#etl.look(table5)

#Writing above ETL pipeline in a functional style
table = (etl
         .fromcsv('example.csv')
         .convert('foo', 'upper')
         .convert('bar', int)
         .convert('baz', float)
         .addfield('finally', lambda row: row.bar * row.baz)
       )

table.look() #look function only displays five rows.
print table

#OOP style programming
l = [['foo','bar'], ['a', 1], ['b', 2], ['c', 2]]
table6 = etl.wrap(l)
print table6
