class Bubbles:

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

    def get_rich_chain(self, txt, bg_color="blue", fg_color="white", divider=""):
        return Link(txt, bg_color, fg_color, divider)

    def get_ansi_chain(self, txt, txt_style, reset, divider=""):
        return ANSILink(txt, txt_style, reset, divider)


class Link:
    base_str = ""
    bg_color = ""
    divider = ""

    def __init__(self, txt, bg_color, fg_color, divider, prev_link=None):
        self.bg_color = bg_color
        self.divider = divider

        body_open, body_close = get_tags(f"{fg_color} on {bg_color}")

        pre_txt = ""
        if prev_link is not None:
            pre_txt = prev_link.base_str

            # divider fg = prev link bg
            # divider bg = current link bg
            divider_open, divider_close = get_tags(f"{prev_link.bg_color} on {bg_color}")

            pre_txt += f"{divider_open}{divider}{divider_close}"

        self.base_str = f"{pre_txt}{body_open} {txt} {body_close}"

    def end(self):
        ending_open, ending_close = get_tags(self.bg_color)
        self.base_str += f"{ending_open}{self.divider}{ending_close}"

        return self.base_str

    def link(self, txt, bg_color, fg_color):
        return Link(txt, bg_color, fg_color, self.divider, self)


class ANSILink:
    base_str = ""
    txt_style = ""
    divider = ""
    reset = ""

    def __init__(self, txt, txt_style, reset, divider, prev_link=None):
        self.txt_style = txt_style
        self.divider = divider
        self.reset = reset

        pre_txt = ""
        if prev_link is not None:
            pre_txt = prev_link.base_str

            # divider fg = prev link bg
            # divider bg = current link bg
            divider_fg = str(int(prev_link.txt_style[-3:-1]) - 10)
            divider_bg = str(int(txt_style[-3:-1]))

            divider_style = f"\033[{divider_fg};{divider_bg}m"

            pre_txt += f"{divider_style}{divider}{reset}"

        self.base_str = f"{pre_txt}{txt_style} {txt} {reset}"

    def end(self):
        divider_fg = str(int(self.txt_style[-3:-1]) - 10)
        self.base_str += f"\033[{divider_fg}m{self.divider}{self.reset}"

        return self.base_str

    def link(self, txt, txt_style):
        return ANSILink(txt, txt_style, self.reset, self.divider, self)


def get_tags(style):
    open_tag = f"[{style}]"
    close_tag = f"{open_tag[:1]}/{open_tag[1:]}"

    return open_tag, close_tag


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
