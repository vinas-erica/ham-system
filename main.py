from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

import json
import logging
import random
import sys
from datetime import datetime
from typing import Iterator

import asyncio

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates", autoescape=False)
random.seed()  # Initialize the random number generator

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
# async def index(request: Request):
    
#     return templates.TemplateResponse("index.html", request)
async def humidityData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100,
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

async def lightData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100,
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

async def phData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100, #getting data, this will be change
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

async def tempData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100, #getting data, this will be change
                # with open('canada.json','r') as f: #opening the file
                #         country_object = json.load(f)
            }
        )
    # with open('file.json', 'r') as f:
    #     data = json.load(f)
    #     json_data = json.dumps(
    #         "time": datetime.now().strftime("%H:%M:%S"),
    #         "value": data,
    #     )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

async def waterLevelData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100, #getting data, this will be change
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)

async def waterTempData(request: Request) -> Iterator[str]:
    """
    Generates random value between 0 and 100

    :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
    """
    client_ip = request.client.host

    logger.info("Client %s connected", client_ip)

    while True:
        json_data = json.dumps(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "value": random.random() * 100, #getting data, this will be change
            }
        )
        yield f"data:{json_data}\n\n"
        await asyncio.sleep(1)


@app.get("/chart-data-water-temp", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(waterTempData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses

@app.get("/chart-data-water-level", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(waterLevelData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses

@app.get("/chart-data-temp", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(tempData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses

@app.get("/chart-data-ph", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(phData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses

@app.get("/chart-data-light", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(lightData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses

@app.get("/chart-data-humidity", response_class=HTMLResponse)
async def chart_data(request: Request) -> StreamingResponse:
    responses = StreamingResponse(humidityData(request), media_type="text/event-stream")
    responses.headers["Cache-Control"] = "no-cache"
    responses.headers["X-Accel-Buffering"] = "no"
    return responses