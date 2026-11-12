"""Core implementation for the vellum-parser tool."""

from __future__ import annotations

import dataclasses
from typing import Iterable, Iterator


@dataclasses.dataclass
class Record:
    key: str
    payload: dict


def run(records: Iterable[Record]) -> Iterator[Record]:
    """Validate and forward records in deterministic order."""
    seen = set()
    for record in sorted(records, key=lambda item: item.key):
        if record.key in seen:
            continue
        seen.add(record.key)
        yield record
