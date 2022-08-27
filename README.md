# MyRDBMS

RDBMSのJOINSなどを模したやつです

```sh
$ python3 test.py
```

```python
import table_schema
import joins

f = open('samples/addresses.csv')
addresses = table_schema.get_schema_from_csv(f)

f = open('samples/postals.csv')
postals = table_schema.get_schema_from_csv(f)

l_addresses = joins.left_outer_join(
    addresses, 'addresses.State Code',
    postals, 'postals.Alpha code'
)
result = joins.select(l_addresses, ['addresses.*', 'postals.State'])
c = result.to_csv()
print(c)
```

## Ref

ここで説明しています

- https://zenn.dev/harukaeru/articles/207812eb1fc7ef
