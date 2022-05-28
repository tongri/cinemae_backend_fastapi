from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from utils.crud_utils import accumulated_dict_fetch_all
from schemas.order_schemas import OrderIn

ORDERS_DETAILED_SELECT = "select o.id as id, amount, price as show__price, busy as show__busy," \
                         " s.id as show__id, p.name as show__place__name, p.size as show__place__size," \
                         " p.id as show__place__id, f.id as show__film__id, f.name as show__film__name, " \
                         " f.begin_date as show__film__begin_date, f.end_date as show__film__end_date," \
                         " f.lasts_minutes as show__film__lasts_minutes, s.show_time_start as show__show_time_start" \
                         " from orders o inner join shows s on o.show_id = s.id" \
                         " inner join films f on f.id = s.film_id" \
                         " inner join places p on s.place_id = p.id"


async def create_order(
        db: AsyncSession, user_id: int, show_id: int, order: OrderIn,
):
    await db.execute(
        text(
            "insert into orders (user_id, show_id, amount) values (:user_id, :show_id, :amount)"
        ),
        {"user_id": user_id, "show_id": show_id, "amount": order.amount}
    )
    await db.commit()


async def list_orders(db: AsyncSession, user_id: int):
    res = await db.execute(
        text(f"{ORDERS_DETAILED_SELECT} where user_id = :user_id"),
        {"user_id": user_id}
    )
    return accumulated_dict_fetch_all(res.cursor)
