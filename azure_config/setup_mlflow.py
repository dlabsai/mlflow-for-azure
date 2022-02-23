import logging

import mlflow
from azureml.core import Workspace

from azure_config.config import AzureConfig


logger = logging.getLogger(__name__)


def setup_mlflow_uri() -> None:
    logger.debug("Setting up mlflow uri.")
    azure_config = AzureConfig()
    if (
        azure_config.resource_group
        and azure_config.subscription_id
        and azure_config.workspace_name
    ):
        azure_workspace = Workspace(
            subscription_id=azure_config.subscription_id,
            resource_group=azure_config.resource_group,
            workspace_name=azure_config.workspace_name,
        )

        mlflow.set_tracking_uri(azure_workspace.get_mlflow_tracking_uri())
        logger.info("Set up remote Azure ML mlflow.")
    else:
        logger.info("Set up local mlflow.")


def setup_experiment(experiment_name: str) -> None:
    logger.debug(f"Setting up mlflow experiment: {experiment_name}.")
    existing_experiment = mlflow.get_experiment_by_name(experiment_name)

    if existing_experiment is None:
        mlflow.create_experiment(name=experiment_name)
        logger.info(f"Created new experiment: {experiment_name}.")
    else:
        mlflow.set_experiment(experiment_name=experiment_name)
        logger.info(f"Set up existing experiment: {experiment_name}.")
