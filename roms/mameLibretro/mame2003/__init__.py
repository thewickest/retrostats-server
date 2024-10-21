import roms.mameLibretro.mame2003.mslug2 as mslug2
import roms.mameLibretro.mame2003.pacman as pacman
import roms.mameLibretro.mame2003.pang as pang
import roms.mameLibretro.mame2003.xmen as xmen

def mslug2Parser(textScorePath, byteScorePath):
    mslug2.parser(textScorePath, byteScorePath)

def pacmanParser(textScorePath, byteScorePath):
    pacman.parser(textScorePath, byteScorePath)

def pangParser(textScorePath, byteScorePath):
    pang.parser(textScorePath, byteScorePath)

def xmenParser(textScorePath, byteScorePath):
    xmen.parser(textScorePath, byteScorePath)