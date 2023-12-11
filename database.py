import chromadb as db

chroma_client = db.Client()

collection = chroma_client.get_or_create_collection(name="main_collection")

results = collection.query(
    query_texts=["This is a query document"]
)

print(results["documents"])
print(results.get("documents"))



