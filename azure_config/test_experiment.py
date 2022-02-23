import logging

import mlflow

from azure_config.setup_mlflow import setup_experiment, setup_mlflow_uri
from logs.logs import setup_logging


logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()

    setup_mlflow_uri()

    setup_experiment("Test_experiment")

    logger.info("STARTING THE MLFLOW RUN")
    with mlflow.start_run():

        logger.info("LOGGING PARAMETER")
        mlflow.log_param("test_param", 1.0)

        logger.info("LOGGING ARTIFACT")
        mlflow.log_artifact("artifacts/panda.png")

        logger.info("ENDING THE MLFLOW RUN")

    logger.info("TEST COMPLETED")


if __name__ == "__main__":
    main()
