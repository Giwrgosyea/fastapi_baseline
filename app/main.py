from fastapi import FastAPI
from .util.db.db_utils import connect_to_mongo, close_mongo_connection
from .routers.api import router as api_router


# from app.server.routes.student import router as StudentRouter
# app.include_router(StudentRouter, tags=["Student"], prefix="/student")


def create_app():
    """Create Fast Api app

    Returns:
        None: None
    """
    app = FastAPI()
    app.add_event_handler("startup", connect_to_mongo)
    app.add_event_handler("shutdown", close_mongo_connection)
    app.include_router(api_router, prefix="/park")
    return app


app = create_app()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FAST API demo!"}
