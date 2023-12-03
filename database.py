import chromadb as db

chroma_client = db.Client()

collection = chroma_client.get_or_create_collection(name="main_collection")

# collection.add(
#     ids=["id1", "id2", "id3"],
#     documents=["This is a document", "This is another document", "industrie"]
# )
#
# results = collection.query(
#     query_texts=["This is a query document"]
# )
#
# for inner_list in results["documents"]:
#     text = ", ".join(inner_list)
#     print(text)


#print(results["documents"])
#print(results.get("documents"))



