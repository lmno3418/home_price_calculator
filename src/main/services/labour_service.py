from fastapi import HTTPException

class LabourService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_labour(self, labour):
        cursor = self.db_connection.cursor()

        check_query = """
        SELECT id FROM labours WHERE LOWER(first_name) = %s AND LOWER(last_name) = %s
        """
        cursor.execute(check_query, (labour.first_name.lower(), labour.last_name.lower()))
        result = cursor.fetchone()
        
        if result:
            raise HTTPException(status_code=400, detail="User is already present")
        
        query = """
        INSERT INTO labours (first_name, last_name, wage, role, email)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (labour.first_name, labour.last_name, labour.wage, labour.role, labour.email)
        cursor.execute(query, values)
        self.db_connection.commit()
        return cursor.lastrowid
    
    def create_mistri(self, mistri):
        cursor = self.db_connection.cursor()

        check_query = """
        SELECT id FROM labours WHERE LOWER(first_name) = %s AND LOWER(last_name) = %s
        """
        cursor.execute(check_query, (mistri.first_name.lower(), mistri.last_name.lower()))
        result = cursor.fetchone()
        
        if result:
            raise HTTPException(status_code=400, detail="User is already present")
        
        query = """
        INSERT INTO labours (first_name, last_name, wage, role, email)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        query2 = """
        INSERT INTO skills (labour_id, skill)
        VALUES (%s, %s)
        """
        
        values = (mistri.first_name, mistri.last_name, mistri.wage, mistri.role, mistri.email)
        cursor.execute(query, values)
        self.db_connection.commit()
        
        mistri_id = cursor.lastrowid
        if mistri.skills:
            for skill in mistri.skills:
                cursor.execute(query2, (mistri_id, skill))  
            
        self.db_connection.commit()
        return mistri_id
    
    def get_labour_by_id(self, labour_id):
        cursor = self.db_connection.cursor()
        query = "SELECT id, first_name, last_name, wage, role, email FROM labours WHERE id = %s"
        cursor.execute(query, (labour_id,))
        result = cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "wage": result[3],
                "role": result[4],
                "email": result[5]
            }
        else:
            raise HTTPException(status_code=404, detail="Labour not found")
        
    def get_all_labours(self):
        cursor = self.db_connection.cursor()
        query = "SELECT id, first_name, last_name, wage, role, email FROM labours"
        cursor.execute(query)
        results = cursor.fetchall()
        labours = []
        for result in results:
            labours.append({
                "id": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "wage": result[3],
                "role": result[4],
                "email": result[5]
            })
        return labours
    