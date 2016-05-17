"""
    stringint
    ~~~~~~~~~

    :copyright: 2016 by Daniel Neuhäuser
    :license: BSD, see LICENSE.rst for details
"""


def bytes_to_int(bytes):
    """
    Takes a byte string and returns an unsigned int.
    """
    result = 1
    for byte in bytes:
        result = result * 256 + byte
    return result


def int_to_bytes(int):
    """
    Takes an unsigned int as returned by `bytes_to_int` and turns it into a
    byte string again.
    """
    result = bytearray()
    while int > 1:
        int, byte = divmod(int, 256)
        result.append(byte)
    return bytes(result[::-1])
