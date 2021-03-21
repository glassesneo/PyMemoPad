from typing import Any

from keys import main

from .const import widget_args

search_img = widget_args(
    filename="asset/search.png",
    size=(12, 12),
    k=main.search_img,
    enable_events=True,
)

search_in = widget_args(
    size=(16, 2),
    k=main.search_in,
)

add_btn = widget_args(
    button_text="+",
    size=(2, 1),
    k=main.add_btn,
)

items_listbox = widget_args(
    enable_events=True,
    size=(22, 20),
    k=main.items_lb,
)

exit_btn = widget_args(
    button_text="Exit",
    size=(3, 1),
    k=main.exit_btn,
)
