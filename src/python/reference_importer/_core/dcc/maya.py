from pathlib import Path

from maya import cmds


class MayaFacade:
    @classmethod
    def create_image_plane(cls, file: Path) -> str:
        """Creates an image with the provided file .

        Args:
            file (str): path to the image

        Returns:
            str: name of the object
        """
        file = Path(str(file).replace("%03d", "001"))
        image_plane = cmds.imagePlane(fn=str(file))
        cmds.setAttr(f"{image_plane[0]}.useFrameExtension", True)

        return image_plane
