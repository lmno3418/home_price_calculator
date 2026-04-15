from loguru import logger
from src.main.databases.mysql_connector import *
from src.main.utility.encrypt_decrypt import decrypt
from src.main.factories.person_factory import PersonFactory
from src.main.services.labour_service import LabourService
from src.main.services.attendance_service import AttendanceService

import configparser
import os

config = configparser.ConfigParser()
config.read("src/resources/config_file.ini")

config.set("mysql_database", "user", decrypt(config["mysql_database"]["user"]))
config.set("mysql_database", "password", decrypt(config["mysql_database"]["password"]))
config.set("mysql_database", "database", decrypt(config["mysql_database"]["database"]))


db = MySqlConnection.get_instance(config)
logger.info(f"Db connection {db}")

# Function to create a new labour dynamically
def create_user(first_name, last_name, wage, role):
    labour = PersonFactory.create_person("labour", first_name=first_name, last_name=last_name, wage=wage, role=role)
    logger.info(f"Value of labour object {labour}")
    labour_service = LabourService(db.connection)
    labour_id = labour_service.create_labour(labour)
    return labour_id

# Function to handle login/logout
def login_logout(labour_id=None, first_name=None, last_name=None):
    attendance_service = AttendanceService(db.connection)
    attendance_service.login_logout(labour_id, first_name, last_name)
    return "Attendance recorded successfully."


# result = create_user("manish", "kumar", 500, "helper")
# logger.info(f"Labour added with Id {result}")
# print(login_logout(first_name="manish", last_name="kumar"))