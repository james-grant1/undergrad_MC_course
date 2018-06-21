# Script to import yaml file, convert nmol for gcmc calcs and export csv

# yaml library handles import the file
import yaml
fstream=open("YAMLDATA.000")
# The file consists of two 'yaml files'
# simparams details the simulation parameters
# dataset contains the data
[ simparams, dataset ] = yaml.load_all(fstream)

# e.g. these can be printed with
# print(simparams)
# print(dataset)

#Generate the list of keys in the list of dicts
data_keys = dataset[0].keys()

# The nmol is a list in its own right so if present
# This needs to be stripped, assuming a single gcmc particle:
if 'nmol' in data_keys:
    for my_dict in dataset:
        my_dict['nmol'] = my_dict['nmol'][-1]

# You can now play with the data in python
# or output the data to a csv
import csv
with open("data.csv",'w') as ostream:
     csv_writer = csv.DictWriter(ostream, data_keys)
     csv_writer.writeheader()
     csv_writer.writerows(dataset)
