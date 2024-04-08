import datetime
import edgedb

from typing import List

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from .queries import get_user_by_name_async_edgeql as get_user_by_name_qry
from .queries import get_users_async_edgeql as get_users_qry


router = APIRouter()
client = edgedb.create_async_client()


class RequestData(BaseModel):
    name: str


@router.get("/users")
async def get_users(
    name: str = Query(None, max_length=50)
) -> List[get_users_qry.GetUsersResult] | get_user_by_name_qry.GetUserByNameResult:

    if not name:
        users = await get_users_qry.get_users(client)
        return users
    else:
        user = await get_user_by_name_qry.get_user_by_name(client, name=name)
        if not user:
            raise HTTPException(
                status_code=404,
                detail={"error": f"Username '{name}' does not exist."},
            )

        return user
