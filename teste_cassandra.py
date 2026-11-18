from mycassandra import session, cluster

linha = session.execute("SELECT release_version FROM system.local").one()
print("Conectado ao Cassandra! Versão:", linha.release_version)

cluster.shutdown()