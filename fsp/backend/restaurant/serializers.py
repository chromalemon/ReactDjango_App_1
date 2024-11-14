from .models import FoodItem
from typing import Iterable, List, Dict, Any


def serialize_foods(foods: Iterable[FoodItem]) -> List[Dict[str, Any]]:
    data = []
    for food in foods:
        data.append({
            "name": food.name,
            "price": food.price,
            "photo_url": food.photo_url,
            "stock": food.stock,
        })
    return data