"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import envpulse


def test_version_is_set() -> None:
    assert envpulse.__version__
