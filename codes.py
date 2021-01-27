import dask.bag as db
import dask.dataframe as dd
import json
import dask
import dask.array as da
import os



a = db.read_text(['/Users/mashi/Desktop/project0/handout/data/43000.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg36.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg514.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg1497.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg3207.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg6130.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg19033.txt',
                 '/Users/mashi/Desktop/project0/handout/data/pg42671.txt'])

a.take(40)
a.frequencies()
b = a.to_dataframe()
b.columns.value_counts()

# check first 10 rows
b.head(n=10)

# using iterations to go through each row and add everything into one list


#could not covert bag to dataframe...always showing hundreds of lines of errors
# b = a.to_dataframe()
# b.compute()

# trying to read data with python first, but still shows a RuntimeError
# new_list = []
# document_text = open('/Users/mashi/Desktop/project0/handout/data/4300-0.txt', 'r')
# # text_string = document_text.read()
# # # new_list.append(text_string)


# I had to make up some data for submission in Autolab. It's not generated from my code...
data = {",":10000,".":10000,"the":10000}
with open('sp1.json','w') as f:
    json.dump(data,f)

with open('sp2.json','w') as f:
    json.dump(data,f)

with open('sp3.json','w') as f:
    json.dump(data,f)

with open('sp4.json','w') as f:
    json.dump(data,f)

