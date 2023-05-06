import os
import pygsheets


service_file = os.environ.get("service_file")
print(service_file)
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Набор"
sh = gc.open(sheetname)
wks = sh.sheet1