import os

ENV = os.getenv("ENV")
if ENV is None:
    ENV = "dev"  # safe default for local/deploy-time only

BRONZE_CATALOG_NAME = f""


STORAGE_ACCOUNT_MAP = {
    "dev": "",
    "val": "",
    "prod": "",
}

STORAGE_ACCOUNT_ID = STORAGE_ACCOUNT_MAP.get(ENV)
if STORAGE_ACCOUNT_ID is None:
    raise ValueError(f"Unknown ENV: {ENV!r}. Expected: dev, val, prod")

match ENV:
    case "dev":
        EXTERNAL_CATALOG_NAME = ""
        SHARED_MULTI_NODE_CLUSTER_ID = ""
        SERVICE_PRINCIPAL_DBS = ""
        env = "dev"
 

    case "qa":
        SHARED_MULTI_NODE_CLUSTER_ID = ""
        SERVICE_PRINCIPAL_DBS = ""
        env = "qa"



    case "prod":
        SHARED_MULTI_NODE_CLUSTER_ID = ""
        SERVICE_PRINCIPAL_DBS = ""


    case _:
        raise ValueError(f"Unknown ENV: {ENV!r}")

# Computed paths
DBS_MANUAL_VOLUME_PATH = (
    f""
    f""
)