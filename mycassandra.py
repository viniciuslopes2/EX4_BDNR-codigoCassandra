import os
from dotenv import load_dotenv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

load_dotenv()

cloud = {"secure_connect_bundle": os.environ["ASTRA_SCB_PATH"]}
auth = PlainTextAuthProvider("token", os.environ["ASTRA_DB_TOKEN"])
cluster = Cluster(cloud=cloud, auth_provider=auth)
session = cluster.connect("mercadolivre")