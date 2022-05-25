from fastapi import FastAPI, Request

from routers import places, user, shows, films, orders
from utils.exceptions_utils import AppException, app_exception_handler

app = FastAPI()

app.include_router(places.router, prefix="/api")
app.include_router(films.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(shows.router, prefix="/api")
app.include_router(orders.router, prefix="/api")


@app.exception_handler(AppException)
async def custom_app_exception_handler(request: Request, exception: AppException):
    return await app_exception_handler(exception)
