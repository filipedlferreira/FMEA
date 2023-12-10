import math
import pandas as pd
from matplotlib import pyplot as pd
from math import ceil

def clean_up_data(df):
  df = df.map(lambda x: x.strip() if isinstance(x,str) else x)
  columns_check = ["Severity","Occurrence","Detectability"]
  rows_delete = df[(df[columns_check].isna() | (df[columns_check]==0)).any(axis =1)]
  df = df.drop(rows_delete.index)
  return df

def rpn_criticality_calc(df):
  df["RPN"] = df["Severity"]*df["Occurrence"]*df["Detectability"]
  df["Criticality"] = df["Severity"]*df["Occurrence"]
  return df

def sort(df):
  df = df.sort_values(["RPN"],ascending = False)
  return df

def pareto_law(df):
  '''Returns the Defects that represent 20% of the highest RPN'''
  ### Pareto Law ###
  row_len = len(df.iloc[:])
  twenty_pc = row_len*.2
  twenty_pc = math.ceil(twenty_pc) 

  # Obtain the first 20% of highest rpn number
  df = df.iloc[:twenty_pc]
  return df