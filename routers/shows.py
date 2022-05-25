from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies import async_get_db, get_admin
from services.show_service import ShowService
from schemas.show_schemas import ShowOut, ShowInDb, ShowIn, ShowUpdate

router = APIRouter(prefix="/shows", tags=["shows"])


@router.get("/", response_model=list[ShowOut])
async def read_shows(db: AsyncSession = Depends(async_get_db)):
    return await ShowService(db).list_shows()


@router.get("/{show_id}/", response_model=ShowOut)
async def read_show(show_id: int, db: AsyncSession = Depends(async_get_db)):
    return await ShowService(db).retrieve_show(show_id)


@router.post("/", response_model=ShowInDb)
async def create_show(show: ShowIn, db: AsyncSession = Depends(async_get_db)):
    return await ShowService(db).create_show(show)


@router.patch("/{show_id}/", response_model=ShowOut)
async def patch_show(
    show_id: int,
    show: ShowUpdate,
    _=Depends(get_admin),
    db: AsyncSession = Depends(async_get_db),
):
    service = ShowService(db)
    await service.update_show(show_id, show)
    return await service.retrieve_show(show_id)


@router.delete("/{show_id}/", status_code=status.HTTP_200_OK)
async def delete_show(show_id: int, db: AsyncSession = Depends(async_get_db)):
    return ShowService(db).delete_show(show_id)
