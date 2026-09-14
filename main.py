from typing import Annotated
from fastapi import FastAPI, status, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from pydantic import AfterValidator


app = FastAPI(title="Rent-A-Room API", description="Rent a house or a room!", version="1.0.0", contact={"name": "Varun Heranjal", "email": "varunheranjal@gmail.com"})

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

apartment = {
    "id": 1,
    "name": "The 'Sunny' 2-Bedroom Apartment Where the Blinds Are Permanently Broken",
    "price_per_night": 200,
    "bedrooms": 2,
    "bathrooms": 2,
    "amenities": ["dial-up speed wifi", "aggressive parallel parking test zone", "one rusty dumbbell (gym)"],
}

house = {
    "id": 2,
    "name": "Spooky Mansion Where the Floorboards Judge Your Life Choices",
    "price_per_night": 300,
    "bedrooms": 3,
    "bathrooms": 3,
    "amenities": ["wifi that requires a seance", "parking meant for a tricycle", "treadmill that only goes backward (gym)"],
}

studio = {
    "id": 3,
    "name": "Cozy Shoebox: Cook, Sleep, and Shower Simultaneously Without Moving",
    "price_per_night": 200,
    "bedrooms": 1,
    "bathrooms": 1,
    "amenities": ["wifi powered by a single tired hamster", "parking if you abandon your car on the pavement", "emotional support yoga mat (gym)"],
}


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to the Rent-A-Room app"}


def fail_if_funny(search: str):
    print("Processing search term:", search)
    if "lol" in search.lower():
        raise ValueError("No funny business allowed!")
    return search

@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms(
    max_price: Annotated[int | None, Query(ge=10, le=10_000)] = None, 
    search: Annotated[
        str | None, 
        Query(min_length=3, max_length=10, title="Search term", description="Provide a Search Term to find rooms (fyi, no funny business)"),
        AfterValidator(fail_if_funny)] = None
):

    results = [apartment, house, studio]
    if max_price:
        results = [room for room in results if room["price_per_night"] <= max_price]
    if search:
        results = [room for room in results if search.lower() in room["name"].lower()]
    return results



@app.get("/rooms/{room_id}", status_code=status.HTTP_200_OK)
def get_room(room_id: int):
    for room in [apartment, house, studio]:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")

