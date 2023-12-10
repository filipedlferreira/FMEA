import pandas as pd
import graphs_data as graph
import func_data as func

still_run = True



while still_run == True:
  
  df = pd.read_csv("fmea_generic.csv", delimiter = ";")
  df = func.rpn_criticality_calc(df)
  
  print('''Available inputs:
  1. RPN vs Criticality/Detectability
  2. RPN vs Detectability
  3. Percentage of highest RPN defects by Operation Number
  4. Percentage of highest RPN defects by Process Phase
  5. Most used process control method in the highest RPN defects
  6. Most used process control method for the whole process
  7. Save a .csv file with the highest 20% RPN value
  ''')
  
  choice = input("What is the information you need? (Choose the number of the options above or exit to close)\n").lower()

  if choice == "exit":
    still_run = False
  elif choice == "1":
    df = graph.graph_rpn_vs_crit_detect(df)
  elif choice == "2":
    df = graph.graph_rpn_vs_detect(df)
  elif choice == "3":
    df = graph.high_rpn_op_number(df)
  elif choice == "4":
    df = graph.high_rpn_process_phase(df)
  elif choice == "5":
    df = graph.most_used_process_control_20(df)
  elif choice == "6":
    df = graph.most_used_process_control_100(df)
  elif choice == "7":
    df = graph.csv_highest_rpn(df)
  else:
    print("\n\nThat is not a valid choice\n\n")