import datetime
from hackytrack.record import Record


class RecordTag(object):
    def __init__(self, tag=""):
        self.tag = tag.strip()
        self.record_tag_list = []
        self.record_list = []

    @property
    def total(self):
        total = datetime.timedelta()
        combine_list = self.record_tag_list + self.record_list
        for item in combine_list:
            total += item.total

        return total

    @property
    def combine_record_list(self):
        combine_list = []
        for record in self.record_list:
            combine_record = self._find_existing_record(record, combine_list)

            if not combine_record:
                combine_record = Record(record.name)
                combine_list.append(combine_record)

            combine_record.add(record)

        return combine_list

    def _find_existing_record(self, record, record_list):
        for r in record_list:
            if r.name == record.name:
                return r

    def add(self, tag, record):
        record_tag = self.add_tag(tag)
        record_tag.record_list.append(record)

    def add_tag(self, tag):
        tag = tag.strip()

        if not tag:
            tag = "OTHER"

        if ">" in tag:
            highest_tag = tag[:tag.index(">")].strip()
            record_tag = self._add_existing_tag(highest_tag)

            # Whats left of the tag after removing the first tag.
            remaining_tag = tag[tag.index(">") + 1:].strip()
            if remaining_tag:
                record_tag = record_tag.add_tag(remaining_tag)
        else:
            record_tag = self._add_existing_tag(tag)

        return record_tag

    def _add_existing_tag(self, tag):
        record_tag = self._find_existing_record_tag(tag)
        if not record_tag:
            record_tag = RecordTag(tag)
            self.record_tag_list.append(record_tag)

        return record_tag

    def _find_existing_record_tag(self, tag):
        for record_tag in self.record_tag_list:
            if record_tag.tag == tag:
                return record_tag
