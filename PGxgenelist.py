#!/usr/bin/env python

import sys, getopt
# from typing import BinaryIO, Dict, Any
from pprint import pprint
# import pandas as pd
# import numpy as np
import io
import re

if __name__ == "__main__":
    #get text from web (CPIC2019,FDA2017,KoreanHan2017,PGxGamazon2012,PharmGKBClinical,TruGenome,Drugbank515,PGRNseq2016,PharmGKBVIP66,iPLEXPGx)
    genelist = sys.argv[1].split(',')
    genepath = sys.argv[2]
    dict_gene = {}
   # genelist ={"CPIC2019.txt","FDA2017.txt","KoreanHan2017.txt","PGxGamazon2012.txt","PharmGKBClinical.txt","TruGenome.txt","Drugbank515.txt","PGRNseq2016.txt","PharmGKBVIP66.txt","iPLEXPGx.txt"}
    
    for gene in genelist:
        filelist = genepath+gene+".txt"
        with open(filelist, "r") as f:
            for line in f:
                line = line.strip()
                dict_gene[line] = 1
        f.close()
    
   # k = open('filtergene.txt', 'w')
   # pprint (dict_gene)
    for key,value in dict_gene.items() :
      #  k.write("%s\n" % (str(key)))
        print (key)
    # 
    
    
 #   k.close


