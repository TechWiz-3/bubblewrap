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

## Example
![bubbles](https://raw.githubusercontent.com/TechWiz-3/bubblewrap/main/media/bubbles.png)

## Contribution Guidelines

First of all, thank you so much for taking a deeper look at the project. It does mean a lot.  

PRs and issues of all sorts are welcome, here are some guides to help you out.  

When contributing to this repository, preferably first discuess the changes you wish to implement via [GitHub Issues](https://github.com/TechWiz-3/happy-jar-cli/issues) page.

If you're unure you to help, check out the `Todo` section of the project's README.md.  

Following the commit messages specified in [emoji-log](https://github.com/ahmadawais/Emoji-Log) is greatly appreciated (however not mandatory). You can use my [CLI tool](https://github.com/TechWiz-3/git-commit-emojis/) for commits if that's easier.  

All changes added must pass the CI tests (TBA) provided by the GitHub Actions workflows. If not, further changes must be done in order to make up for a valid pull request / merge request. If you need help because a test isn't passing, please open an issue :+1:

When making the pull request, please ensure you tick `Allow edits by maintainers`. More info [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork)  

We also have a [Code of Conduct](./CODE_OF_CONDUCT.md) in place so please make sure to follow the given set of guidelines and thresholds while you interact with the project!  

Contributors will receive recognition for their contributions to mankind (I mean this project) in the `Contributors` section of the `README.md`. You will also receive a nice title to describle your abilities and might open-source prowess.

## Contributors🌟
<br>

<div align="center">
<a href="https://github.com/TechWiz-3/bubblewrap/graphs/contributors">

  <img src="https://contrib.rocks/image?repo=TechWiz-3/bubblewrap&&max=817" />

</a>
</div>
