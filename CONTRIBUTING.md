# Contributing

You can contribute in two ways:
- **Adding a new game to the system**: Create a function that parses the binary file into a human-readable format.
- **Suggesting improvements**: Submit a merge request (MR) with any enhancements you think of, and we will review it.

## Parse Function
1. Create a new Python file, typically named after the game you want to include (`pang.py` for Pang, `pacman.py` for Pacman, etc.).
2. Inside it, define a function with the following description:
```
    # 
    # It receives a file with binary content and returns an array with each line being a different score + additional content.
    # Currently, only the first section of the line (the score) will be considered, but we return everything for later usage.
    #
    def pangParser(binaryFile: File) -> str[]:
        ....
        return [
            234583|BOB|20|01,
            80000|M.K|18|02,
            70000|T.U|17|03,
            60000|K.H|15|04,
            50000|Y.N|13|05,
            40000|Y.K|12|06,
            30000|Y.F|11|07,
            20000|M.N|10|08,
            10000|M.M|05|09,
            5000|J.O|03|10,
        ]
```
3. Place the file in the corresponding project folder.
```
\project_folder
    \roms
        \mame-libretro
            \mame2003
                ...
                pang.py
                ...

```
4. Add your function inside the `switcher.py` file:
```
...
from mame2003 import pacmanParser, pangParser

class Switcher(object):
    def hiToText(self, textScorePath, byteScorePath, gameName):
        ...
```
