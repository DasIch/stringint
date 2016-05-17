"""
    test_stringint
    ~~~~~~~~~~~~~~

    :copyright: 2016 by Daniel Neuhäuser
    :license: BSD, see LICENSE.rst for details
"""
import os
import random

import pytest

from stringint import bytes_to_int, int_to_bytes


@pytest.fixture(params=[
    # important edge cases to consider
    b'',
    b'\x00',
    b'\xff',
    # truly random bytes
    *[os.urandom(random.choice(range(10))) for _ in range(10)]
])
def rbytes(request):
    return request.param


def test_reversable(rbytes):
    int = bytes_to_int(rbytes)
    assert int_to_bytes(int) == rbytes


def test_size(rbytes):
    int = bytes_to_int(rbytes)
    # we need an additional bit to disambiguate between b'' and b'\x00'
    assert int.bit_length() == len(rbytes) * 8 + 1
