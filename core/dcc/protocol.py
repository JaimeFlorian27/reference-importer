from typing import Protocol


class DccFacade(Protocol):
    def create_image_plane(self, file) -> str:
        ...
