import RegisterAssests, Buffers
import VMInit

def mov(register1: str, register2: str):
    if register1 in RegisterAssests.AviliableRegisters \
        and register2 in RegisterAssests.AviliableRegisters \
        and register1 != register2:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, register1)
        Register2: RegisterAssests.Register = getattr(RegisterAssests, register2)
        Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register1.PopContents())
        Register2.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")

def add(register1: str, register2: str):
    if register1 in RegisterAssests.AviliableRegisters \
        and register2 in RegisterAssests.AviliableRegisters \
        and register1 != register2:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, register1)
        Register2: RegisterAssests.Register = getattr(RegisterAssests, register2)
        Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register1.PopContents() + Register2.PopContents())
        Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")

def sub(register1: str, register2: str):
    if register1 in RegisterAssests.AviliableRegisters \
        and register2 in RegisterAssests.AviliableRegisters \
        and register1 != register2:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, register1)
        Register2: RegisterAssests.Register = getattr(RegisterAssests, register2)
        Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(int(Register1.PopContents()) - int(Register2.PopContents()))
        Register1.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")

def addr(register1, register2, resultRegister):
    if register1 in RegisterAssests.AviliableRegisters \
        and resultRegister in RegisterAssests.AviliableRegisters \
        and register2 in RegisterAssests.AviliableRegisters \
        and register1 != register2:
        Register1: RegisterAssests.Register = getattr(RegisterAssests, register1)
        Register2: RegisterAssests.Register = getattr(RegisterAssests, register2)
        ResultRegister: RegisterAssests.Register = getattr(RegisterAssests, resultRegister)
        Result_From_Buffer: tuple = Buffers.BufferMethods.AutoAllocate(Register1.PopContents() + Register2.PopContents())
        ResultRegister.PushContents((Result_From_Buffer[2], Result_From_Buffer[3]))
    else:
        raise NameError("Designated Register cannot be found.")
