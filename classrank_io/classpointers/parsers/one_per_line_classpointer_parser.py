from classrank_io.classpointers.parsers.classpointer_parser_interface import ClasspointerParserInterface


class OnePerLineClasspointerParser(ClasspointerParserInterface):

    def __init__(self, source_file=None, raw_string=None):
        super(OnePerLineClasspointerParser, self).__init__()
        self._source_file = source_file
        self._raw_string = raw_string
        self._err_count = 0
        self._line_count = 0


    def parse_classpointers(self):
        if self._source_file is not None:
            return self._parse_file()
        else:
            return self._parse_raw_string()

    def _parse_raw_string(self):
        result = set()
        for a_line in self._raw_string.split("\n"):
            # print a_line
            a_classpointer = self._get_classpointer_from_line(a_line)
            # print a_classpointer
            if a_classpointer is not None:
                self._line_count += 1
                result.add(a_classpointer)
                # print a_classpointer

            else:
                self._err_count += 1
        # print result
        return result

    def _parse_file(self):
        result = set()
        with open(self._source_file, "r") as input_io:
            for a_line in input_io:
                a_classpointer = self._get_classpointer_from_line(a_line)
                if a_classpointer is not None:
                    self._line_count += 1
                    result.add(a_classpointer)
                else:
                    self._err_count += 1
        return result

    def _get_classpointer_from_line(self, a_line):
        result = a_line.strip()
        if result not in ["", None]:
            return result
        return None


