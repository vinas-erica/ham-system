from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import grovepi

app = FastAPI()

templates = Jinja2Templates(directory="templates", autoescape=False)

dht_sensor = 4
moisture_sensor = 3
light_sensor = 0

grovepi.pinMode(dht_sensor, "INPUT")
grovepi.pinMode(moisture_sensor, "INPUT")
grovepi.pinMode(light_sensor, "INPUT")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    [temp, humidity] = grovepi.dht(dht_sensor, 0)
    light = grovepi.analogRead(light_sensor)
    moisture = grovepi.analogRead(moisture_sensor)
    context = {
    "request": request,
        "temp": temp,
        "humidity": humidity,
        "light": light,
        "moisture": moisture
    }
    return templates.TemplateResponse("index.html", context)
