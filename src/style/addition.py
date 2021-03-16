from keys import addition

from .const import grey, red, widget_args

title_in = widget_args(
    k=addition.title_in,
)

on_btn = widget_args(
    button_text="",  # デフォルトでは"off"だけ表示する
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

pass_in = widget_args(
    password_char="*",
    k=addition.pass_in,
)

confirm_pass_in = widget_args(
    password_char="*",
    k=addition.confirm_pass_in,
)

pass_pin_col = widget_args(
    k=addition.pass_col,
    visible=False,
)
