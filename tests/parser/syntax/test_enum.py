
import pytest

from vyper import compiler
from vyper.exceptions import (
    ArgumentException,
    InvalidReference,
    StructureException,
    TypeMismatch,
    UnknownAttribute,
)

valid_list = [
    """
enum Action:
    buy
    sale
    """
]

@pytest.mark.parametrize("good_code", valid_list)
def test_enum_success(good_code):
    assert compiler.compile_code(good_code) is not None