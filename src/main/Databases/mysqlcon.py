from loguru import logger

import mysql.connector

from src.main.encryp_decrypt import AES

class MySQLConnection:
    def __init__(self, config):
        self.config = config

    def connect(self):
        try:
            self.con = mysql.connector.connect(
                host=self.config["MySQL"]["host"],
                user=AES.decrypt(self.config["MySQL"]["user"]),               #encrypted value in config.ini, decrypted using AES.py
                password=AES.decrypt(self.config["MySQL"]["password"]),       #encrypted value in config.ini, decrypted using AES.py
                database=AES.decrypt(self.config["MySQL"]["database"])        #encrypted value in config.ini, decrypted using AES.py
            )
            logger.info("MySQL connection established successfully.")
            return self.con
        
        except Exception as e: 
            logger.error(f"Error occurred while connecting to MySQL. Details: {e}")
            raise e
        
    def close(self):
        try:
            if hasattr(self, 'con') and self.con.is_connected():
                self.con.close()
                logger.info("MySQL connection closed successfully.")
        except Exception as e:
            logger.error(f"Error occurred while closing MySQL connection. Details: {e}")
            raise e    
        
        
class MysqlCrudOperations:
    def __init__(self, connection):
        self.connection = connection
        
    def read_from_mysql(self, query):
        try:
            if self.connection.is_connected():
                cur = self.connection.cursor()
                cur.execute(query)
                result = cur.fetchall()
                cur.close()
                return result
            else:
                raise Exception("MySQL connection is not established.")
        except Exception as e:
            logger.error(f"Error occurred while executing query. Details: {e}")
            raise e
        
    def write_to_mysql(self, query):
        try:
            if self.connection.is_connected():
                cur = self.connection.cursor()
                cur.execute(query)
                self.connection.commit()
                cur.close()
                logger.info("Data written to MySQL successfully.")
            else:
                raise Exception("MySQL connection is not established.")
        except Exception as e:
            logger.error(f"Error occurred while executing query. Details: {e}")
            raise e
        
    def update_mysql(self, query):
        try:
            if self.connection.is_connected():
                cur = self.connection.cursor()
                cur.execute(query)
                self.connection.commit()
                cur.close()
                logger.info("Data updated in MySQL successfully.")
            else:
                raise Exception("MySQL connection is not established.")
        except Exception as e:
            logger.error(f"Error occurred while executing query. Details: {e}")
            raise e
        
    def delete_from_mysql(self, query):
        try:
            if self.connection.is_connected():
                cur = self.connection.cursor()
                cur.execute(query)
                self.connection.commit()
                cur.close()
                logger.info("Data deleted from MySQL successfully.")
            else:
                raise Exception("MySQL connection is not established.")
        except Exception as e:
            logger.error(f"Error occurred while executing query. Details: {e}")
            raise e
        
    def execute_query(self, query):
        try:
            if self.connection.is_connected():
                cur = self.connection.cursor()
                cur.execute(query)
                result = cur.fetchall()
                cur.close()
                return result
            else:
                raise Exception("MySQL connection is not established.")
        except Exception as e:
            logger.error(f"Error occurred while executing query. Details: {e}")
            raise e
        

