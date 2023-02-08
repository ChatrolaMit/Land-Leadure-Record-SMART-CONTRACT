from brownie import Peoples , Lands , Land , accounts , network  , config  , Contract
from scripts.helpful_scripts import get_account


def deploy_lands():
    lands = Lands.deploy({"from": get_account()})
    # lands.wait(1)
    return lands 

def add_lands(_upin , _address , _lands ):
    lan = Lands[-1].add_land(_upin, _address , {"from": get_account()} )
    lan.wait(1) 
    return lan 
