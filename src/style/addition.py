from keys import addition

from .const import grey, red, widget_args

title_in = widget_args(
    k=addition.title_in,
)

pass_txt = widget_args(
    text="password:",
    size=(8, 2),
)

pass_in = widget_args(
    password_char="*",
    k=addition.pass_in,
)

pass_check = widget_args(
    text="show password",
    enable_events=True,
    k=addition.pass_check,
)

on_btn = widget_args(
    button_text="on",  # デフォルトでは"off"だけ表示する
    size=(3, 1),
    button_color=grey,
    pad=((5, 0), (5, 5)),
    k=addition.on_btn,
)

off_btn = widget_args(
    button_text="off",
    size=(3, 1),
    button_color=red,
    pad=((0, 5), (5, 5)),
    k=addition.off_btn,
)

pass_pin_col = widget_args(
    k=addition.pass_col,
    visible=False,
)

error_txt = widget_args(
    text="This title is already in use.",
    text_color=red,
)

error_pin_col = widget_args(
    k=addition.error_col,
    visible=False,
)

cancel_btn = widget_args(
    size=(6, 1),
    k=addition.cancel_btn,
)

ok_btn = widget_args(
    size=(6, 1),
    k=addition.ok_btn,
)
