class AnalyzeView(object):
    """
        Responsible for creating a string of output
        in various ways.
    """

    def __init__(self, total, record_tag_list):
        """
            Args:
                total(datetime.timedelta)
                record_tag_list(List[hackytrack.record_tag.RecordTag)
        """
        self.record_tag_list = record_tag_list
        self.total = total

    def get_tag_total(self):
        output = ""

        for tag in self.record_tag_list:
            output += "{0}: {1}\n".format(tag.name, tag.total)

        output = self._add_total(output)
        return output

    def get_combined_names(self):
        output = ""

        for tag in self.record_tag_list:
            output += "{0}: {1}\n".format(tag.name, tag.total)

            for item in tag.combined_name_list:
                output += "\t{0}: {1}\n".format(item["name"], item["delta"])

        output = self._add_total(output)

        return output

    def _add_total(self, output):
        output += "Total: {0}".format(self.total)
        return output
