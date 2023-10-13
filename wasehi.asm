.386
.model flat, stdcall

.data
.code
main PROC
    ; Load the first number (num1) into EAX
        mov eax, 3
        mov ebx, 4
    ; Add the second number (num2) to EAX
        add eax, ebx

        ret
main ENDP

END main