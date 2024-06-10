from __future__ import annotations

from .protocol import DccError, DccFacade


def get_current_dcc() -> DccFacade:
    """Returns the current DCC facade.

    Raises:
        DccError: When no DCC is found.

    Returns:
        DccFacade: Facade object to interface with current DCC.
    """
    try:
        from .maya import MayaFacade
    except ImportError:
        pass
    else:
        return MayaFacade

    _err_msg = "No DCC found."
    raise DccError(_err_msg)
