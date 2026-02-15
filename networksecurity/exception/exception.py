import sys
import logging

class NetworkSecurityException(Exception):
    

    def __init__(self, message: str, error_details: sys):
        
        self.message = message
        _,_,exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno

    def __str__(self):
        logging.error(f"Error occured in [{self.file_name}] line number [{self.line_number}] and error msg[{str(self.message)}]:")
        return f"Error occured in [{self.file_name}] line number [{self.line_number}] and error msg[{str(self.message)}]:"
    

if __name__ == "__main__":
    try:
        logging.info("Testing NetworkSecurityException")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityException(e, sys)