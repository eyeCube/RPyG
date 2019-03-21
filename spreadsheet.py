'''
speadsheet.py
functions to get metadata from spreadsheets and load it into the game
'''

import xlrd
import os

class Weapon:
    weapList = {}
    def __init__(self, weapID, mods):
        for k,v in cls.weapList[weapID].items():
            self.__dict__.update({k:v})
        self.mods = mods
        
    @classmethod
    def getWeapons(cls):
        weapons = "weapons.xlsx"
        loc = os.path.join(os.curdir, "meta", weapons)

        try:
            wb = xlrd.open_workbook(loc)
        except:
            print("failed to open spreadsheet '", weapons, "'.")
        try:
            sheet = wb.sheet_by_index(0)
        except:
            print("failed to open spreadsheet '", weapons, "' sheet index 0.")

        print("successfully loaded spreadsheet '", weapons, "'. Reading...")
        
        cols = []
        for i in range(sheet.ncols):
            val = sheet.cell_value(0, i)
            cols.append(val)

        for i in range(sheet.nrows - 1):
            weapID = None
            weap = []
            for j in range(sheet.ncols - 1):
                val = sheet.cell_value(i+1, j)
                weap.append({cols[j] : val})
                if cols[j] == "ID":
                    weapID = val
            cls.weapList.update({weapID : weap})

