from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi_pagination import Page
from dependencies import get_current_user, async_get_db
from schemas.order_schemas import OrderIn, OrderOut
from services.order_service import OrderService
from schemas.user_schemas import UserOut
from utils.pagination_utils import PaginationParams, from_response_to_page

router = APIRouter(tags=["orders"])


@router.post("/shows/{show_id}/create_order/", status_code=status.HTTP_200_OK)
async def create_order(
    show_id: int,
    order: OrderIn,
    db: AsyncSession = Depends(async_get_db),
    current_user: UserOut = Depends(get_current_user),
):
    await OrderService(db).create_order(current_user.id, show_id, order)


@router.get("/orders/", response_model=Page[OrderOut])
async def list_orders(
    page: PaginationParams = Depends(PaginationParams),
    db: AsyncSession = Depends(async_get_db),
    current_user: UserOut = Depends(get_current_user),
):
    return from_response_to_page(page, await OrderService(db).get_all_orders(current_user.id))
