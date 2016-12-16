class AnalyzeView(object):
    """
        Responsible for creating a string of output
        in various ways.
    """

    def __init__(self, top_record_tag):
        """
            Args:
                total(datetime.timedelta)
                top_record_tag(hacktrack.record_tag.RecordTag)
        """
        self.top_record_tag = top_record_tag
        self.total = top_record_tag.total

    def get_tag_total(self):
        output = []

        for tag in self.top_record_tag.record_tag_list:
            output.append("{0}: {1}".format(tag.tag, tag.total))

        output.append(self._get_total())
        return "\n".join(output)

    def get_combined_items(self):
        output = []
        for record_tag in self.top_record_tag.record_tag_list:
            self._generate_record_tag("", output, True, record_tag)

        output.append(self._get_total())

        return "\n".join(output)

    def get_individual_items(self):
        output = []
        for record_tag in self.top_record_tag.record_tag_list:
            self._generate_record_tag("", output, False, record_tag)

        output.append(self._get_total())

        return "\n".join(output)

    def _generate_record_tag(self, indent, output, combine, record_tag):
        output.append("{}{}: {}".format(indent, record_tag.tag, record_tag.total))
        new_indent = "{}{}".format("\t", indent)

        record_list = record_tag.record_list

        if combine:
            record_list = record_tag.combine_record_list

        for record in record_list:
            output.append("{}{}: {}".format(new_indent, record.description, record.total))

        for sub_tag in record_tag.record_tag_list:
            self._generate_record_tag(new_indent, output, combine, sub_tag)

    def _get_total(self):
        return "Total: {}".format(self.total)
