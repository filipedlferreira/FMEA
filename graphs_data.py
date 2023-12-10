import pandas as pd
from matplotlib import pyplot as plt
import func_data as func

def graph_rpn_vs_crit_detect(df):
  
  # Data cleanup
  df = func.clean_up_data(df)
  
  # RPN sorting
  df = func.sort(df)
  
  # Pareto Law application
  df = func.pareto_law(df)

  # Graph making
  fig, ax1 = plt.subplots()
  
  ## Atribuição da data a fazer plot
  rpn_sort_x = df["Defect number"]+" "+df["Potential failure mode"]
  rpn_sort_y = df["RPN"]
  rpn_sort_y2 = df["Detectability"]
  rpn_sort_y3 = df["Criticality"]

  ## Rotação dos parametros do eixo x
  ax1.tick_params(axis='x', labelrotation = 90)

  ## Plot do RPN em função dos potencial failure Modes
  ax1.bar(rpn_sort_x, rpn_sort_y, color = "b", width = 0.85)

  ## Adicionar um segundo eixo para o mesmo eixo x
  ax2 = ax1.twinx()
  ax2.plot(rpn_sort_x, rpn_sort_y2, color = "r",linewidth = 2, linestyle = "-", marker = "o", markeredgecolor = "r", label = "Detectability")

  ## Adicionar um terceiro eixo para o mesmo eixo x
  ax3 = ax1.twinx()
  ax3.plot(rpn_sort_x, rpn_sort_y3, color = "g", linewidth = 2, marker = "o", label = "Criticality")

  ## Alterar a posição do terceiro eixo para a direita para não ficar em cima do outro
  ax2.spines["right"].set_position(("axes",1.12))

  ## Adicionar labels aos eixos
  ax1.set_ylabel("RPN", color = "b")
  ax2.set_ylabel("Detectability", color = "r")
  ax3.set_ylabel("Criticality", color = "g")

  ## Alterar as cores dos parâmetros dos eixos
  ax1.tick_params(axis = "y", colors = "b")
  ax2.tick_params(axis = "y", colors = "r")
  ax3.tick_params(axis = "y", colors = "g")

  ## Alterar a cor das barras dos eixos
  ax2.spines["right"].set_color("r")
  ax3.spines["right"].set_color("g")
  ax3.spines["left"].set_color("b")

  
  plt.title("RPN vs Criticality/Detectability \nof the 20% highest RPN defects", fontdict= {"fontweight":"bold", "fontsize":18})
  ax1.set_xlabel("Defect Number and corresponding Failure Mode", fontdict= { "fontsize":12})
  plt.show()

def graph_rpn_vs_detect(df):
  
  # Data cleanup
  df = func.clean_up_data(df)
  
  # RPN sorting
  df = func.sort(df)
  
  # Pareto Law application
  df = func.pareto_law(df)

  # Graph making
  fig, ax1 = plt.subplots()

  ## Atribuição da data a fazer plot
  rpn_sort_x = df["Defect number"]+" "+df["Potential failure mode"]
  rpn_sort_y = df["RPN"]
  rpn_sort_y2 = df["Detectability"]

  ## Rotação dos parametros do eixo x
  ax1.tick_params(axis='x', labelrotation = 90)

  ## Plot do RPN em função dos potencial failure Modes
  ax1.bar(rpn_sort_x, rpn_sort_y, color = "b", width = 0.85)

  ## Adicionar um segundo eixo para o mesmo eixo x
  ax2 = ax1.twinx()
  ax2.plot(rpn_sort_x, rpn_sort_y2, color = "r",linewidth = 2, linestyle = "-", marker = "o", markeredgecolor = "r", label = "Detectability")

  ## Alterar a posição do terceiro eixo para a direita para não ficar em cima do outro
  ax2.spines["right"].set_position(("axes",1))

  ## Adicionar labels aos eixos
  ax1.set_ylabel("RPN", color = "b")
  ax2.set_ylabel("Detectability", color = "r")

  ## Alterar as cores dos parâmetros dos eixos
  ax1.tick_params(axis = "y", colors = "b")
  ax2.tick_params(axis = "y", colors = "r")

  #Alterar os valores do segundo eixo
  ax2.set_yticks(range(1,11,1))

  ## Alterar a cor das barras dos eixos
  ax2.spines["right"].set_color("r")

  #plt.legend()
  plt.title("RPN vs Detectability\nof the 20% highest RPN defects", fontdict= {"fontweight":"bold", "fontsize":18})
  ax1.set_xlabel("Defect Number and corresponding Failure Mode", fontdict= { "fontsize":12})
  plt.show()

