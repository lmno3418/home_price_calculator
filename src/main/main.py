from src.main.Databases.mysqlcon import *

import loguru


logger = loguru.logger

import configparser

config = configparser.ConfigParser()
config.read('/Users/lmno3418/Documents/PROJECTS/project1/src/resources/config.ini')

def main():
    
    mysql_connection = MySQLConnection(config)
    connection = mysql_connection.connect()        #establishing connection to MySQL database using the MySQLConnection class
    
    crud_operations = MysqlCrudOperations(connection)        #creating an instance of the MysqlCrudOperations class to perform CRUD operations on the MySQL database
    
    query = "SELECT * FROM labours_table;"                #example query to fetch all records from the labours_table
    result = crud_operations.read_from_mysql(query)      #executing the query using the read_from_mysql method of the MysqlCrudOperations class
    logger.info(result)                                   #logging the result of the query execution
    
    mysql_connection.close()                       #closing the MySQL connection 
    
     
if __name__ == "__main__":
    main()