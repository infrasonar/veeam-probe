from typing import Any
from libprobe.asset import Asset
from ..query import query


async def check_health(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict[str, list[dict[str, Any]]]:
    req = '/Health'
    resp = await query(asset, asset_config, asset_config, req)
    entries = resp.get('entries', {})
    configuration_db = entries.get('configurationDb', {}).get('status')
    nats = entries.get('nats', {}).get('status')

    item = {
        'name': 'Health',  # str
        'status': resp['status'],  # str
        'configurationDb': configuration_db,  # str?
        'nats': nats,  # str?
    }

    return {
        'Health': [item]
    }
