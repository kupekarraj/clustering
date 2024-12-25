import sys
from src.logger import logging

def error_message(error:Exception,error_detail:sys):
    """Generate detailed error messages with file name, line number, and error details."""
    _,_,exc_tb=error_detail.exc_info() # Get traceback object

    file_name = exc_tb.tb_frame.f_code.co_filename  # Filename where the error occurred
    line_number = exc_tb.tb_lineno  # Line number where the error occurred
    error_message = (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"with error message: [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    """Custom Exception class for handling and displaying detailed error messages."""
    
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        # Generate a detailed error message using the function
        self.error_message = error_message(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.error("Divide Zero Error")
        raise CustomException(e,sys)
        