def high_rpn_op_number(df):

  # Data cleanup
  df = func.clean_up_data(df)

  # RPN sorting
  df = func.sort(df)
  
  # Convert the Defect number row to string
  df["Defect number"] = df["Defect number"].astype(str)

  # Create a new column with the Operation Number
  df["Operation_number"] = df["Defect number"].apply(lambda x: x.split(".")[0])

  # Pareto Law application
  df = func.pareto_law(df)

  # Create a Count column to group by operation number and operation phase
  operation_counts = df.groupby(["Operation_number", "Operation Phase"]).size().reset_index(name='Count')

  # Graph making
  plt.pie(operation_counts["Count"], labels=operation_counts["Operation_number"] + ". " + operation_counts["Operation Phase"],autopct = "%.2f%%", pctdistance = 0.80)
  plt.title("Percentage of highest RPN defects\nby Operation Number", fontdict= {"fontweight":"bold", "fontsize":18})
  plt.show()


def high_rpn_process_phase(df):

  # Data cleanup
  df = func.clean_up_data(df)

  # RPN sorting
  df = func.sort(df)

  # Convert the Defect number row to string
  df["Defect number"] = df["Defect number"].astype(str)

  # Create a new column with the Operation Number
  df["Operation_number"] = df["Defect number"].apply(lambda x: x.split(".")[0])

  # Pareto Law application
  df = func.pareto_law(df)

  # Group those 20% by process phase.
  operation_counts = df.groupby(["Process Phase"]).size().reset_index(name='Count')
  
  plt.pie(operation_counts["Count"], labels=operation_counts["Process Phase"],autopct = "%.2f%%", pctdistance = 0.8)
  
  plt.title("Percentage of highest RPN defects\nby Process Phase", fontdict= {"fontweight":"bold", "fontsize":18})
  plt.show()


def most_used_process_control_20(df):
  # Data cleanup
  df = func.clean_up_data(df)

  # RPN sorting
  df = func.sort(df)
  
  # Pareto Law application
  df = func.pareto_law(df)
  
  # Group by Process Control.
  operation_counts = df.groupby(["Current process control"]).size().reset_index(name='Count')

  plt.pie(operation_counts["Count"], labels=operation_counts["Current process control"],autopct = "%.2f%%", pctdistance = 0.75)

  plt.title("Most used process control method in the highest RPN defects", fontdict= {"fontweight":"bold", "fontsize":18})
  plt.show()



def most_used_process_control_100(df):
  # Data cleanup
  df = func.clean_up_data(df)

  # Group by Control method.
  operation_counts = df.groupby(["Current process control"]).size().reset_index(name='Count')
  
  plt.pie(operation_counts["Count"], labels=operation_counts["Current process control"],autopct = "%.2f%%", pctdistance = 0.8)
  
  plt.title("Most used process control method for the whole process", fontdict= {"fontweight":"bold", "fontsize":18})
  plt.show()

def csv_highest_rpn(df):
  # Data cleanup
  df = func.clean_up_data(df)

  # RPN sorting
  df = func.sort(df)

  # Pareto Law application
  df = func.pareto_law(df)

  #Name the document
  csv_name = input("What is the name you want for the file? ")
  
  #File save
  df.to_csv(csv_name + '.csv', index=False, sep =";")