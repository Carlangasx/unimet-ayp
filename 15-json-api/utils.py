import json
from typing import List, Dict
from Client import Client

# 'clients.json'
def write_clients(file_name: str, clients: List[Client]):
  result = []
  for client in clients:
    result.append(client.to_dict())
  with open(file_name, 'w') as file:
    json.dump(result, file)

def read_clients(file_name: str) -> List[Client]:
  try:
    result: List[Dict[str, any]] = []
    with open(file_name, 'r') as file:
      result = json.load(file)
    clients: List[Client] = []
    for client in result:
      c = Client.from_dict(client)
      clients.append(c)
    return clients
  except FileNotFoundError:
    return []

