from fastapi import APIRouter, Body
from ..util.schemas.park_schema import Park_schema
from ..service.park_service import post_new_park

router = APIRouter()


@router.get("/{id}", response_description="Park based on id")
async def get_park_id(id, park: Park_schema = Body(...)):
    pass


@router.post("/post", response_description="Post park")
async def post_park_(park: Park_schema = Body(...)):
    data = {"park_name": "xanthi", "asset_id": "1"}
    response = await post_new_park(data=data)
    print(response)
    if response[1] == 201:
        return response[0], 201
    else:
        return False
