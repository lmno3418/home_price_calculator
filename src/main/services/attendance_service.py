from datetime import datetime
from loguru import logger

class AttendanceService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def login_logout(self, labour_id=None, first_name=None, last_name=None):
        cursor = self.db_connection.cursor()

        if labour_id is None:
            if first_name is None or last_name is None:
                logger.error("Please provide either labour_id or first_name and last_name")
                return

            query = """
                    SELECT id FROM labours
                    WHERE LOWER(first_name) = %s
                    AND LOWER(last_name) = %s
                    """
            try:
                cursor.execute(query, (first_name.lower(), last_name.lower()))
                result = cursor.fetchall()  # Fetch result here
                if not result:
                    logger.error("Please register yourself. No entry found.")
                    raise ValueError("Labour not registered")
                labour_id = result[0][0]
                logger.info(f"Labour ID retrieved: {labour_id}")
            except Exception as e:
                logger.error(f"Error occurred: {e}")
                raise

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Ensure previous query results are fully read before running a new query
        logger.info(f"Current date {current_date} and labour_id {labour_id}")
        check_query = """
            SELECT id, start_time, end_time FROM attendance
            WHERE labour_id = %s AND DATE(start_time) = %s
        """
        cursor.execute(check_query, (labour_id, current_date))
        result = cursor.fetchone()
        logger.info(f"Attendance record found: {result}")

        if not result:
            insert_query = """
                INSERT INTO attendance (labour_id, start_time)
                VALUES (%s, %s)
            """
            cursor.execute(insert_query, (labour_id, current_time))
            logger.info(f"Labour {labour_id} logged in at {current_time}")
        else:
            attendance_id = result[0]
            update_query = """
                UPDATE attendance
                SET end_time = %s
                WHERE id = %s
            """
            cursor.execute(update_query, (current_time, attendance_id))
            logger.info(f"Labour {labour_id} logged out at {current_time}")

        self.db_connection.commit()
        cursor.close()
