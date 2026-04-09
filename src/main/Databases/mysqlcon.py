from loguru import logger

import mysql.connector

from src.main.encryp_decrypt import AES


def read_from_mysql(config,query):
    try:
        con = mysql.connector.connect(
            host=config["MySQL"]["host"],
            user=AES.decrypt(config["MySQL"]["user"]),       #encrypted value in config.ini, decrypted using AES.py
            password=AES.decrypt(config["MySQL"]["password"]),       #encrypted value in config.ini, decrypted using AES.py
            database=AES.decrypt(config["MySQL"]["database"])        #encrypted value in config.ini, decrypted using AES.py
        )


        # logger.info(f"{con}")       #check connection

        cur = con.cursor()          #creating cursor object to execute SQL queries

        cur.execute(query)         #executing query
        result = cur.fetchall()                             #fetching all results from the executed query

        # logger.info(result)                                 #logging the results to check if the query was executed successfully
        return result
    
    except Exception as e:
        logger.error(f"Error occurred in MySQL. Details: {e}")
        raise e
    
    finally:
        if 'cur' in locals():
            cur.close()
        if 'con' in locals():
            con.close()
        logger.info("MySQL cursor & connection closed.")