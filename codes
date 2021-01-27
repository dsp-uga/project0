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

#could not covert bag to dataframe...
# b = a.to_dataframe()
# b.compute()

# trying to read data with python first, but still shows a RuntimeError
# new_list = []
# document_text = open('/Users/mashi/Desktop/project0/handout/data/4300-0.txt', 'r')
# # text_string = document_text.read()
# # # new_list.append(text_string)
