"""
A Simple Power Control Request module for accessing the Windows API to acquire wakelocks
and other power mode control requests.

Copyright (C) 2025 - Ziad (Mr.X)'s Software

Licensed under the same license as Temp_Cleaner GUI

The goals of this module are:

* To provide necessary constants for power request types

* To provide necessary functions for calling, releasing power control requests

In order to properly acquire and release a power control request, the following steps must be precisely followed:

* Create a power request control object instance, by storing the return value of the function createPowerRequest() into a variable

* Use the power request control object instance you just created to actually make system calls to a power request control, by calling the function
modifyPowerRequest() against the power request control object and specify the power request control type.

* After you finish the execution of all functions that require the power control request (or the wakelock), release the power control request by
using the function clrPowerRequest() against the power request control object and specify the power request control type.

* DO NOT FORGET to close the power request control object handle (or instance) by calling the function closeHandle() against the power control request object
you made in the first step.
"""
import ctypes.wintypes
import ctypes

# Detailed REASON_CONTEXT Structure, not needed for now.
# class Detailed(ctypes.Structure):
#     _fields_ = [
#         ("LocalizedReasonModule", ctypes.wintypes.HMODULE),
#         ("LocalizedReasonId", ctypes.wintypes.ULONG),
#         ("ReasonStringCount", ctypes.wintypes.ULONG),
#         ("ReasonStrings", ctypes.pointer(ctypes.wintypes.LPWSTR))
#     ]

class Reason(ctypes.Union):
    _fields_ = [
        ("SimpleReasonString", ctypes.wintypes.LPWSTR)
        # other fields
        # ('d', Detailed)
    ]

class REASON_CONTEXT(ctypes.Structure):
    pass
REASON_CONTEXT._fields_ = [
    ("Version", ctypes.wintypes.ULONG),
    ("Flags", ctypes.wintypes.DWORD),
    ('r', Reason)
]

# Power Request Types
# System Required Power Control Request Type
POWER_REQUEST_SYSTEM_REQUIRED: int = 1
# Display Required Power Control Request Type, Used to prevent monitor from going to sleep
# or to prevent operating system from turning off the display during inactivity after timeout
# specified in Control Panel > Power Options
POWER_REQUEST_DISPLAY_REQUIRED: int = 0
# Away Mode Power Control Request Type, Used to allow the computer to fully enter away mode
# but keep processor and background services running to make sure tasks will perform correctly.
POWER_REQUEST_AWAYMODE_REQUIRED: int = 2
# Execution Power Control Request Type
POWER_REQUEST_EXECUTION_REQUIRED: int = 3


def createPowerRequest(reasonString: str):
    """
    Creates and returns a Power Request object, with the string reason specified at reasonString parameter
    """
    _reason: REASON_CONTEXT = REASON_CONTEXT()
    _reason.Version = ctypes.wintypes.ULONG(0)
    _reason.Flags = 1
    _reason.r.SimpleReasonString = str(reasonString)
    return ctypes.windll.kernel32.PowerCreateRequest(_reason)

def modifyPowerRequest(pwrReqObj, reqType) -> bool:
    """
    Modifies a Power Request Object, is also used to initiate a power control request.

    Required parameters:

    pwrReqObj: a Power Request Object

    reqType: a constant integer representing the type of the power control request

    This function returns True if the modification is successfully done, False otherwise.
    """
    _setResult = ctypes.windll.kernel32.PowerSetRequest(pwrReqObj, reqType)
    if _setResult != 0:  # function returns 0 on failure
        return True
    else:
        return False
    return False

def clrPowerRequest(pwrReqObj, reqType) -> bool:
    """
    Clears the Power Control request

    Required arguments: 

    pwrReqObj: an object returned by the function createPowerRequest() that is, originally, a Power Control Request object.

    reqType: a constant integer representing the type of the power control request.

    This function returns True when it successes to clear the power control request, and False otherwise.
    """
    clearResult = ctypes.windll.kernel32.PowerClearRequest(pwrReqObj, reqType)
    if clearResult != 0: # wakelock released!
        return True
    else:
        return False
    return False

def closeHandle(handle) -> bool:
    """
    Closes a handle specified at parameter handle

    handle: a Power Control request Object

    this returns True if it successed to close the handle, False otherwise
    """
    _retval: int = ctypes.windll.kernel32.CloseHandle(handle)
    if _retval != 0: # success
        return True
    else:
        return False
    return False


if __name__ == '__main__':
    pass