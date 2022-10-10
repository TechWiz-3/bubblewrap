# Bubblewrap

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

## Example
![bubbles](https://raw.githubusercontent.com/TechWiz-3/bubblewrap/main/media/bubbles.png)
