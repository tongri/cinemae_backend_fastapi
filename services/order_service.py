from crud.order_crud import create_order, list_orders
from crud.place_crud import get_place_by_id
from crud.show_crud import retrieve_show_short, update_show_busy
from utils.exceptions_utils import ConflictException, ObjNotFoundException
from utils.service_base import BaseService
from schemas.order_schemas import OrderIn


class OrderService(BaseService):
    async def create_order(self, user_id: int, show_id: int, order: OrderIn):
        show = await retrieve_show_short(self.db, show_id)
        if not show:
            raise ObjNotFoundException("Show", "id", show_id)
        place = await get_place_by_id(self.db, show.place_id)

        if show.busy + order.amount > place.size:
            raise ConflictException("Not enough free places")

        await update_show_busy(self.db, show_id, order.amount)
        await create_order(self.db, user_id, show_id, order)

    async def get_all_orders(self, user_id: int):
        return await list_orders(self.db, user_id)
