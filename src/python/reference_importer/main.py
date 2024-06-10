"""Main file."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

from Qt5 import QtGui, QtQml

from ._core import VideoProcessor

if TYPE_CHECKING:
    from ._core import (
        DccFacade,
        ProcessorOptions,
        Video,
    )


def create_image_sequence(
    video: Video,
    processor_options: ProcessorOptions,
    dcc: DccFacade | None,
    create_image_plane: bool,
) -> None:
    """Creates an image sequence from a video.

    This function creates an image sequence from a video file and creates an image plane
    in the DCC if specified.

    Args:
        video: Video to process.
        processor_options: Options to process the video.
        dcc: Interface to the DCC.
        create_image_plane: If an image plane should be created in the DCC.
    """
    VideoProcessor.create_image_sequence(video, processor_options)
    if create_image_plane and dcc:
        dcc.create_image_plane(processor_options.output_file())


def run_gui() -> int:
    """Creates a  Qt application and runs the GUI.

    Returns:
        return value.
    """
    app: QtGui.QGuiApplication = QtGui.QGuiApplication(sys.argv)
    engine: QtQml.QQmlApplicationEngine = QtQml.QQmlApplicationEngine()

    source_dir: Path = Path(__file__).resolve().parent.parent.parent
    qml_dir: Path = Path(source_dir / "qml")
    main_qml_path: Path = Path(qml_dir / "main.qml")


    engine.load(str(main_qml_path))
    if not engine.rootObjects():
        sys.exit(-1)
    app.aboutToQuit.connect(engine.deleteLater)
    return app.exec_()


if __name__ == "__main__":
    pass
