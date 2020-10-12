#!/usr/bin/python3
"""Centos7."""
from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus


class Centos7(CharmBase):
    """A rudimentary charm used to deploy centos7."""

    def __init__(self, *args):
        super().__init__(*args)
        # Observe the start event so we can set the status.
        self.framework.observe(self.on.start, self._on_start)

    def _on_start(self, event):
        # Set the charm status.
        self.unit.status = ActiveStatus()


if __name__ == "__main__":
    main(Centos7)
