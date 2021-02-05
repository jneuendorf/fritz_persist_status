import csv
import os.path
import sys

from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection.core.exceptions import FritzConnectionException

from fritz_persist_status.settings import settings


if __name__ == "__main__":
    try:
        status = FritzStatus()
    except FritzConnectionException as e:
        with open(settings.error_file, mode='a+') as error_file:
            error_file.write(str(e) + '\n')

    write_header = not os.path.isfile(settings.output_file)
    try:
        with open(settings.output_file, mode='a+') as output_file:
            writer = csv.writer(output_file)
            if write_header:
                writer.writerow(settings.attrs)
            writer.writerow([getattr(status, attr) for attr in settings.attrs])
    except Exception:
        with open(settings.error_file, mode='a+') as error_file:
            error_file.write(f'Could not open "{settings.output_file}"\n')
        raise


