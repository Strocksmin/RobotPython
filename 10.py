def transpose(table):
    response = []
    for i in range(len(table[0])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def delete_duplicate_rows(table):
    new_dict = {x[3]: x for x in table}
    return list(new_dict.values())


def delete_duplicate_columns(table):
    for row in table:
        del row[2]
    return table


def transformer(i, value):
    if i == 0:
        replaced = value.replace('-', '').replace('-', '')
        return replaced[4:]
    if i == 1:
        return "Y" if value == "true" else "N"
    if i == 2:
        digit = float(value)
        return f'{digit:.4f}'


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(i, table[i][j])
    return table


def main(table):
    return transform(transpose(delete_duplicate_columns
                               (delete_duplicate_rows(table))))
