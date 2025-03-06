import mysql.connector
from .config import Config

def get_db_connection():
    connection = mysql.connector.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )
    return connection

def check_email_exists(email):
    """check if the email exists"""
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result is not None

def get_user_data_by_email(email):
    """get user data by email"""
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT email, name, permission FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return {'email': result[0], 'name': result[1], 'permission': result[2]}
    return None

def get_all_room_data():
    """get all room data"""
    connection = get_db_connection()
    cursor = connection.cursor()


def get_booking_record_of_a_room(room):
    """get booking record of a room"""
    connection = get_db_connection()
    cursor = connection.cursor()


def get_room_detailed(room):
    """get detailed room data"""
    connection = get_db_connection()
    cursor = connection.cursor()
    booking_details = get_booking_record_of_a_room(room)