from enum import Enum

from pydantic import BaseModel, Field
from typing import Any, Optional

class User(BaseModel):
    first_name: str=Field(examples=["John"])
    last_name: str=Field(examples=["Doe"])
    wage: float=Field(default=500, examples=[500])
    role: Optional[str]=Field(default="labour", examples=["labour"])
    skills: Optional[list[str]]=Field(default=None, examples=[["carpentry", "plumbing"]])
    
class UIResponse(BaseModel):
    status: str
    status_code: Optional[int] = None
    data: Any
    message: Optional[str] = None

class Attendance(BaseModel):
    labour_id: int=Field(examples=[1])
    first_name: str=Field(examples=["John"])
    last_name: str=Field(examples=["Doe"])
    
class HomeType(str, Enum):
    two_bhk = "two_bhk"
    three_bhk = "three_bhk"
    four_bhk = "four_bhk"
    
class Home(BaseModel):
    home_type: HomeType=Field(examples=["two_bhk"])
    length_of_land: float = Field(gt=0, description="Length of the land in feet", examples=[50])
    breadth_of_land: float = Field(gt=0, description="Breadth of the land in feet", examples=[30])
    floor: int = Field(default=1, ge=1, description="Number of floors", examples=[2])
    