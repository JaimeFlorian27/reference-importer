"""Main module of the package, defines aliases for easy import to api classes."""

from ._core import (
    DccError,
    DccFacade,
    ProcessorOptions,
    Timecode,
    Video,
    VideoError,
    VideoMetadata,
    VideoProcessor,
    get_current_dcc,
)
from .main import create_image_sequence, run_gui
