# uvicorn app_fastapi:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import app_database
from typing import Union

app = FastAPI()


# --- Models ---
class UserData(BaseModel):
    name: str
    level: int

class UserUpdate(BaseModel):
    name: Union[str, None] = None
    level: Union[int, None] = None


# --- Table Management ---
@app.post("/create-user/{table_name}")
def api_create_table(table_name: str):
    try:
        app_database.create_table(table_name)
        return {"message": f"Table '{table_name}' created successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.delete("/delete-user/{table_name}")
def api_delete_table(table_name: str):
    try:
        app_database.delete_table(table_name)
        return {"message": f"Table '{table_name}' deleted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/check-users/{table_name}")
def api_check_table(table_name: str):
    try:
        exists = app_database.check_table_exists(table_name)
        return {"exists": exists}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/list-users")
def api_list_tables():
    try:
        tables = app_database.list_tables()
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# --- User Management ---
@app.post("/add-character/{table_name}")
def api_add_user(table_name: str, user: UserData):
    try:
        app_database.insert_data(table_name, user.name, user.level)
        return {"message": "User added."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/list-character/{table_name}")
def api_list_users(table_name: str):
    try:
        users = app_database.retrieve_data(table_name)
        return [dict(u) for u in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/show-character/{table_name}/{user_id}")
def api_get_user_by_id(table_name: str, user_id: int):
    try:
        user = app_database.get_user_by_id(table_name, user_id)
        if user:
            return dict(user)
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search-character/{table_name}")
def api_find_user_by_name(table_name: str, name: str):
    try:
        users = app_database.find_users_by_name(table_name, name)
        return [dict(u) for u in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/change-character/{table_name}/{user_id}")
def api_update_user(table_name: str, user_id: int, updates: UserUpdate):
    try:
        app_database.update_user(table_name, user_id, name=updates.name, level=updates.level)
        return {"message": "User updated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/delete-character/{table_name}/{user_id}")
def api_delete_user(table_name: str, user_id: int):
    try:
        app_database.delete_user(table_name, user_id)
        return {"message": "User deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/count/{table_name}")
def api_count_users(table_name: str):
    try:
        count = app_database.count_users(table_name)
        return {"count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
