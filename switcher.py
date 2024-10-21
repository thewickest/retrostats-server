from roms.mameLibretro import mame2003

class Switcher(object):
    def hiToText(self, textScorePath, byteScorePath, gameName):
        methodName = f'{gameName}Parser'
        if hasattr(self, methodName) and callable(method := getattr(self, methodName)):
            return method(textScorePath, byteScorePath)