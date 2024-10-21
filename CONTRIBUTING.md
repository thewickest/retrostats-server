# Contributing

You can contribute in two ways:
- **Adding a new game to the system**: Create a function that parses the binary file into a human-readable format.
- **Suggesting improvements**: Submit a merge request (MR) with any enhancements you think of, and we will review it.

## Parse Function
1. Create a new Python file, typically named after the game you want to include (`pang.py` for Pang, `pacman.py` for Pacman, etc.).
2. Inside it, define a function with the following description:
```
    def parser(textScorePath, byteScorePath)-> None:
        ....
        # write the sessions in .txt format into textScorePath
        # See pang.py for an example

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
4. Add your function inside the `mame2003/__init__.py` file:
```
...
import roms.mameLibretro.mame2003.pang as pang

...
def pangParser(textScorePath, byteScorePath):
    pang.parser(textScorePath, byteScorePath)
...
```

Note: We are working in a more dynamic way for including new games. Suggestions are welcome.