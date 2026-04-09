from src.main.Databases.mysqlcon import *

import loguru


logger = loguru.logger

import configparser

config = configparser.ConfigParser()
config.read('/Users/lmno3418/Documents/PROJECTS/PythonProject/src/resources/config.ini')

def main():
    query="select * from labours_table;"
    result = read_from_mysql(config=config, query=query)         #example of executing a query using the read_from_mysql function
    logger.info(result)
    
     
if __name__ == "__main__":
    main()