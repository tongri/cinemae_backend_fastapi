from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.order_schemas import OrderIn


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
