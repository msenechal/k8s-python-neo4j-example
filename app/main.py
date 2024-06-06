from fastapi import FastAPI, HTTPException
from .neo4j_connector import get_neo4j_data

app = FastAPI()

@app.get("/neo4j")
async def read_neo4j():
    try:
        data = get_neo4j_data()
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))