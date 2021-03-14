from typing import Any

from keys import keys

args = dict[str, Any]

search_img: args = dict(
    filename="asset/search.png",
    size=(12, 12),
    k=keys.search_img,
    enable_events=True,
)

search_in: args = dict(
    size=(20, 2),
    k=keys.search_in,
)

items_listbox: args = dict(
    enable_events=True,
    size=(22, 20),
    k=keys.items_lb,
)
