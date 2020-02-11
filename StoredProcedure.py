
import pyodbc



class ExecuteProcedure:

    def __init__(self):
        self.server = 'e6kvli9933.database.windows.net'
        self.database = 'DataFactory'
        self.username = 'DataFactory'
        self.password = '#GC9coHtKQLR'
        self.driver= '{ODBC Driver 17 for SQL Server}'

    def call_procedure(self):
        try:
            cnxn = pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
            cursor = cnxn.cursor()
            return_value=cursor.execute("{call usp_GetFileName()}")
            for i in return_value:
                current_excel_month=i[2]
            
            return current_excel_month
        except Exception as e:
            print(str(e))
            raise

