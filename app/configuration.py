import json
from pathlib import Path
from typing import Any, Dict

import sys_vars


__all__ = ["get_app_config", "get_app_config_file"]


def get_app_config_file(env: str) -> str:
    """Determine the appropriate config file for the environment.

    @param {str} env - The currently set value of ENV.
    @return {str} - The config file name for the environment.
    """
    return f"{env}.json"


def get_app_config(config_file: str) -> dict:
    """Collect the app configuration values.

    @param {str} config_file - The config file name to use.
    @return {dict} - A dictionary with all config values.
    """
    path = Path(f"configuration/{config_file}").resolve()
    file_content = json.loads(path.read_text())

    # Immediately add the app-specific values to the final values
    # because there is no need to fetch these from an outside source
    app_config: Dict[str, Any] = {}
    app_config.update(file_content["appConfig"])

    # Now fetch the system variable stored in a outside source
    # if they are defined at all
    system_vars = file_content.get("env", []) + file_content.get("secrets", [])
    for var in system_vars:
        app_config[var] = sys_vars.get(var)

    return app_config
