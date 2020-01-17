# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:19:12 2020

@author: BarendS
"""
import pandas as pd
import os 
DATA_DIR="D:\\BarendS\\Documents\\data" 
os.chdir(DATA_DIR)
def open_weights():
    file1 = pd.read_excel('weights_good.xlsx')
    return file1
    

weights = open_weights()
