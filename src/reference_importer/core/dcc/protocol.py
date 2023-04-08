from typing import Protocol


class DccFacade(Protocol):

    @classmethod
    def create_image_plane(cls, file) -> str:
        """Creates an image with the provided file and returns the name of the 
        image plane.

        Args:
            file (str): path to the image

        Returns:
            str: name of the object
        """
        ...
