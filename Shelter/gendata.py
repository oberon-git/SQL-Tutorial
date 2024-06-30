import pandas as pd
import random
import datetime

df = pd.read_csv("https://raw.githubusercontent.com/jalapic/rblog/master/raw_data/Austin_Animal_Center_Intakes.csv")

data = {}
i = 0
for _, row in df.iterrows():
    if row["Name"] != "" and str(row["Name"]) != "nan":
        i += 1
        try:
            if "Female" in row["Sex upon Intake"]:
                gender_id = 1
            elif "Male" in row["Sex upon Intake"]:
                gender_id = 2
            else:
                gender_id = random.randint(1, 2)
        except:
            gender_id = random.randint(1, 2)
        data[i] = {
            "Name": row["Name"].replace("*", "").replace("'", "''"),
            "GenderId": gender_id
        }

cats = []
cat_biometrics = []
cat_shelter_reasons = []
cat_adoptions = []

def get_rand_date():
    while True:
        try:
            td = datetime.datetime.now()
            if random.randint(0, 3) == 0:
                td = td.replace(year = td.year - random.randint(1, 6))
            if random.randint(0, 1):
                m = random.randint(1, 11)
                if m >= td.month:
                    m -= td.month
                    td = td.replace(year = td.year - 1)
                td = td.replace(month = td.month - m)
            if random.randint(0, 1):
                d = random.randint(1, 29)
                if d >= td.day:
                    d -= td.day
                    td = td.replace(month = td.month - 1)
                td = td.replace(day = td.day - d)
            td = td.replace(hour = random.randint(0, 23))
            td = td.replace(minute = random.randint(0, 59))
            return td
        except:
            pass


data = [(x, y) for x, y in data.items()]
random.shuffle(data)
for cat_id, d in data: #random.shuffle([(x[0], x[1]) for x in data.items()]):
    cats.append({
        "CatId": cat_id,
        "CatTypeId": random.randint(1, 10),
        "CatName": d["Name"]
    })

    birth = get_rand_date()
    cat_biometrics.append({
        "CatBiometricId": len(cat_biometrics) + 1,
        "CatId": cat_id,
        "GenderId": d["GenderId"],
        "DateOfBirth": birth.strftime("%x %X")
    })

    cat_shelter_reasons.append({
        "CatShelterReasonId": len(cat_shelter_reasons) + 1,
        "CatId": cat_id,
        "CatShelterReasonTypeId": random.randint(1, 5),
    })

    if random.randint(0, 10) == 0:
        adop = get_rand_date()
        while adop < birth:
            adop = get_rand_date()
        cat_adoptions.append({
            "CatAdoptionId": len(cat_adoptions) + 1,
            "CatId": cat_id,
            "CatAdoptionDate": adop.strftime("%x %X"),
            "AmountPaid": random.random() * 200
        })


insert_smt = "INSERT INTO dbo.Cat (CatId, CatTypeId, CatName)\nVALUES\n"
sql_str = "USE Shelter\nGO\n"
cats = sorted(cats, key=lambda x: x["CatId"])
for i, cat in enumerate(cats):
    if i % 999 == 0:
        sql_str += "\n" + insert_smt
    else:
        sql_str += ",\n"
    sql_str += "(" + str(cat["CatId"]) + ", " + str(cat["CatTypeId"]) + ", '" + str(cat["CatName"]) + "')"
sql_str += "\n"
with open("Insert_Cats.sql", "w") as f:
    f.write(sql_str)


insert_smt = "INSERT INTO dbo.CatBiometric (CatBiometricId, CatId, GenderId, DateOfBirth)\nVALUES\n"
sql_str = "USE Shelter\nGO\n"
cat_biometrics = sorted(cat_biometrics, key=lambda x: x["CatBiometricId"])
for i, cat in enumerate(cat_biometrics):
    if i % 999 == 0:
        sql_str += "\n" + insert_smt
    else:
        sql_str += ",\n"
    sql_str += "(" + str(cat["CatBiometricId"]) + ", " + str(cat["CatId"]) + ", " + str(cat["GenderId"]) + ", '" + str(cat["DateOfBirth"]) + "')"
sql_str += "\n"
with open("Insert_CatBiometrics.sql", "w") as f:
    f.write(sql_str)


insert_smt = "INSERT INTO dbo.CatShelterReason (CatShelterReasonId, CatId, CatShelterReasonTypeId)\nVALUES\n"
sql_str = "USE Shelter\nGO\n"
cat_shelter_reasons = sorted(cat_shelter_reasons, key=lambda x: x["CatShelterReasonId"])
for i, cat in enumerate(cat_shelter_reasons):
    if i % 999 == 0:
        sql_str += "\n" + insert_smt
    else:
        sql_str += ",\n"
    sql_str += "(" + str(cat["CatShelterReasonId"]) + ", " + str(cat["CatId"]) + ", " + str(cat["CatShelterReasonTypeId"]) + ")"
sql_str += "\n"
with open("Insert_CatShelterReasons.sql", "w") as f:
    f.write(sql_str)


insert_smt = "INSERT INTO dbo.CatAdoption (CatAdoptionId, CatId, CatAdoptionDate, AmountPaid)\nVALUES\n"
sql_str = "USE Shelter\nGO\n"
cat_adoptions = sorted(cat_adoptions, key=lambda x: x["CatAdoptionId"])
for i, cat in enumerate(cat_adoptions):
    if i % 999 == 0:
        sql_str += "\n" + insert_smt
    else:
        sql_str += ",\n"
    sql_str += "(" + str(cat["CatAdoptionId"]) + ", " + str(cat["CatId"]) + ", '" + str(cat["CatAdoptionDate"]) + "', " + str(cat["AmountPaid"]) + ")"
sql_str += "\n"
with open("Insert_CatAdoptions.sql", "w") as f:
    f.write(sql_str)

print(len(cats), len(cat_biometrics), len(cat_shelter_reasons), len(cat_adoptions))