from maya import cmds


class MayaFacade:

    @classmethod
    def create_image_plane(cls, file) -> str:
        """Creates an image with the provided file and returns the name of the
        image plane.

        Args:
            file (str): path to the image

        Returns:
            str: name of the object
        """
        file = file.replace("%03d", "001")
        image_plane = cmds.imagePlane(fn=file)
        cmds.setAttr("%s.useFrameExtension" % image_plane[0], True)

        return image_plane
