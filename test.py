from blockchain import Blockchain

blockchain = Blockchain()

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return chain_data

# Show Genesis Block
print(get_chain())

# show participant_registration
tx_data = {"Participant": "GreenHarvest Farms", "Industry": "Agriculture", "Account": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", "message": "1710260241", "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="}
blockchain.participant_registration(transaction=tx_data)
blockchain.mine()
print(get_chain())

# show pruoduct_registration
tx_data = {"Owner ID": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", "Product Name": "Green Pepper", "Description": "Not good", "Item Weight": "50 KG", "Expiry Date": "1 years", "message": "1710260241", "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="}
blockchain.pruoduct_registration(transaction=tx_data)
blockchain.mine()
print(get_chain())

