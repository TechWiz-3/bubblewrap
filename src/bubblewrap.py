class Bubbles():

    def __init__(self):
        pass

    def get_rich_bubble(self, txt, bg_color="blue", fg_color="white", rich=True):
        circle_style = f"[{bg_color}]"
        circle_close = f"{circle_style[:1]}/{circle_style[1:]}"
        body_open = f"[{fg_color} on {bg_color}]"
        body_close = f"{body_open[:1]}/{body_open[1:]}"
        return f"{circle_style}{circle_close}{body_open}{txt}{body_close}{circle_style}{circle_close}"

    def get_ansi_bubbles(self, txt, circle_style, txt_style, reset):
        bubble = f"{circle_style}{reset}{txt_style}{txt}{reset}{circle_style}{reset}"
        return bubble


def cli() -> None:
    from rich.console import Console
    b = Bubbles()
    c = Console()
    print()
    c.print(b.get_rich_bubble("Hello World", bg_color="purple"), end=" ")
    c.print(b.get_rich_bubble("I love bubblewrap", bg_color="red"), end=" ")
    c.print(b.get_rich_bubble("try it now", bg_color="blue"))
    print()
    c.print(b.get_rich_bubble("Bubble up words", bg_color="dark_green", fg_color="grey66"), end=" ")
    c.print(b.get_rich_bubble("or entire sentences", bg_color="blue"), end=" ")
    c.print(b.get_rich_bubble("try it now", bg_color="purple"))
    print()
    c.print(b.get_rich_bubble("Use Rich, or ANSI colors of your choosing", bg_color="purple"))
    print()
    c.print(b.get_rich_bubble("Fully control", bg_color="blue"), end=" ")
    c.print(b.get_rich_bubble("background", bg_color="dark_green"), end=" ")
    c.print(b.get_rich_bubble("and", bg_color="purple"), end=" ")
    c.print(b.get_rich_bubble("foreground", bg_color="blue", fg_color="dark_red"), end=" ")
    c.print(b.get_rich_bubble("colors", bg_color="grey66", fg_color="grey3"))
    print()
    c.print(b.get_rich_bubble("Create beautiful CLI applications, with ease!", bg_color="deep_pink4"))
    print()

#print(b.get_ansi_bubbles("Ayo how are you", "\033[31m", "\033[32;41m", "\033[0m"))
