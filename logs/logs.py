import logging
import logging.config
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging() -> None:
    here = Path(__file__).parent
    logging.config.fileConfig(here / "logging.conf", disable_existing_loggers=False)
    logger.info("Logging configured")


def setup_logging_for_click() -> None:
    here = Path(__file__).parent
    logging.config.fileConfig(
        here / "logging.click.conf", disable_existing_loggers=False
    )
