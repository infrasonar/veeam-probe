from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query


class CheckHealth(Check):
    key = 'health'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = '/health'
        resp = await query(asset, local_config, config, req)
        entries = resp.get('entries', {})
        configuration_db = entries.get('configurationDb', {}).get('status')
        nats = entries.get('nats', {}).get('status')

        item = {
            'name': 'health',  # str
            'status': resp['status'],  # str
            'configurationDb': configuration_db,  # str?
            'nats': nats,  # str?
        }

        return {
            'health': [item]
        }
