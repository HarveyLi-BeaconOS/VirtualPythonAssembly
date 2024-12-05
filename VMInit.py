import Buffers, RegisterAssests, ReconfiguedPackages, pathlib

NumberedContents: dict = {}
CodeStructure: dict = {}


ReconfiguedPackages.ConsolePrint("Starting VM Initalization \n ")

Buffers.BufferInit()
RegisterAssests.RegisterInit()

ReconfiguedPackages.ConsolePrint("Starting VM Initalization DONE \n ")