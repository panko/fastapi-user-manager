from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int | None = None
    username: str
    password: str
    email: str


def get_id_upto(start: int = 0, end: int = 1000):
    yield from range(start, end)


id_gen = get_id_upto()


@app.get("/")
async def root():
    return {"message": "This is a user-manager api"}


@app.post("/v1/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    # TODO validations
    user.id = next(id_gen)
    users.append(user)
    return {"message": f"Congratulations you've created {user.username}"}


@app.get("/v1/users", status_code=status.HTTP_200_OK)
async def get_all_users():
    return {"users": users}
