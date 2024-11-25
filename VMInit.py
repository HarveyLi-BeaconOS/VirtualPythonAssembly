import Buffers, RegisterAssests, ReconfiguedPackages, pathlib

NumberedContents: dict = {}
CodeStructure: dict = {}

with open(pathlib.Path("entry.vm_asm"), 'r') as entry_file:
    LineCounter: int = 0
    for x in entry_file.readlines():
        LineCounter+=1
        NumberedContents.update({x[:-1]:LineCounter})

for x in list(NumberedContents.keys()):
    if ":" in x:
        CodeStructure.update({x: NumberedContents[x]})


ReconfiguedPackages.ConsolePrint("Starting VM Initalization \n ")

Buffers.BufferInit()
RegisterAssests.RegisterInit()

ReconfiguedPackages.ConsolePrint("Starting VM Initalization DONE \n ")