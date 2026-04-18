from src.main.models.all_modals import Home, HomeType

def calculate_raw_material_cost(length_of_land: float, breadth_of_land: float, floor: int, home_type: HomeType, config):
    height = 10
    wall_thickness = 0.5
    
    # Room count can be used for advanced calculations if needed
    # room_count_map = {
    #     "two_bhk": 2,
    #     "three_bhk": 3,
    #     "four_bhk": 4
    # }
    
    total_wall_area = 2 * (length_of_land + breadth_of_land) * height * floor
    bricks_volume = total_wall_area * length_of_land * breadth_of_land
    bricks_needed = bricks_volume / 0.001125
    
    brick_cost = bricks_needed * config.getfloat("raw_materials", "brick_cost")
    cement_cost = (total_wall_area / 10) * config.getfloat("raw_materials", "cement_cost")
    sand_cost = (total_wall_area / 20) * config.getfloat("raw_materials", "sand_cost")
    
    total_raw_material_cost = brick_cost + cement_cost + sand_cost
    return total_raw_material_cost
    
    
    
    
def calculate_labour_cost(floor: int = 1, home_type: HomeType = None):
    labour_rate_map = {
        "two_bhk": {
            "foundation": 15000,
            "structure": 25000,
            "finishing": 20000
        },
        "three_bhk": {
            "foundation": 18000,
            "structure": 30000,
            "finishing": 25000
        },
        "four_bhk": {
            "foundation": 20000,
            "structure": 35000,
            "finishing": 30000
        }
    }
    
    # Default to two_bhk if not provided
    home_type_str = home_type.value if home_type else "two_bhk"
    rates = labour_rate_map.get(home_type_str, labour_rate_map["two_bhk"])
    
    # Calculate per phase labour cost
    foundation_cost = rates["foundation"] * floor
    structure_cost = rates["structure"] * floor
    finishing_cost = rates["finishing"] * floor
    
    # Add complexity multiplier based on floors
    complexity_multiplier = 1 + (floor - 1) * 0.15
    
    total_labour_cost = (foundation_cost + structure_cost + finishing_cost) * complexity_multiplier
    return total_labour_cost
    
def calculate_interior_cost(length_of_land: float, breadth_of_land: float, floor: int = 1, home_type: HomeType = None):
    area = length_of_land * breadth_of_land
    
    interior_cost_map = {
        "two_bhk": {
            "flooring": 40,
            "painting": 15,
            "fixtures": 35,
            "electrical": 25
        },
        "three_bhk": {
            "flooring": 45,
            "painting": 18,
            "fixtures": 40,
            "electrical": 30
        },
        "four_bhk": {
            "flooring": 50,
            "painting": 20,
            "fixtures": 45,
            "electrical": 35
        }
    }
    
    # Default to two_bhk if not provided
    home_type_str = home_type.value if home_type else "two_bhk"
    costs = interior_cost_map.get(home_type_str, interior_cost_map["two_bhk"])
    
    # Calculate individual components
    flooring_cost = area * costs["flooring"] * floor
    painting_cost = area * costs["painting"] * floor
    fixtures_cost = area * costs["fixtures"] * floor
    electrical_cost = area * costs["electrical"] * floor
    
    # Add premium for higher floors
    floor_premium = 1 + (floor - 1) * 0.10
    
    total_interior_cost = (flooring_cost + painting_cost + fixtures_cost + electrical_cost) * floor_premium
    return total_interior_cost
    