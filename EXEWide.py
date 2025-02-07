# EXEWide.py
# Convert "Spider-Man" (2002) EXEs to support widescreen (16:9).
# Feb-2025 @CelestialAddy

import os

WideOffset = 4810360

Valid = False
while not Valid:
    Path = input("Path to game EXE (will be overwritten)? ")
    if os.path.exists(Path): Valid = True
    else: print("Doesn't appear to exist. Try again.")

try:
    EXEf = open(Path, "rb")
    EXEb = bytearray(EXEf.read())
    EXEf.close()
except:
   input("Input acquisition error.\n")
   exit(0)

try:
    EXEb[WideOffset+0] = 0
    EXEb[WideOffset+1] = 0
    EXEb[WideOffset+2] = 190
    EXEb[WideOffset+3] = 60
except:
    input("Executable interaction error.\n")
    exit(0)

try:
    EXE = open(Path, "wb")
    EXE.write(EXEb)
    EXE.close()
    input("Done!\n")
except:
    input("Output data error.\n")
    exit(0)

# End.
