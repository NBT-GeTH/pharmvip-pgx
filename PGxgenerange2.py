#!/usr/bin/env python

import sys, getopt
# from typing import BinaryIO, Dict, Any
from pprint import pprint
# import pandas as pd
# import numpy as np
import io
import re

if __name__ == "__main__":
    genelist = sys.argv[1]
    generange = sys.argv[2]

    dict_range = {}
    listrange=[]
    
    ##add bed to dict
    filelist = generange
    with open(filelist, "r") as f:
        for line in f:
            line = line.strip()
            genename = line.split('\t')[3]

            if not genename in dict_range:
               # print ("new"+genename)
                listrange=[]
                dict_range[genename] = {}
                listrange.append(line) 
                dict_range[genename] = listrange
                #print (dict_range[genename])
            else:
             #   print ("dup"+genename)
                # print (dict_range[genename])
                listrange = dict_range[genename]
                listrange.append(line)
                #print (listrange)
                dict_range[genename] = listrange
    f.close()
    
    with open(genelist, "r") as f:
        for gene in f:
           # print (gene)
            gene = gene.strip()
            print(*dict_range[gene], sep = "\n") 
            #print ("\n")


