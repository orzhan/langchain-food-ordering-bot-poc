from typing import List

from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document

restaurant_name = "TestSushi"

full_menu = [{"name": "Salmon Nigiri", "id": 1, "price": 4.5,
              "description": "Fresh salmon slices served over seasoned sushi rice."},
             {"name": "California Roll", "id": 2, "price": 8.5,
              "description": "Crab meat, avocado, cucumber, and masago rolled in nori and sushi rice."},
             {"name": "Spicy Tuna Roll", "id": 3, "price": 9.5,
              "description": "Tuna, spicy mayo, cucumber, and avocado rolled in nori and sushi rice."},
             {"name": "Dragon Roll", "id": 4, "price": 14.5,
              "description": "Eel, cucumber, avocado, and crab meat rolled in nori and sushi rice, topped with avocado and eel sauce."},
             {"name": "Vegetable Roll", "id": 5, "price": 7.5,
              "description": "Cucumber, avocado, carrot, and asparagus rolled in nori and sushi rice."},
             {"name": "Tuna Sashimi", "id": 6, "price": 12.5,
              "description": "Thin slices of fresh tuna served raw with soy sauce and wasabi."},
             {"name": "Eel Nigiri", "id": 7, "price": 5.5,
              "description": "Grilled eel slices served over seasoned sushi rice, topped with eel sauce."},
             {"name": "Rainbow Roll", "id": 8, "price": 15.5,
              "description": "California roll topped with slices of tuna, salmon, yellowtail, and avocado."},
             {"name": "Spider Roll", "id": 9, "price": 12.5,
              "description": "Fried soft shell crab, avocado, and cucumber rolled in nori and sushi rice, topped with spicy mayo."},
             {"name": "Shrimp Tempura Roll", "id": 10, "price": 10.5,
              "description": "Tempura-fried shrimp, avocado, and cucumber rolled in nori and sushi rice, topped with eel sauce."},
             {"name": "Salmon Skin Roll", "id": 11, "price": 9.5,
              "description": "Grilled salmon skin, cucumber, and scallion rolled in nori and sushi rice."},
    {"name": "Rainbow Nigiri", "id": 12, "price": 5.50, "description": "Assorted fish slices served over seasoned sushi rice."},
    {"name": "Philadelphia Roll", "id": 13, "price": 8.50, "description": "Smoked salmon, cream cheese, cucumber, and avocado rolled in nori and sushi rice."},
    {"name": "Spider Nigiri", "id": 14, "price": 5.50, "description": "Fried soft shell crab served over seasoned sushi rice."},
    {"name": "Crunchy Roll", "id": 15, "price": 10.50, "description": "Shrimp tempura, avocado, and cucumber rolled in nori and sushi rice, topped with crunchy tempura bits."},
    {"name": "Sake Roll", "id": 16, "price": 9.50, "description": "Grilled salmon, cucumber, and avocado rolled in nori and sushi rice."},
    {"name": "Spicy Salmon Roll", "id": 17, "price": 10.50, "description": "Salmon, spicy mayo, cucumber, and avocado rolled in nori and sushi rice."},
    {"name": "Yellowtail Nigiri", "id": 18, "price": 6.50, "description": "Thin slices of fresh yellowtail served over seasoned sushi rice."},
    {"name": "Vegan Roll", "id": 19, "price": 8.50, "description": "Sweet potato tempura, avocado, and cucumber rolled in nori and sushi rice, topped with vegan spicy mayo."},
    {"name": "Dragonfly Roll", "id": 20, "price": 14.50, "description": "Shrimp tempura, eel, cucumber, and avocado rolled in nori and sushi rice, topped with eel sauce."},
    {"name": "Tuna Tartare", "id": 21, "price": 12.50, "description": "Chopped tuna mixed with avocado, cucumber, and scallions, served with crispy wonton chips."},
    {"name": "Volcano Roll", "id": 22, "price": 13.50, "description": "Spicy tuna, cream cheese, and avocado rolled in nori and sushi rice, baked and topped with spicy mayo and eel sauce."},
    {"name": "Octopus Nigiri", "id": 23, "price": 6.50, "description": "Thin slices of fresh octopus served over seasoned sushi rice."},
    {"name": "Scallop Roll", "id": 24, "price": 11.50, "description": "Baked scallop mixed with spicy mayo and cucumber, rolled in nori and sushi rice."},
    {"name": "Crab Rangoon Roll", "id": 25, "price": 9.50, "description": "Cream cheese, crab meat, and scallions rolled in nori and sushi rice, deep-fried and served with sweet and sour sauce."},
    {"name": "Red Dragon Roll", "id": 26, "price": 15.50, "description": "Spicy tuna, cucumber, and avocado rolled in nori and sushi rice, topped with slices of red snapper and spicy mayo."}]


full_menu_text = '\n'.join([f"{x['name']} ({x['id']}) - {x['price']} - {x['description']}" for x in full_menu]) + '''


TestSushi restaurant is located on Main street 123, Anytown. Working hours: 9am-10pm. Delivery area: all areas on Anytown. Ordering options: delivery, takeout.
All dishes can be prepared without any selected ingredients, on customer's request, the price is the same. 
'''
print(full_menu_text)


class StringLoader(BaseLoader):
    """Load text files."""

    def __init__(self, text: str):
        """Initialize with file path."""
        self.text = text

    def load(self) -> List[Document]:
        metadata = {}
        return [Document(page_content=s, metadata=metadata) for s in self.text.split('\n') if s.strip() != '']

