import pandas
import csv
from pymongo import MongoClient
import random

mongo_str = "mongodb+srv://hdrproject:50230@cluster0.ktm1unb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_str)

db = client.HDRProjecct
datas = db.historiess

box_code = []

ran_str = ''
for i in range(100):
    for n in range(5):
        ran_num = random.randint(0,9)
        ran_str += str(ran_num)
    box_code.append(ran_str)
    ran_str = ''


print(box_code)
run = True
while run:
    StudentNumber = int(input("12345 : "))
    if StudentNumber == 0:
        print("end")
        break
    StudentName = input("Name : ").strip()
    Room = int(input("Room 601 : "))
    Number = int(input("Number 1 2 3 16 : "))
    Symptom = input("ปวดหัว มีไข้ ท้องเสีย ปวดประจำเดือน ลมพิษ/แพ้ : ") .strip()
    Age = int(input("Age"))
    Weight = float(input("weight"))
    Cause = input("อาการที่พบ : ").strip()
    Range = int(input("ระดับความปวด"))
    Temp = float(input("Temp : "))
    Date_poo = input("Date poo dd/mm/yyyy 03/05/2566 : ").strip()
    time_poo = input("Time poo dd/mm/yyyy 03/05/2566 : ").strip()
    poo_time = int(input("ถ่ายมาแล้วกี่ครั้ง : "))
    Serial = int(input())
    SendStatus = bool(input("True : "))
    Sendby = input("อนุมัติโดยระบบ/อนุมัติโดยครู : ").strip()
    Time = input("time AM/PM 09:30 AM :").strip()
    date = input("Date dd/mm/yyyy 03/05/2566 : ").strip()

    data = {
        "StudentNumber":StudentNumber,
        "StudentName":StudentName,
        "Room":Room,
        "Number":Number,
        "Symptom":Symptom,
        "Age":Age,
        "Weight":Weight,
        "Cause":Cause,
        "Range":Range,
        "Temp":Temp,
        "Date_poo":Date_poo,
        "time_poo":time_poo,
        "poo_time":poo_time,
        "Detail":{
            "Serial":Serial,
            "SendStatus":SendStatus,
            "Sendby":Sendby,
            "Time":Time,
            "date":date
        }
    }

    datas.insert_one(data)