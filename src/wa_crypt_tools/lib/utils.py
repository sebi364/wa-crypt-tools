from javaobj.v2.beans import JavaArray

import logging
l = logging.getLogger(__name__)
def hexstring2bytes(string: str) -> bytes:
    """Converts a hex string into a bytes array"""
    if len(string) != 64:
        l.critical("The key file specified does not exist.\n    "
                 "If you tried to specify the key directly, note it should be "
                 "64 characters long and not {} characters long.".format(len(string)))

    barr = None
    try:
        barr = bytes.fromhex(string)
    except ValueError as e:
        l.critical("Couldn't convert the hex string.\n    "
                 "Exception: {}".format(e))
    if len(barr) != 32:
        l.error("The key is not 32 bytes long but {} bytes long.".format(len(barr)))
    return barr

def javaintlist2bytes(barr: JavaArray) -> bytes:
    """Converts a javaobj bytearray which somehow became a list of signed integers back to a Python byte array"""
    out: bytes = b''
    for i in barr:
        out += i.to_bytes(1, byteorder='big', signed=True)
    return out