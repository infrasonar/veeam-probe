from libprobe.probe import Probe
from lib.check.jobs import CheckJobs
from lib.check.health import CheckHealth
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckJobs,
        CheckHealth,
    )

    probe = Probe("veeam", version, checks)

    probe.start()
