# blockchain_foodtrace
Use Blockchain to guarantee "Food trace ability" from the farm to the table with complete transparency of the food Supply chain ensuring 100% Food Safety and Trust.

### Run blockchain
export FLASK_APP=blockchain.py
flask run --port 8000

python run_app.py




### Client ECDSA Key generate and validate

Generate Public Key & Private Key
```sh
python3 client.py -g
```
Public Key: FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==
Private Key: e4eb0bd056fb81461b3505c1e8666dd47f5b0e6abbe8eb3ca47377b58ac2254b

Generate signature & message with Private Key
```sh
python3 client.py -s e4eb0bd056fb81461b3505c1e8666dd47f5b0e6abbe8eb3ca47377b58ac2254b
```
signature: AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g==
message: 1710260241

Validate signature with
```sh
python3 client.py -v FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg== AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g== 1710260241
```
Signature Validation: Success

### Client register account

Account is Public Key
```sh
curl -X POST \
  http://127.0.0.1:8000/register \
  -H 'Content-Type: application/json' \
  -d '{"Participant": "GreenHarvest Farms", "Industry": "Agriculture", "Account": "FXAIbYvbUzkjSyabFYOvGbrUb9UvT8moBgOrzYwo57qs8/8kD99IyUER+MP7jr7R3d2xLHRqFl2OEUUsLo/oEg==", "message": "1710260241", "signature": "AlbSt6B6R7l22kJzEk623NI8tsVe3yyllax1NIHEE7QhLRBHwbNWoP4QtlfsRRqCd1l9qYNiBhNijQjQ2qxQ2g=="}'
```

```sh
curl -X GET http://localhost:8000/mine
```

```sh
curl -X GET http://localhost:8000/chain
```


