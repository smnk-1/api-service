from fastapi import FastAPI, HTTPException, Depends
from config import DATABASE_BACKEND
from schemas import UserCreate, UserRead
import models

app = FastAPI()

if DATABASE_BACKEND == "postgres":
    from database import SessionLocal
    import crud_postgres
    models.Base.metadata.create_all(bind=SessionLocal.kw["bind"])
    crud = crud_postgres
elif DATABASE_BACKEND == "redis":
    from database import redis_client
    import crud_redis
    crud = crud_redis
else: 
    raise Exception("Unsupported database type")

def get_db():
    if DATABASE_BACKEND == "postgres":
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    elif DATABASE_BACKEND == "redis":
        yield redis_client
    else:
        raise RuntimeError("Unsupported database backend")

@app.post("/user/", response_model=UserRead, status_code=201)
def create_user(user: UserCreate, db=Depends(get_db)):
    if crud.get_user(db, user.id):
        raise HTTPException(status_code=400, detail="ID is occupied")
    return crud.create_user(db, user)

@app.get("/user/{user_id}", response_model=UserRead)
def read_user(user_id: int, db=Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db=Depends(get_db)):
    if user.id != user_id:
        raise HTTPException(status_code=400, detail="IDs don't match")
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/user/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db=Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted

if __name__ == "__main__":
    import uvicorn
    print("running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("end")
