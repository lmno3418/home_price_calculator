from loguru import logger
from fastapi import FastAPI, HTTPException


from src.main.databases.mysql_connector import *
from src.main.utility.encrypt_decrypt import decrypt
from src.main.factories.person_factory import PersonFactory
from src.main.services.labour_service import LabourService
from src.main.services.attendance_service import AttendanceService
from src.main.models.all_modals import Home, User, UIResponse, Attendance
from src.main.services.cost_calculator import calculate_raw_material_cost, calculate_labour_cost, calculate_interior_cost

import configparser
import os

config = configparser.ConfigParser()
config.read("src/resources/config_file.ini")

config.set("mysql_database", "user", decrypt(config["mysql_database"]["user"]))
config.set("mysql_database", "password", decrypt(config["mysql_database"]["password"]))
config.set("mysql_database", "database", decrypt(config["mysql_database"]["database"]))


db = MySqlConnection.get_instance(config)
logger.info(f"Db connection {db}")





app = FastAPI(title="Home Cost Calculator", description="TO CALCULATE COST OF YOUR DREAM HOME")
                                
@app.get("/")
def read_root():
    return {"message": "Welcome to the Labour Management System API!"}

@app.post("/create_user/")
# Function to create a new labour dynamically
def create_user(user: User):
    try:
        labour = PersonFactory.create_person("labour", first_name=user.first_name, last_name=user.last_name, wage=user.wage, role=user.role)
        logger.info(f"Value of labour object {labour}")
        labour_service = LabourService(db.connection)
        labour_id = labour_service.create_labour(labour)
        return UIResponse(status="success", status_code=201, data={"labour_id": labour_id}, message=f"Labour added with Id {labour_id}")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")
    
    
@app.post("/create_mistri/")
def create_mistri(user: User):
    try:
        labour = PersonFactory.create_person("mistri", first_name=user.first_name, last_name=user.last_name, wage=user.wage, role=user.role, skills=user.skills)
        logger.info(f"Value of labour object {labour}")
        labour_service = LabourService(db.connection)
        labour_id = labour_service.create_mistri(labour)
        return UIResponse(status="success", status_code=201, data={"labour_id": labour_id}, message=f"Mistri added with Id {labour_id}")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")
    
    
@app.get("/get_labour_id/{labour_id}")
def get_labour_id(labour_id: int):
    try:
        labour_service = LabourService(db.connection)
        labour = labour_service.get_labour_by_id(labour_id)
        if not labour:
            raise HTTPException(status_code=404, detail="Labour not found")
        return UIResponse(status="success", status_code=200, data={"labour": labour}, message="Labour found")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")


@app.get("/get_labours/")
def get_labours():
    try:
        labour_service = LabourService(db.connection)
        labour = labour_service.get_all_labours()
        if not labour:
            raise HTTPException(status_code=404, detail="Labours not found")
        return UIResponse(status="success", status_code=200, data={"labour": labour}, message="Labours found")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")
    
    
@app.post("/home_price_estimate/")
def home_price_estimate(request: Home):
    try:
        rc = calculate_raw_material_cost(request.length_of_land, request.breadth_of_land, request.floor, request.home_type, config=config)
        lc = calculate_labour_cost(request.floor, request.home_type)
        ic = calculate_interior_cost(request.length_of_land, request.breadth_of_land, request.floor, request.home_type)
        total_cost = rc + lc + ic
        return UIResponse(status="success", status_code=200, data={"raw_material_cost": rc, "labour_cost": lc, "interior_cost": ic, "total_cost": total_cost}, message="Home price estimate calculated successfully")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")


@app.post("/attendance/")
# Function to handle attendance
def record_attendance(attendance: Attendance):
    try:
        attendance_service = AttendanceService(db.connection)
        attendance_service.login_logout(attendance.labour_id, attendance.first_name, attendance.last_name)
        return UIResponse(status="success", status_code=200, data=None, message="Attendance recorded successfully.")
    except Exception as e:
        return UIResponse(status="error", status_code=500, data=None, message=f"Error occurred: {str(e)}")


# result = create_user("manish", "kumar", 500, "helper")
# logger.info(f"Labour added with Id {result}")
# print(login_logout(first_name="manish", last_name="kumar"))

# if __name__ == "__main__":
    # pass