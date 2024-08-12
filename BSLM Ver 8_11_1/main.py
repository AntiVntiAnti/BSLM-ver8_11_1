from PyQt6.QtWidgets import QApplication
from ui.app import MainWindow
import sys
from logger_setup import logger
from ui.main_ui import res
# pyrcc5 resources.qrc -o resources.py  DON'T FORGET this ya dope! :D


def run_app():
    """
    Runs the application.

    This function initializes the application, creates the main window,
    and starts the event loop.

    Raises:
        Exception: If an error occurs during the execution of the application.
    """
    logger.debug("ENTER BY PORTAL START YES!")
    try:
        app = QApplication(sys.argv)
        # app.setStyleSheet(homie_stylesheet)
        window = MainWindow()
        window.show()
        window.resize(300, 330)
        sys.exit(app.exec())
    except (ValueError, TypeError) as e:
        logger.error(f"Value or Type error occurred {e}", exc_info=True)
    except ImportError as e:
        logger.error(f"Import error occurred {e}", exc_info=True)
    except OSError as e:
        logger.error(f"OS error occurred {e}", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error occurred {e}", exc_info=True)


if __name__ == "__main__":
    run_app()
