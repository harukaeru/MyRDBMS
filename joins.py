from table_schema import TableSchema

def left_outer_join(left_table_schema, left_column_name, right_table_schema, right_column_name, table_name=None):
    left_header = left_table_schema.header
    right_header = right_table_schema.header
    left_idx = left_header.index(left_column_name)
    right_idx = right_header.index(right_column_name)

    result_table_schema = TableSchema()
    result_table_schema.table_name = table_name if table_name else left_table_schema.table_name + '__' + right_table_schema.table_name
    result_table_schema.header = left_header + right_header
    result_table_schema.rows = []
    for outer_row in left_table_schema.rows:
        on_left = outer_row[left_idx]

        found = False
        for inner_row in right_table_schema.rows:
            on_right = inner_row[right_idx]
            if on_left == on_right:
                found = True
                result_row = outer_row + inner_row
                result_table_schema.rows.append(result_row)
            else:
                continue
        if not found:
            result_row = outer_row + [None] * len(right_header)
            result_table_schema.rows.append(result_row)
    return result_table_schema

def select(original_table_schema, column_names):
    result_table_schema = TableSchema()
    result_table_schema.table_name = 'selected__' + original_table_schema.table_name
    result_table_schema.header = []

    header_idxs = []
    for column_name in column_names:
        if '*' in column_name:
            for i, header_column in enumerate(original_table_schema.header):
                if header_column.startswith(column_name.split('*')[0]) and i not in header_idxs:
                    result_table_schema.header.append(header_column)
                    header_idxs.append(i)
        else:
            i = original_table_schema.header.index(column_name)
            if i not in header_idxs:
                result_table_schema.header.append(column_name)
                header_idxs.append(i)

    result_table_schema.rows = [[row[idx] for idx in header_idxs] for row in original_table_schema.rows]

    return result_table_schema
