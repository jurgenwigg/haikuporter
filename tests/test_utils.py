# Copyright 2023 @jurgenwigg
# Distributed under the terms of the MIT License.
"""Unit tests for the Utils.py module."""
import pytest
from HaikuPorter.Utils import ThreadFilter

# Define variables used during the test
IDENT: int = 1234
BUILD: dict = {"lines": 0}
EXPECTED_BUILD: dict = {"lines": 1}


@pytest.fixture(scope="function")
def thread_filter():
    """Initialises ThreadFilter() object."""
    return ThreadFilter()


def test_init():
    """Tests if ThreadFilter() initialises properly."""
    result = ThreadFilter()
    assert result.build is None and isinstance(result.ident, int)


def test_reset(thread_filter):
    """Tests if ThreadFilter().reset() works properly."""
    thread_filter.ident = IDENT
    thread_filter.reset()
    assert thread_filter.ident != IDENT


def test_setbuild(thread_filter):
    """Tests if setBuild works."""
    build_init = thread_filter.build
    thread_filter.setBuild(BUILD)
    assert (
        build_init != thread_filter.build
        and thread_filter.build == BUILD
        and isinstance(thread_filter.build, dict)
    )


def test_filter_build_not_set(thread_filter):
    """Tests if filter() behaves as expected."""
    thread_filter.ident = IDENT
    assert not thread_filter.filter("")


def test_filter_build_set_different_ident(thread_filter):
    """Tests if filter() behaves as expected."""
    thread_filter.ident = IDENT
    thread_filter.setBuild(BUILD)
    res = thread_filter.filter("")
    assert not res and thread_filter.build == BUILD


def test_filter_build_set_same_ident(thread_filter):
    """Tests if filter() behaves as expected."""
    thread_filter.setBuild(BUILD)
    result = thread_filter.filter("")
    assert result and thread_filter.build == EXPECTED_BUILD
