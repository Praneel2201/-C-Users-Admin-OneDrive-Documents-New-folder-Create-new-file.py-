# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:27:35 2023

@author: Praneel Talekar

Description: This code is designed to create a dataframe from a dictionary and save it to a path determined by you.
"""

import pandas as pd

data = {"Names":[],
        "Maths":[],
        "Science":[],
        "Marathi":[],
        "History":[],
        "Geography":[],
        "Total marks":[],
        "Percentage":[]}
df=pd.DataFrame(data)

File_path=input("File path: ")
File_path_full=File_path+"Studemt data.csv"

df.to_csv(File_path_full,index=True)

print("file successfully saved at path: ",File_path,"\n","With name: Studemt data")

