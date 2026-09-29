from databricks.bundles.core import (
    Bundle,
    Resources,
    load_resources_from_current_package_module,
    load_resources_from_package_module,
)
import importlib


def load_resources(bundle: Bundle) -> Resources:
    """
    'load_resources' function is referenced in databricks.yml and is responsible for loading
    bundle resources defined in Python code. This function is called by Databricks CLI during
    bundle deployment. After deployment, this function is not used.
    """

    if bundle.target == "dev_local":
        local_module = importlib.import_module("dev_local_jobs")
        return load_resources_from_package_module(local_module)
    else:
        return load_resources_from_current_package_module()