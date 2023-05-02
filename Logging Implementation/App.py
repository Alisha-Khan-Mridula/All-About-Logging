from flask import Flask 
import logging

app = Flask(__name__)

######## Logging ######

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# #### Error Messages ####
# error_handler = logging.FileHandler('error.log')
# error_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# error_handler.setFormatter(formatter)
# logger.addHandler(error_handler)



# # #### Warning Messages ####
# file_handler = logging.FileHandler('warning.log')
# file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# # #### Info #########
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('info.log')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)



# # ##### Debuging ######
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('debug.log')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)



# # ###### Critical #####
# logger.setLevel(logging.CRITICAL)
# file_handler = logging.FileHandler('critical.log')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)





####### Testing Messages ###########
# logger.info('This is the information')
# logger.critical('Critical situation has occured')
# logger.debug('Debugging')
# logger.error('An error has occure')
# logger.warning('Warning messages')










# Create a file handler for each log level and set the output file path
debug_handler = logging.FileHandler('debug.log')
info_handler = logging.FileHandler('info.log')
warning_handler = logging.FileHandler('warning.log')
error_handler = logging.FileHandler('error.log')
critical_handler = logging.FileHandler('critical.log')



# Set the logging level for each file handler
debug_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)
warning_handler.setLevel(logging.WARNING)
error_handler.setLevel(logging.ERROR)
critical_handler.setLevel(logging.CRITICAL)




# Create a formatter for each file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')




# Set the formatter for each file handler
debug_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
critical_handler.setFormatter(formatter)




# Add each file handler to the logger
logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)
logger.addHandler(critical_handler)



@app.route('/great/<name>')
def great(name):
    logger.warning('This is a warning message')
    return f'Hello {name}'



@app.route('/debugging')
def debugging():
    logger.debug('Debuggig')
    return "Let's do debugging" 


@app.route('/information')
def information():
    logger.info('Give some information')
    return "Give some information" 



@app.route('/criticalSituation')
def criticalSituation():
    logger.critical('This is a critical situation')
    return "This is a critical situation" 




@app.route('/divide/number/<number1>/<number2>')
def index(number1:int , number2:int):
    #logger.error("This is an error")
    return str(int(number1)/int(number2))



######### Middleware ############

# @app.before_request
# def beforeRequest():
#     pass

@app.teardown_request
def teardownRequest(exception):
    if exception is not None:
        logger.error( "RUNTIME ERROR :: " + str(exception)) 
        








if __name__ == "__main__":
    app.run(debug=True)