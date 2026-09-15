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
    "amenities": [
        "dial-up speed wifi",
        "aggressive parallel parking test zone",
        "one rusty dumbbell (gym)"
    ],
}

house = {
    "id": 2,
    "name": "Spooky Mansionhouse Where the Floorboards Judge Your Life Choices",
    "price_per_night": 300,
    "bedrooms": 3,
    "bathrooms": 3,
    "amenities": [
        "wifi that requires a seance",
        "parking meant for a tricycle",
        "treadmill that only goes backward (gym)"
    ],
}

studio = {
    "id": 3,
    "name": "Cozy Shoebox: Cook, Sleep, and Shower Simultaneously Without Moving",
    "price_per_night": 200,
    "bedrooms": 1,
    "bathrooms": 1,
    "amenities": [
        "wifi powered by a single tired hamster",
        "parking if you abandon your car on the pavement",
        "emotional support yoga mat (gym)"
    ],
}

penthouse = {
    "id": 4,
    "name": "Luxury Penthouse With a Balcony Bigger Than Your First Flat",
    "price_per_night": 650,
    "bedrooms": 3,
    "bathrooms": 2,
    "amenities": [
        "fast wifi",
        "private parking",
        "rooftop terrace",
        "proper gym"
    ],
}

cottage = {
    "id": 5,
    "name": "Quiet Countryside Cottage Where Even Your Phone Gives Up",
    "price_per_night": 150,
    "bedrooms": 2,
    "bathrooms": 1,
    "amenities": [
        "questionable countryside wifi",
        "free parking",
        "fireplace",
        "garden"
    ],
}

loft = {
    "id": 6,
    "name": "City Centre Loft Above a Pub You Will Definitely Hear at 1AM",
    "price_per_night": 275,
    "bedrooms": 1,
    "bathrooms": 1,
    "amenities": [
        "fast wifi",
        "no parking",
        "city centre location",
        "coffee machine"
    ],
}

villa = {
    "id": 7,
    "name": "Poolside Villa Where You Pretend You Have Your Life Together",
    "price_per_night": 900,
    "bedrooms": 4,
    "bathrooms": 4,
    "amenities": [
        "fast wifi",
        "private parking",
        "swimming pool",
        "home gym"
    ],
}

basement = {
    "id": 8,
    "name": "Budget Basement Room With Surprisingly Optimistic Marketing",
    "price_per_night": 75,
    "bedrooms": 1,
    "bathrooms": 1,
    "amenities": [
        "wifi near the stairs",
        "street parking",
        "shared kitchen"
    ],
}


rooms = [
    apartment,
    house,
    studio,
    penthouse,
    cottage,
    loft,
    villa,
    basement
]


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

    results = rooms
    if max_price:
        results = [room for room in results if room["price_per_night"] <= max_price]
    if search:
        results = [room for room in results if search.lower() in room["name"].lower()]
    return results



@app.get("/rooms/{room_id}", status_code=status.HTTP_200_OK)
def get_room(room_id: int):
    for room in rooms:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")

