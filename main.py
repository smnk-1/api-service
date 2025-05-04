from fastapi import FastAPI, HTTPException
from shemas import *
from typing import List

db: List[User] = []

app = FastAPI()

@app.post("/user/", response_model=UserRead)
def create_user(user: User):
    if any(user.id == u.id for u in db):
        raise HTTPException(status_code=400, detail="ID is occupied ")
    db.append(user)
    return user

@app.get("/user/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int):
    for u in db:
        if user_id == u.id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/user/{user_id}", response_model=UserRead)
def update_user(user_id: int, new_data: User):
    if new_data.id != user_id:
        raise HTTPException(status_code=400, detail="IDs don't match")
    for idx, u in enumerate(db):
        if u.id == user_id:
            db[idx] = new_data
            return new_data
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}", response_model=UserRead)
def delete_user(user_id: int):
    for idx, u in enumerate(db):
        if u.id == user_id:
            deleted = db.pop(idx)
            return deleted
    raise HTTPException(status_code=404, detail='User not found')

if __name__ == "__main__":
    import uvicorn
    print("running")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print('end')
