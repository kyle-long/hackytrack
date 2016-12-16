import datetime
from hackytrack.record_tag import RecordTag
from hackytrack.record import Record
import re


class RecordListInterpreter(object):
    def __init__(self, record_list):
        self.record_list = record_list
        self.top_record_tag = RecordTag()

    def process(self):
        """
            The main function to process all the
            records and put them into a format that
            is more easily consumable.
        """
        for record in self.record_list:
            self._process_record(record)

    def _process_record(self, r):
        """
            Takes a single record and uses it to add
            to the record_tags dict and add its delta to
            the total.

            Example of record:
            {
                "start": "2016-06-21T15:36:25.517011",
                "end": "2016-06-21T16:00:26.468865",
                "name": "TAG_NAME: more description",
                "elapsed": "0:24:00.951854"
            }

            Args:
               r(dict)
        """
        if "elapsed" not in r:
            return

        key = ""
        name = r["name"]
        if ":" in name:
            key = re.search(".*?(?=:)", name).group(0)

        elapsed = r["elapsed"]
        delta = self._to_delta(elapsed)
        record = Record(name, delta)
        self.top_record_tag.add(key, record)

    def _to_delta(self, elapsed):
        """
            Turns a elapsed time string into a
            datetime.timedelta so it can be used
            to add or subtract.

            Args:
                elapsed(basestring)

            Returns:
                datetime.timedelta
        """
        d = datetime.datetime.strptime(elapsed, "%H:%M:%S.%f")
        delta = datetime.timedelta(hours=d.hour, minutes=d.minute, seconds=d.second, microseconds=d.microsecond)
        return delta
