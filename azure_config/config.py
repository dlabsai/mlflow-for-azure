from typing import Optional

from pydantic import BaseSettings


class AzureConfig(BaseSettings):
    subscription_id: Optional[str]
    resource_group: Optional[str]
    workspace_name: Optional[str]

    class Config:
        env_prefix: str = "azure_"
