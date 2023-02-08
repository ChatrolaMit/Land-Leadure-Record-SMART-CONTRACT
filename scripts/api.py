# from flask import request , Flask
# import json


# app = Flask(__name__)

# @app.route('/' , methods = ['POST'])
# def get_info():
#     data = request.json
#     loaded = json.load(data)
    
    


# app.run( host = '0.0.0.0' , port=5000 , debug=True)    


loaded = {
        "fid": {
            "name": "dilip",
            "id": "jzhcfbzjxh",
            "lands": [
                {
                    "upin": 111,
                    "new_survay_number": 11,
                    "district": "amreli",
                    "taluka": "amreli",
                    "village": "keriya",
                    "land_title": "shivaji vadi",
                    "old_survay_no": 11,
                    "area": "2-12-33",
                    "total_assesment": 1,
                    "land_use": "kheti",
                    "tenure": 1,
                },
                {
                    "upin": 112,
                    "new_survay_number": 12,
                    "district": "amreli",
                    "taluka": "amreli",
                    "village": "keriya",
                    "land_title": "shivaji vadi",
                    "old_survay_no": 12,
                    "area": "2-12-33",
                    "total_assesment": 2,
                    "land_use": "kheti",
                    "tenure": 2,
                },
                {
                    "upin": 113,
                    "new_survay_number": 13,
                    "district": "amreli",
                    "taluka": "amreli",
                    "village": "keriya",
                    "land_title": "shivaji vadi",
                    "old_survay_no": 13,
                    "area": "2-12-33",
                    "total_assesment": 3,
                    "land_use": "kheti",
                    "tenure": 3,
                },
            ],
        }
    }

print(loaded["fid"]["name"])
print(loaded["fid"]["id"])
print(len(loaded["fid"]["lands"]))
print(loaded["fid"]["lands"][0]["upin"])