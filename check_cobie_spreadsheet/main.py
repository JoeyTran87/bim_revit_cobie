# IN: READ EXCEL FILE
# done


# PROCESS: FIND NAMING ERROR


# OUT: EXPORT TXT

import pandas as pd

#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
# functions

#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
# execution
if __name__ == "__main__":
    print("This is Main")
    path_excel = r"C:\Users\USER\Documents\GitHub\bim_revit_cobie\check_cobie_spreadsheet\xlsx\BW.TPT4-A-BVHC-GH-ZZ-GUARDHOUSE 1_COBie Export.xlsx"
    sheet_name = "Instruction"

    df = pd.read_excel(path_excel,sheet_name)

    print(df)