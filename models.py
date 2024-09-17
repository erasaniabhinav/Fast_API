from fastapi import FastAPI
from pydantic import BaseModel


class List_class(BaseModel):
    id : int
    item : str
    