
import pyodbc



class ExceptionProcedure:

    def __init__(self):
        self.server = 'e6kvli9933.database.windows.net'
        self.database = 'DataFactory'
        self.username = 'DataFactory'
        self.password = '#GC9coHtKQLR'
        self.driver= '{ODBC Driver 17 for SQL Server}'

    def Execution_procedure(self,errorvalue):
     
        cnxn = pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        cursor = cnxn.cursor()
     
     
        return_value=cursor.execute('{CALL usp_SetError(@errmsg =?, @stage =?,@source  =?,@errType =?)}',(errorvalue, 'FCM Python Script','FCM','P'))
        cnxn.commit()
     
        return "Error"
    

