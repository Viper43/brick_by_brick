from fastapi import FastAPI
from fastapi.responses import JSONResponse
import util


app = FastAPI()
util.load_saved_artifacts()

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Predictor API"}

@app.get("/test")
def test():
    print("Test endpoint hit")
    return {"message": "Test successful"}

@app.get("/get_location_names")
def get_location_names():
    response = {'locations': util.get_location_names()}

    return JSONResponse(content=response, status_code=200)

@app.get("/get_predicted_price")
def get_predicted_price(bhk: float, bath: int, sqft: float, age: int, bal: int, location: str):
    try:
        price = util.get_house_price(bhk, bath, sqft, age, bal, location)
        return JSONResponse(content=float(price), status_code=200)
    except Exception as e:
        return {"error": str(e)}