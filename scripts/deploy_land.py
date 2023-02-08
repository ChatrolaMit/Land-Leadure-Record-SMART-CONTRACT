from brownie import Land, Lands, Peoples , Contract
from scripts.helpful_scripts import get_account
from scripts.deploy_contract_land import deploy_land
from scripts.deploy_contract_lands import deploy_lands , add_lands
from scripts.deploy_contract_peoples import deploy_people ,add_people_in_chain
import time

# def add_new_farmer():
#     account = get_account()
#     upin = list()
#     land1 = deploy_land(
#         111,
#         11,
#         "amreli",
#         "amreli",
#         "keriya",
#         "shivaji vadi",
#         11,
#         "2-12-33",
#         1,
#         "kheti",
#         1

#     )
#     land2 = deploy_land(
#         112,
#         12,
#         "amreli",
#         "amreli",
#         "keriya",
#         "shivaji vadi",
#         12,
#         "2-12-33",
#         2,
#         "kheti",
#         2
#     )
#     land3 = deploy_land(
#         113,
#         13,
#         "amreli",
#         "amreli",
#         "keriya",
#         "shivaji vadi",
#         13,
#         "2-12-33",
#         3,
#         "kheti",
#         3

#     )
#     lands = deploy_lands()
#     landd = add_lands(111, land1 , lands  )
#     landd = add_lands(112, land2 , lands  )
#     landd = add_lands(113, land3 , lands  )
#     people = deploy_people()
#     peoples = add_people_in_chain(1111 , lands , people)
#     # print(land.UPIN())
#     # land.wait(1)
#     # people = Lands.deploy(land.UPIN(), land, {"from": account})

#     people_c = create_people_contract(people)
#     people_l = create_lands_contract(people_c.people_to_upin(1111))
#     l = create_land_contract(people_l.upinToAddress(113))
#     print(l.UPIN())


# def create_people_contract(_people):
#     contract = Contract.from_abi(Peoples ,_people , Peoples.abi )
#     return contract

# def create_lands_contract(_lands):
#     contract = Contract.from_abi(Lands ,_lands , Lands.abi )
#     return contract

# def create_land_contract(_land):
#     contract = Contract.from_abi(Land ,_land , Land.abi )
#     return contract


# from flask import request, Flask
# import json

people = deploy_people()

def main():

    # app = Flask(__name__)

    # @app.route('/' , methods = ['POST'])
    # def get_info():
        # data = request.json
        # loaded = json.load(data)
    
        
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
    lands = deploy_lands()
    for i in range(len(loaded["fid"]["lands"])):
        land = loaded["fid"]["lands"][i] 
        lan = deploy_land(land["upin"] , land["new_survay_number"],land["district"] ,land["taluka"] ,land["village"] ,land["land_title"] ,land["old_survay_no"] ,land["area"], land["total_assesment"] , land["land_use"] , land["tenure"] )
        add_lands(loaded["fid"]["lands"][i]["upin"] ,lan , lands )
        lands = Lands[-1]
        # time.sleep(60)
    add_people_in_chain(loaded["fid"] , lands , people)




        
