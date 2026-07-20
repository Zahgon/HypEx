from __future__ import annotations

from functools import wraps
from typing import Any, Callable, cast

from hypex.utils import DecoratedType, DocstringInheritDecorator


def inherit_docstring_from(
    source: Callable[..., Any] | property,
) -> DocstringInheritDecorator:
    pass
