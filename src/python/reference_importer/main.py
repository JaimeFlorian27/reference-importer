"""Main file."""
import sys
from pathlib import Path

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


def main() -> int:
    """Creates a qml window.

    Returns:
        return value.
    """
    app: QGuiApplication = QGuiApplication(sys.argv)
    engine: QQmlApplicationEngine = QQmlApplicationEngine()

    source_dir: Path = Path(__file__).parent.parent.parent
    qml_dir: Path = Path(source_dir / "qml")
    main_qml_path: Path = Path(qml_dir / "main.qml")

    engine.load(str(main_qml_path))
    if not engine.rootObjects():
        sys.exit(-1)
    app.aboutToQuit.connect(engine.deleteLater)
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
