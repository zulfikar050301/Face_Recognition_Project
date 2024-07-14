import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facerecognitionfirst-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1104194019":
        {
            "name": "Zulfikar Salam",
            "major": "Physics Engineering",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "6",
            "year": 4,
            "las_attendance_time": "2022-12-11 00:54:34"
        },
    "16112001":
        {
            "name": "Azkia Khoirunnisa",
            "major": "Al-Qur'an and Tafsir",
            "starting_year": 2018,
            "total_attendance": 5,
            "standing": "7",
            "year": 3,
            "las_attendance_time": "2022-12-10 00:34:24"
        },
    "123456789":
        {
            "name": "Bruce Wayne",
            "major": "Criminology",
            "starting_year": 2005,
            "total_attendance": 100,
            "standing": "10",
            "year": 2,
            "las_attendance_time": "2022-11-10 00:11:24"
        },
    "12052024":
        {
            "name": "Anindya Wiraprasasta",
            "major": "Design Management",
            "starting_year": 2019,
            "total_attendance": 4,
            "standing": "3",
            "year": 2,
            "las_attendance_time": "2022-10-10 00:14:24"
        },
    "999999999":
        {
            "name": "Nur Hidayah Agustina",
            "major": "Physics Engineering",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "3",
            "year": 3,
            "las_attendance_time": "2022-10-10 00:14:24"
        }
}

for key, value in data.items():
    ref.child(key).set(value)