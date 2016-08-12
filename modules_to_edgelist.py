#!/bin/python
#Author: Anna-Lisa R. Doebley
#        Laboratory of Evan Eichler
#Date: 08/12/2016

#to run this script enter the following in command line:
#python modules_to_edgelist.py path/to/module_file.txt path/to/coexpression_data.txt path/to/ppi_data.txt

#module_file should be a txt file in the format: 
#gene,modulename
#see full_module_list.txt for example

#coexpression_data should be a tab separated text file in the format: 
#gene1	gene2	pearson_correlation_coefficient_r^6 
#see adj1.csv.Tab.BinaryFormat for example
#this script will select those with significant coexpression

#ppi_data should be a tab separated text file in the format:
#gene1	gene2
#should only contain pairs of genes which have ppis
#see StringNew_BioGrid for example


#import the necessary things and define the arguments provided:
import csv
from sys import argv
script, module_file, coexpression_data, ppi_data = argv

#make a list of all the genes in your modules:
mods=open(module_file, 'r')
csv_mods=csv.reader(mods, delimiter=',')

modlist=[]

for row in csv_mods:
    if row[0] == 'Gene':
            continue
    modlist.append(row[0])

mods.close()

#make a dictionary of the genes and modules:
mods=open(module_file, 'r')
csv_mods=csv.reader(mods, delimiter=',')

mod_dictionary={}

for row in csv_mods:
	if row[0] == 'Gene':
		continue
	mod_dictionary[row[0]]=row[1]

mods.close()

#make an edgelist of all the genes in your modules with both ppis and coexpression:
ppis=open(ppi_data, 'r')
csv_ppis=csv.reader(ppis, delimiter='\t')

ppilist=[]

for row in csv_ppis:
    ppilist.append(row),
    ppilist.append(list(reversed(row)))

ppis.close()

edgelist_all=open("edgelist_all.txt", 'w')
csv_edgelist_all=csv.writer(edgelist_all, delimiter='\t')

with open(coexpression_data, 'r') as expdata:
    csv_expdata = csv.reader(expdata, delimiter='\t')
    for row in csv_expdata:
        if row[0] in modlist:
            if row[1] in modlist:
                if float(row[2])>0.050653:
                    if row[0:2] in ppilist:
                    	csv_edgelist_all.writerow(row)
                    	#print '\t'.join(row)+'\n'

edgelist_all.close()
expdata.close()

#make an edgelist of all the ppis+coexpression between genes within a module:
edgelist_within=open("edgelist_within.txt",'w')
csv_edgelist_within=csv.writer(edgelist_within, delimiter='\t')

edgelist_all=open("edgelist_all.txt", 'r')
csv_edgelist_all=csv.reader(edgelist_all, delimiter='\t')

for row in csv_edgelist_all:
	if mod_dictionary[row[0]] == mod_dictionary[row[1]]:
		csv_edgelist_within.writerow(row)
		
edgelist_within.close()
edgelist_all.close()
