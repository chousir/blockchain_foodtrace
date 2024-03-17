from blockchain import Blockchain


blockchain = Blockchain()

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return chain_data

# Show Genesis Block
print(get_chain())
print("\n")

# show participant_registration
tx_data = {
    "Participant": "GreenHarvest Farms", 
    "Industry": "Agriculture", 
    "Account": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", 
    "message": "1710260241", 
    "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="
    }
blockchain.participant_registration(transaction=tx_data)
blockchain.mine()
print(get_chain())
print("\n")

# show product registration
tx_data = {
    "Owner ID": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", 
    "Product Name": "Green Pepper", 
    "Description": "Not good", 
    "Item Weight": "50 KG", 
    "Expiry Date": "365",
    "Ingredients": [],
    "message": "1710260241", 
    "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="
    }
blockchain.product_registration(transaction=tx_data)
blockchain.mine()
print(get_chain())
print("\n")

# search product_registration block by OwnerName, ProductName, ProductID
a = blockchain.search_product(OwnerName='GreenHarvest Farms')
print(a)
print("\n")
b = blockchain.search_product(ProductName='Green Pepper')
print(b)
print("\n")
c = blockchain.search_product(OwnerName='GreenHarvest Farms', ProductName='Green Pepper')
print(c)
print("\n")
for i in c:
    d = blockchain.search_product(ProductID=i['Product ID'])
    print(d)
    print("\n")

# show product registration with ingredient(ProductID)
tx_data = {
    "Owner ID": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", 
    "Product Name": "Green Pepper hamberger", 
    "Description": "good", 
    "Item Weight": "5 KG", 
    "Expiry Date": "365",
    "Ingredients": [d[0]['Product ID']],
    "message": "1710260241", 
    "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="
    }
blockchain.product_registration(transaction=tx_data)
blockchain.mine()
print(get_chain())
print("\n")
