import logging
from typing import Any, TypedDict

class SecretConfig(TypedDict):
    username: str

def run(secret_config: SecretConfig, cwd: str) -> None:
    logging.info("Hello {{ cookiecutter.project_slug | replace('-', '_')}}!")

    logging.info("Goodbye.")