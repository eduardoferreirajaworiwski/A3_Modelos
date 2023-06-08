from pymongo import MongoClient

def load_db():
    client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
    db = client["gestao_escola"]
    return db