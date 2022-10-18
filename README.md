# Bubblewrap
[![GitHub Super-Linter](https://github.com/TechWiz-3/bubblewrap/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

<img src="https://raw.githubusercontent.com/TechWiz-3/bubblewrap/main/media/example.png" alt="bubbles" width="650"> 

A Python library that makes beautiful text bubbles in your terminal using [NerdFont](https://www.nerdfonts.com/) icons.  

## Install
```sh
pip install bubblewrap-cli
```

## Usage

The easiest way to use bubblewrap is with the [Rich](https://github.com/Textualize/rich) library.  
```py
from bubblewrap import Bubbles
from rich.console import Console

b = Bubbles()
c = Console()
print()
c.print(b.get_rich_bubble("This is text", bg_color="purple"))
print()
c.print(b.get_rich_bubble("Bubblewrap!", bg_color="dark_green", fg_color="grey66"))
print()
```

You can also use your own ANSI codes

```py
from bubblewrap import Bubbles

b = Bubbles()

print()
# takes the text, circle style (an fg color), test style (the bg color same as fg color
# foreground and optionally it's own fg color), reset (your ANSI reset sequence)
print(b.get_ansi_bubbles("Ayo how are you?", "\033[31m", "\033[32;41m", "\033[0m"))
print()
```

Alternatively, you can link bubbles together:
```py
from bubblewrap import Bubbles
from rich.console import Console

b = Bubbles()
c = Console()

print()
c.print(b.get_rich_chain("Fri 09:45", "white", "black", divider="")
         .link("直 Wi-Fi", "orange3", "white")
         .link(" Charging", "bright_green", "black").end())

print()
print(b.get_ansi_chain("~/Projects", "\033[37;45m", "\033[0m")
       .link("bubblewrap", "\033[30;46m")
       .link("שׂ main", "\033[30;43m").end())
```

## Example
![bubbles](https://raw.githubusercontent.com/TechWiz-3/bubblewrap/main/media/bubbles.png)


## Contributors 🌟
<br>
<br>
<div align="center">
<a href="https://github.com/TechWiz-3/bubblewrap/graphs/contributors">

  <img src="https://contrib.rocks/image?repo=TechWiz-3/bubblewrap&&max=817" />

</a>
</div>
