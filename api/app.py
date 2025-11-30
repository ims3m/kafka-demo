from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import os
from datetime import datetime
from faker import Faker
from threading import Thread


fake = Faker()


Producer = KafkaProducer()


class Location(BaseModel):
    pass

class Ride(BaseModel):
    pass


app = FastAPI()


@app.get("/")
def app():
    return {"message": "App is running..."}


@app.post("/generate/locations")
def generate_locations():
    pass


@app.post("/generate/rides")
def generate_rides():
    pass
