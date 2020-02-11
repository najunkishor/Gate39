from ExcelToCsv import ExportExcelToCsv
from Scrap import WebScrap
from StoredProcedure import ExecuteProcedure
from WebToBlob import AzureBlobStoage
from createfilename import filename 
from exception import ExceptionProcedure

try:
    # Execute the procedure and that return month value

    ExecuteProcedure_obj=ExecuteProcedure()
    current_excel_month=ExecuteProcedure_obj.call_procedure()




    # scrap the website,select the corresponding table and return the excel url based on the year and month
    WebScrap_obj=WebScrap()
    current_excel_href=WebScrap_obj.WebScrapFunction(current_excel_month)

    # create file name
    filename_obj=filename()
    filenamevalue=filename_obj.create_filename(current_excel_href)



    # convert the excel to csv
    ExportExcelToCsv_obj=ExportExcelToCsv()
    export_csv=ExportExcelToCsv_obj.Excel_to_csv(current_excel_href,filenamevalue)

    

    # store the data in blob storage
    AzureBlobStoage_obj=AzureBlobStoage()
    response_value=AzureBlobStoage_obj.LocalToBlob(export_csv,filenamevalue)

    print(response_value)

except Exception as e:
    exception_obj=ExceptionProcedure()
    value=str(e)
    print(value)
    exception_value=exception_obj.Execution_procedure(value)
    print(exception_value)


