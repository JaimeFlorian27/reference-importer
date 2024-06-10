from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pathlib import Path


class DccError(Exception):
    """Base class for DCC exceptions."""


class DccFacade(Protocol):
    @classmethod
    def create_image_plane(cls, file: Path) -> str:
        """Creates an image with the provided file.

        Args:
            file: path to the image

        Returns:
            str: name of the object
        """
        ...
