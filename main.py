from pymongo import MongoClient
import random

IDPASS = "" #hdrproject:50230
mongo_str = f"mongodb+srv://{IDPASS}@cluster0.ktm1unb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_str)

db = client.HDRProjecct
datas = db.studentdatas
insertdatas = db.historiess

Symptom_box = ["ปวดหัว", "มีไข้", "ท้องเสีย", "ปวดประจำเดือน", "ลมพิษ"]


def up_to_db(data):
    print("Update data to DataBase Wait a Second...")
    insertdatas.insert_one(data)
    print("Done")


def gen_serial():
    ran_box = ''
    for i in range(5):
        ran_box += str(random.randint(0,9))
    return ran_box


def detail(Sendby):
    Detail = {
    "Serial":int(gen_serial()),
        "SendStatus":True,
        "Sendby":Sendby,
        "Time":Time,
        "date":Date
    }
    return Detail


def headmen(Symptom):
    headmen = {
    "StudentNumber":Student_Number,
    "StudentName":student_data_name,
    "Room":int(student_data_room),
    "Number":int(student_data_number),
    "Symptom":Symptom,
    "Age":int(Age),
    "Weight":float(Weight),
    "Cause":Cause,
    "Range":int(Range),
    }
    return headmen


def urticaria(Symptom):
    urticaria = {
    "StudentNumber":Student_Number,
    "StudentName":student_data_name,
    "Room":int(student_data_room),
    "Number":int(student_data_number),
    "Symptom":Symptom,
    "Age":int(Age),
    "Weight":float(Weight),
    "Cause":Cause,
    }
    return urticaria


def fever(Symptom):
    fever = {
    "StudentNumber":Student_Number,
    "StudentName":student_data_name,
    "Room":int(student_data_room),
    "Number":int(student_data_number),
    "Symptom":Symptom,
    "Age":int(Age),
    "Weight":float(Weight),
    "Cause":Cause,
    "Temp":float(Temp),
    }
    return fever


def diarrhea(Symptom):
    diarrhea = {
    "StudentNumber":Student_Number,
    "StudentName":student_data_name,
    "Room":int(student_data_room),
    "Number":int(student_data_number),
    "Symptom":Symptom,
    "Age":int(Age),
    "Weight":float(Weight),
    "Date_poo":Date_poo,
    "Time_poo":Time_poo,
    "Poo_Time":Poo_time,
    }
    return diarrhea


try:
    print("\n=============================")
    print("\nStart The Program!")
    while True:

        Student_Number = int(input("StudentNumber is : "))
        print("Searching for StudentName by StudentNumber, pls wait a second...")
        student_data_name = datas.find_one({"StudentNumber":Student_Number})["StudentName"]
        student_data_room = datas.find_one({"StudentNumber":Student_Number})["Room"]
        student_data_number = datas.find_one({"StudentNumber":Student_Number})["Number"]

        Symptom = int(input("1.ปวดหัว 2.มีไข้ 3.ท้องเสีย 4.ปวดประจำเดือน 5.ลมพิษ/แพ้ : "))
        Age = int(input("Age is : "))
        Weight = float(input("Weight is : "))
        Date = input("Date is : ")
        Time = input("Time is : ")


        if Symptom == 1:
            print(f"Symptom is : '{Symptom_box[Symptom-1]}' "),
            Cause = input("Cause is : ")
            Range = int(input("Range is : "))
            Sendby = "อนุมัติโดยครู"
            data = headmen(Symptom_box[Symptom-1])
            data.update({"Detail":detail(Sendby)})
            up_to_db(data)

        elif Symptom == 2:
            print(f"Symptom is : '{Symptom_box[Symptom-1]}' "),
            Cause = input("Cause is : ")
            Temp = float(input("Temp is : "))
            if Temp >= 38:
                Sendby = "อนุมัติโดยระบบ"
            else:
                Sendby = "อนุมัติโดยครู"
            data = fever(Symptom_box[Symptom-1])
            data.update({"Detail":detail(Sendby)})
            up_to_db(data)

        elif Symptom == 3:
            print(f"Symptom is : '{Symptom_box[Symptom-1]}' "),
            Date_poo = input("Date_poo is : ")
            Time_poo = input("Time_poo is : ")
            Poo_time = int(input("Poo_time is : "))
            Sendby = "อนุมัติโดยครู"
            data = diarrhea(Symptom_box[Symptom-1])
            data.update({"Detail":detail(Sendby)})
            up_to_db(data)

        elif Symptom == 4:
            print(f"Symptom is : '{Symptom_box[Symptom-1]}' "),
            Cause = input("Cause is : ")
            Range = int(input("Range is : "))
            Sendby = "อนุมัติโดยครู"
            data = headmen(Symptom_box[Symptom-1])
            data.update({"Detail":detail(Sendby)})
            up_to_db(data)

        elif Symptom == 5:
            print(f"Symptom is : '{Symptom_box[Symptom-1]}' "),
            Cause = input("Cause is : ")
            Sendby = "อนุมัติโดยครู"
            data = urticaria(Symptom_box[Symptom-1])
            data.update({"Detail":detail(Sendby)})
            up_to_db(data)


except KeyboardInterrupt as k:
    print("\n=============================")
    print(f"\n[System] : See You Next Time")
    print("\n=============================")


except Exception as e:
    print("\n============Error============")
    print(f"\nerror is : {e}")
    print("\n=============================")