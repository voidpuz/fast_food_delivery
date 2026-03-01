from fastapi import APIRouter, HTTPException
from sqlalchemy import select 

from app.models import Order
from app.database import db_dep
from app.schemas.order import OrderListResponse, OrderUpdateRequest,OrederCreateRequest
from app.dependencies import current_user_dep

router=APIRouter(prefix="/order",tags=["/Orders"])

@router.get("/{order_id}",response_model=OrderListResponse)
async def get_order(session: db_dep, order_id: int):
    stmt=select(Order).where(Order.id==order_id)
    res=session.execute(stmt)
    product=res.scalars().first()

    return product 


@router.post("/create",response_model=OrederCreateRequest)
