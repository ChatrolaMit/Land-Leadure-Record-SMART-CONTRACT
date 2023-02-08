# from brownie import Peoples , Lands , Land , Contract
# from scripts.helpful_scripts import get_account

# def deploy_people():
#     people = Peoples.deploy({"from": get_account()})
#     return people 
    
# def add_people_in_chain(_fid , _address):
#     account = get_account()
#     contract = Peoples.deploy({"from" : account})
#     added_people = contract.add_people(_fid ,_address , {"from": get_account()})
#     return added_people 

from brownie import Peoples , Lands , Land , accounts , network  , config  , Contract
from scripts.helpful_scripts import get_account


def deploy_people():
    people = Peoples.deploy({"from": get_account()})
    # people.wait(1)
    return people

def add_people_in_chain(_f_id , _address , _people ):
    contract = Contract.from_abi(Peoples ,_people.address , Peoples.abi )
    people = contract.add_people(_f_id, _address , {"from": get_account()} )
    # people.wait(1)
    return people 

    


    