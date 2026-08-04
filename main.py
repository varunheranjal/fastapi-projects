from fastapi import FastAPI, status

app = FastAPI(title="Rent-A-Room API", description="Rent a house or a room!", version="1.0.0")


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to the Rent-A-Room app"}

@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms():
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

    return [apartment, house, studio]
