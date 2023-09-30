from sqlalchemy.exc import SQLAlchemyError
from models import HotelProfit
from db_login import MySQL
from dotenv import load_dotenv
import os

load_dotenv('mysql.env')
db_url = os.getenv('DB_URL')

if db_url is None:
    raise ValueError("DB_URL environment variable is not set")

database_boot = MySQL(database_url=db_url)
tables = [HotelProfit]
database_boot.create_tables(tables)

db_conn = database_boot.get_conn()

def create_hotel_income(Month_Year, Kind_Room, Monthly_Room_Profit, Total_Rooms, Occupied_Rooms, Occupation_Percentage, Total_Monthly_Profit):
    try:
        new_record = HotelProfit(
            Month_Year = Month_Year,
            Kind_Room = Kind_Room,
            Monthly_Room_Profit = Monthly_Room_Profit,
            Total_Rooms = Total_Rooms,
            Occupied_Rooms = Occupied_Rooms,
            Occupation_Percentage = Occupation_Percentage,
            Total_Monthly_Profit = Total_Monthly_Profit
        )
        db_conn.add(new_record)
        db_conn.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error creating record: {e}")
        db_conn.rollback()
        return False

def batch_create_hotel_income(data_file, filename):
    try:
        for index, row in data_file.iterrows():
            Month_Year = row['Month-Year']
            Kind_Room = row['Kind Room']
            Monthly_Room_Profit = row['Monthly Room Profit']
            Total_Rooms = row['Total Rooms']
            Occupied_Rooms = row['Occupied Rooms']
            Occupation_Percentage = row['% Occupation']
            Total_Monthly_Profit = row['Total Monthly Profit']
            
            hotel_income = HotelProfit(
                Month_Year = Month_Year,
                Kind_Room = Kind_Room,
                Monthly_Room_Profit = Monthly_Room_Profit,
                Total_Rooms = Total_Rooms,
                Occupied_Rooms = Occupied_Rooms,
                Occupation_Percentage = Occupation_Percentage,
                Total_Monthly_Profit = Total_Monthly_Profit
            )
            
            db_conn.add(hotel_income)
            
            try:
                db_conn.commit()
                print(f"Record for {index} added to the database.")
            except Exception as e:
                db_conn.rollback()
                print(f"Failed to add record for {index} to the database due to integrity error.\n {e}")
        return True
    
    except SQLAlchemyError as e:
        print(f"Error creating records from file: {e}")
        db_conn.rollback()
        return False
    

def batch_read_hotel_income():
    try:
        records = db_conn.query(HotelProfit).all()
        return records
    except SQLAlchemyError as e:
        print(f"Error reading records: {e}")
        return []

def read_hotel_income(record_id):
    try:
        record = db_conn.query(HotelProfit).filter_by(id=record_id).first()
        return record
    except SQLAlchemyError as e:
        print(f"Error reading record by ID: {e}")
        return None

def update_hotel_income(record_id, Month_Year, Kind_Room, Monthly_Room_Profit, Total_Rooms, Occupied_Rooms, Occupation_Percentage, Total_Monthly_Profit):
    try:
        record = db_conn.query(HotelProfit).filter_by(id=record_id).first()
        if record:
            record.Month_Year = Month_Year,
            record.Kind_Room = Kind_Room,
            record.Monthly_Room_Profit = Monthly_Room_Profit,
            record.Total_Rooms = Total_Rooms,
            record.Occupied_Rooms = Occupied_Rooms,
            record.Occupation_Percentage = Occupation_Percentage,
            record.Total_Monthly_Profit = Total_Monthly_Profit
            db_conn.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        print(f"Error updating record: {e}")
        db_conn.rollback()
        return False

def delete_hotel_income(record_id):
    try:
        record = db_conn.query(HotelProfit).filter_by(id=record_id).first()
        if record:
            db_conn.delete(record)
            db_conn.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        print(f"Error deleting record: {e}")
        db_conn.rollback()
        return False