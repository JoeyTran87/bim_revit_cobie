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
    path_excel = input("\tExcel Path: ")#r"C:\Users\USER\Documents\GitHub\bim_revit_cobie\check_cobie_spreadsheet\xlsx\BW.TPT4-A-BVHC-GH-ZZ-GUARDHOUSE 1_COBie Export.xlsx"

    xl = pd.ExcelFile(path_excel)
    sheet_names = xl.sheet_names
    print('[Sheet Name]')
    [print(f"{i} : {sheet_names[i]}") for i in range(len(sheet_names))]
    
    while True:
        try:
            sheet_name = sheet_names[int(input("\tPick index of Sheet Name: "))]
        except:
            pass
        if sheet_name == "":
            df = pd.read_excel(path_excel,)
            break
        else:        
            df = pd.read_excel(path_excel,sheet_name)
            break


    print(df)