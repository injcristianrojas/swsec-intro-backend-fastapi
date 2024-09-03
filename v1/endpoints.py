from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_items():
    return {"version": "v1", "items": ["item1", "item2"]}