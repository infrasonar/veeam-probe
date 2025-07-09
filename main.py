from libprobe.probe import Probe
from lib.check.backup_repositories import check_backup_repositories
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'BackupRepositories': check_backup_repositories,
    }

    probe = Probe("veeam", version, checks)

    probe.start()
