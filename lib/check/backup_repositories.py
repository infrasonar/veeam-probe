from typing import Any
from libprobe.asset import Asset
from ..query import query


async def check_backup_repositories(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict[str, list[dict[str, Any]]]:
    req = '/BackupRepositories'
    resp = await query(asset, asset_config, asset_config, req)

    return resp
