from brownie import Land, Lands, Peoples , Contract
from scripts.helpful_scripts import get_account
import time


def add_new_farmer():
    account = get_account()
    land = Land.deploy(
        111,
        11,
        "amreli",
        "amreli",
        "keriya",
        "shivaji vadi",
        11,
        "2-12-33",
        1,
        "kheti",
        1,
        {"from": account},
    )
    # land.wait(1)
    people = Lands.deploy(land.UPIN(), land, {"from": account})
    # people.wait(1)
    product = Peoples.deploy(1111, people, {"from": account})
    # peoples.wait(1)
    land = Land.deploy(
        112,
        12,
        "amreli",
        "amreli",
        "keriya",
        "shivaji vadi",
        11,
        "2-12-33",
        1,
        "kheti",
        1,
        {"from": account},
    )
    # land.wait(1)
    people = Lands.deploy(land.UPIN(), land, {"from": account})
    # people.wait(1)
    peoples = Peoples.deploy(1111, people, {"from": account})
    # # peoples.wait(1)
    # land = Land.deploy(
    #     113,
    #     13,
    #     "amreli",
    #     "amreli",
    #     "keriya",
    #     "shivaji vadi",
    #     11,
    #     "2-12-33",
    #     1,
    #     "kheti",
    #     1,
    #     {"from": account},
    # )
    # # land.wait(1)
    # people = Lands.deploy(land.UPIN(), land, {"from": account})
    # # people.wait(1)
    # product = Lands.deploy(1111, people, {"from": account})
    # peoples.wait(1)
    # print(people)
    # print(Peoples[0] , Peoples[1] , Peoples[2])
    
    
    # print(land , land.UPIN())
    # print("upin and land")
    # print(people , people.upinToAddress(111))
    # print("fid to land")
    # print(product , product.people_to_upin(1111))
    print(1)
    contract = Contract.from_abi(Lands ,product.people_to_upin(1111) , Lands.abi )
    # x = Contracts.Lands(product.people_to_upin(1111))
    print(2)
    contract1 = Contract.from_abi(Land ,contract.upinToAddress(111) , Land.abi )
    print(product , contract.upinToAddress(112))
    print(1)
    contract2 = Contract.from_abi(Land ,contract.upinToAddress(112) , Land.abi )
    print(2)
    # print(contract1)
    print(contract1.UPIN())
    print(contract2.UPIN())
    

def main():
    add_new_farmer()
