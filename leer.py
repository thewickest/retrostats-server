with open("/home/pi/RetroPie/roms/neogeo/fbneo/mslug.fs","rb") as f:
    byte = "empty"
    while byte:
        byte = f.read(8)
        print(byte.hex())
f.close()