import pandas as pd
import urllib.request
import shutil

'''download latest XLS file from ANAC website'''
url = 'http://www.anac.gov.br/assuntos/setor-regulado/aerodromos/cadastro-de-aerodromos/aerodromos-cadastrados/aerodromospublicos-12.xls'

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open('last_checked_file/latest.xls', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

'''Read XLS file to variable'''
xlsFile = pd.ExcelFile('last_checked_file/latest.xls')

'''Parse XLS to pandas DataFrame'''
XlsDataFrame = xlsFile.parse(0)

'''spy file head :-)'''
print(XlsDataFrame.head())

'''save dataframe to csv for later use'''
XlsDataFrame.to_csv('last_checked_file/latest.csv')
