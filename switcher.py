from roms.mameLibretro import mame2003

class Switcher(object):
    def hiToText(self, textScorePath, byteScorePath, gameName):
        methodName = f'{gameName}Parser'
        # TODO this is better but should be totaly dynamic
        if hasattr(mame2003, methodName) and callable(method := getattr(mame2003, methodName)):
            return method(textScorePath, byteScorePath)