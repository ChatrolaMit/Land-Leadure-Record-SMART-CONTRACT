from brownie import Peoples , Lands , Land , accounts , network  , config  
from scripts.helpful_scripts import get_account

def deploy_land(_UPIN ,_newSurvayNo ,_district ,_taluka ,_village ,_landTitle ,_oldSurvayNo ,_area ,_totalAssesment ,_landUse ,_tenure):
    land = Land.deploy(_UPIN ,_newSurvayNo ,_district ,_taluka ,_village ,_landTitle ,_oldSurvayNo ,_area ,_totalAssesment ,_landUse ,_tenure , {"from": get_account()})
    # land.wait(1)
    
    return land 

# def add_land(_UPIN ,_newSurvayNo ,_district ,_taluka ,_village ,_landTitle ,_oldSurvayNo ,_area ,_totalAssesment ,_landUse ,_tenure):
    