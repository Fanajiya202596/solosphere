import os

class Config:
    SECRET_KEY = "solosphere-secret-key"
    DATABASE_PATH = os.path.join("database", "solosphere.db")
