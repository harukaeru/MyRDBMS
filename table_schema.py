import io
import csv

class TableSchema:
    def __init__(self):
        self.table_name = None
        self.header = []
        self.rows = []

    def __str__(self):
        return f'<header: {self.header}, rows: {self.rows}'

    def from_csv(self, csv_file, has_header=True, table_name=None):
        self.table_name = table_name if table_name else csv_file.name.split('/')[-1].split('.')[0]
        self.header = []
        self.rows = []

        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if has_header and i == 0:
                self.header = row
            elif not has_header and i == 0:
                self.header = map(str, range(len(row)))
            else:
                if len(row) != len(self.header):
                    raise Exception('Invalid row count')
                self.rows.append(row)
        self.header = [self.table_name + '.' + h for h in self.header]

    def to_csv(self, filename=None):
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(self.header)
        writer.writerows(self.rows)
        if filename:
            with open(filename, 'w') as f:
                f.write(output.getvalue())
            return 'Written!'
        else:
            return output.getvalue()


def get_schema_from_csv(csv_file, has_header=True):
    table_schema = TableSchema()
    table_schema.from_csv(csv_file, has_header)
    return table_schema
