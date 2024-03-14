from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB dropped")
    await create_tables()
    print("DB ready to work")
    yield
    print("Swith off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
