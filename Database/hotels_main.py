import pandas as pd
from mysql_api import create_hotel_income, batch_create_hotel_income, update_hotel_income, read_hotel_income, batch_read_hotel_income, delete_hotel_income

def batch_write_from_file(filename):
    try:
        df = pd.read_excel(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Make sure the file exists.")
        return
    
    success = batch_create_hotel_income(df, filename)
    
    if success:
        print(f"Records from {filename} have been added to the database.\n")
    else:
        print(f"Failed to add record for {filename} to the database.")

def write_record(room_kind, occupancy_percentage, monthly_income):
    success = create_hotel_income(room_kind, occupancy_percentage, monthly_income)
    
    if success:
        print(f"Record for {room_kind} added to the database.")
    else:
        print(f"Failed to add record for {room_kind} to the database.")

def update_record(record_id, occupancy_percentage, monthly_income):
    success = update_hotel_income(record_id, occupancy_percentage, monthly_income)
    
    if success:
        print(f"Record with ID {record_id} updated.")
    else:
        print(f"Failed to update record with ID {record_id}.")

def read_record(record_id):
    record = read_hotel_income(record_id)
    
    if record:
        print(record)
    else:
        print("No record {record_id} found in the database.")

def read_all_records():
    records = batch_read_hotel_income()
    if records:
        for record in records:
            print(record)
    else:
        print("No records found in the database.")

def delete_record(record_id):
    success = delete_hotel_income(record_id)
    
    if success:
        print(f"Record with ID {record_id} deleted.")
    else:
        print(f"Failed to delete record with ID {record_id}.")

def export_table(filename, kind):
    records = batch_read_hotel_income()
    if records:
        data = {
            'ID': [record.id for record in records],
            'Month-Year': [record.Month_Year for record in records],
            'Kind Room': [record.Kind_Room for record in records],
            'Monthly Room Profit': [record.Monthly_Room_Profit for record in records],
            'Total Rooms': [record.Total_Rooms for record in records],
            'Occupied Rooms': [record.Occupied_Rooms for record in records],
            '% Occupation': [record.Occupation_Percentage for record in records],
            'Total Monthly Profit': [record.Total_Monthly_Profit for record in records],
        }
        df = pd.DataFrame(data)
        if kind == 'csv':
            df.to_csv('../Data/' + filename + '.csv', index=False)
        if kind == 'excel':
            df.to_excel('../Data/' + filename + '.xlsx', index=False)
        print(f"Data exported to '{filename}'.")
    else:
        print("No records found in the database.")


batch_write_from_file('../Data/Hotel_Profit_Analysis.xlsx')

# write_record('04/2023', 'AABB / AABB', '125000', '140', '66', '0.4714', '125000')
# update_record(1, '08/2022', 'AABB / AABB', '125000', '140', '66', '0.4714', '125000')

read_record(12)

# read_all_records()
# delete_record(1)

export_table('Hotel_Profit_Export_CSV', 'csv')
export_table('Hotel_Profit_Export_EXCEL', 'excel')