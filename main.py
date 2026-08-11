from fastapi import FastAPI, status, HTTPException

app = FastAPI(title="Rent-A-Room API", description="Rent a house or a room!", version="1.0.0")

apartment = {
        "id": 1,
        "name": "Sunny 2 bed room apartment",
        "price_per_night": 200,
        "bedrooms": 2,
        "bathrooms": 2,
        "amenities": ["wifi", "parking", "gym"],
    }

house = {
        "id": 2,
        "name": "House for rent in JP Nagar",
        "price_per_night": 300,
        "bedrooms": 3,
        "bathrooms": 3,
        "amenities": ["wifi", "parking", "gym"],
    }

studio = {
        "id": 3,
        "name": "Studio apartment in Koramangala",
        "price_per_night": 200,
        "bedrooms": 1,
        "bathrooms": 1,
        "amenities": ["wifi", "parking", "gym"],
    }


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to the Rent-A-Room app"}


@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms():
    return [apartment, house, studio]


@app.get("/rooms/faq", status_code=status.HTTP_200_OK)
def get_rooms_faq():
    return {"check_in:" "From 15:00 to 19:00", "check_out:" "From 10:00 to 12:00"}


@app.get("/rooms/{room_id}", status_code=status.HTTP_200_OK)
def get_room(room_id: int):
    for room in [apartment, house, studio]:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")

