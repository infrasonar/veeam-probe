from libprobe.asset import Asset
from libprobe.check import Check
from ..query import query_multi
from ..utils import str_to_timestamp


class CheckJobs(Check):
    key = 'jobs'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        req = '/jobs'
        results = await query_multi(asset, local_config, config, req)
        jobs = []
        for result in results:
            jobs.append({
                'name': result['id'],  # str (id)
                'displayName': result['name'],  # str (name)
                'description': result['description'],  # str
                'backupType': result['backupType'],  # str
                'schedulePolicyType': result['schedulePolicy']['type'],  # str
                'schedulePolicyScheduleEnabled':
                    result['schedulePolicy']['scheduleEnabled'],  # bool
                'schedulePolicyBackupWindowEnabled':
                    result['schedulePolicy']['backupWindowEnabled'],  # bool
                'schedulePolicyRetryEnabled':
                    result['schedulePolicy']['retryEnabled'],  # bool
                'organizationId': result['organizationId'],  # str
                'repositoryId': result['repositoryId'],  # str -> ref
                'isEnabled': result['isEnabled'],  # bool
                'nextRun': str_to_timestamp(result.get('nextRun')),  # int?
                'lastRun': str_to_timestamp(result.get('lastRun')),  # int?
                'lastBackup':
                    str_to_timestamp(result.get('lastBackup')),  # int?
                'lastStatus': result.get('lastStatus'),  # str?
                'eTag': result['eTag'],  # int
            })

        req = '/backupRepositories'
        results = await query_multi(asset, local_config, config, req)
        backup_repositories = []
        for result in results:
            backup_repositories.append({
                'name': result['id'],  # str (id)
                'displayName': result['name'],  # str (name)
                'capacityBytes': result['capacityBytes'],  # int
                'freeSpaceBytes': result['freeSpaceBytes'],  # int
                'description': result['description'],  # str
                'path': result['path'],  # str
                'retentionType': result['retentionType'],  # str
                'retentionPeriodType': result['retentionPeriodType'],  # str,
                'isOutdated': result['isOutdated'],  # bool
                'isOutOfSync': result['isOutOfSync'],  # bool
                'isIndexed': result['isIndexed'],  # bool
                'isOutOfOrder': result['isOutOfOrder'],  # bool
            })

        return {
            'jobs': jobs,
            'backupRepositories': backup_repositories,
        }
