import os
import sys

import requests

base = os.environ["OPS_API_BASE"]
token = os.environ["OPS_API_TOKEN"]
queue = sys.argv[1]
reply = requests.get(f"{base}/interfaces/{queue}/queue", headers={"Authorization": "Bearer " + token}, timeout=10)
print(queue, reply.json().get("depth"))
