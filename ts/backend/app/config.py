import os
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chain_docs.db")
# SETTINGS = {"AWS_ACCESS_KEY" :"",
#  "AWS_SECRET_KEY" :"",
#  "AWS_REGION" :"", 
# "S3_BUCKET" :""}

AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
AWS_REGION = ""
S3_BUCKET = ""
