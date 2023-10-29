from typing import List


class Shop:
    def __init__(self, name: str, items: List):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)