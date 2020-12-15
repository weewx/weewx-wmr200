# installer for WMR200 weather station

from weecfg.extension import ExtensionInstaller


def loader():
    return WMR200Installer()


class WMR200Installer(ExtensionInstaller):
    """Installer for the Oregon Scientific WMR200"""

    def __init__(self):
        super(WMR200Installer, self).__init__(
            version="3.5.0",
            name='wmr200',
            description='WeeWX driver for the Oregon Scientific WMR200 station',
            author="Chris Manton",
            config={
                'WMR200': {
                    'model': 'WMR200',
                    'user_pc_time': 'True',
                    'erase_archive': 'False',
                    'archive_startup': '120',
                    'archive_threshold': '1512000',
                    'sensor_status': 'True',
                    'sensor_map': {
                    }
                }
            },
            files=[
                ('bin/user', ['bin/user/wmr200.py']),
            ]
        )
