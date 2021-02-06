import csv
from datetime import datetime
import os.path
import time

from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection.core.exceptions import FritzConnectionException

from fritz_persist_status import settings, map_value


if __name__ == "__main__":
    try:
        status = FritzStatus()
    except FritzConnectionException as e:
        with open(settings.error_file, mode='a+') as error_file:
            error_file.write(str(e) + '\n')

    write_header = not os.path.isfile(settings.output_file)
    while True:
        try:
            with open(settings.output_file, mode='a+') as output_file:
                writer = csv.writer(output_file)
                if write_header:
                    write_header = False
                    writer.writerow(['datetime', *settings.attrs])

                writer.writerow(
                    [datetime.now().isoformat()]
                    + [
                        map_value(getattr(status, attr), attr)
                        for attr in settings.attrs
                    ]
                )
            time.sleep(30)
        except Exception:
            with open(settings.error_file, mode='a+') as error_file:
                error_file.write(str(e) + '\n')


