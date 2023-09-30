from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class HotelProfit(Base):
    __tablename__ = 'Hotel_Profit'
    
    id = Column(Integer, primary_key=True)
    Month_Year = Column(String(50))
    Kind_Room = Column(String(50)) 
    Monthly_Room_Profit = Column(String(50))
    Total_Rooms = Column(String(50))
    Occupied_Rooms = Column(String(50))
    Occupation_Percentage = Column(String(50))
    Total_Monthly_Profit = Column(String(50))
    
    def __init__(self, Month_Year, Kind_Room, Monthly_Room_Profit, Total_Rooms, Occupied_Rooms, Occupation_Percentage, Total_Monthly_Profit):
        self.Month_Year = Month_Year
        # self.Month_Year = datetime.strptime(f"01/{Month_Year}", '%d/%m/%Y').date()
        self.Kind_Room = Kind_Room
        self.Monthly_Room_Profit = Monthly_Room_Profit
        self.Total_Rooms = Total_Rooms
        self.Occupied_Rooms = Occupied_Rooms
        self.Occupation_Percentage = Occupation_Percentage
        self.Total_Monthly_Profit = Total_Monthly_Profit
    def __repr__(self):
        return f"\nHotelProfit(id = {self.id},\
    \nMonth_Year = {self.Month_Year},\
    \nKind_Room = {self.Kind_Room},\
    \nMonthly_Room_Profit = {self.Monthly_Room_Profit},\
    \nTotal_Rooms = {self.Total_Rooms},\
    \nOccupied_Rooms = {self.Occupied_Rooms},\
    \nOccupation_Percentage = {self.Occupation_Percentage},\
    \nTotal_Monthly_Profit = {self.Total_Monthly_Profit})\n"