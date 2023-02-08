from brownie import network , config , accounts

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development" , "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork" , "mainnet-fork-dev"] 


def get_account(index=None ,id=None) :
    
    
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    
    
    return accounts.add(config["wallets"]["from_key"])