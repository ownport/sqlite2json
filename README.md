# sqlite2json

Simple script for returning SQL query result as JSONline 

## How to use

```
./sqlite2json --help
usage: sqlite2json [-h] --database DATABASE --sql SQL
                   [--fetch-size FETCH_SIZE] [--udf UDF]

optional arguments:
  -h, --help            show this help message and exit
  --database DATABASE   the path to sqlite3 database
  --sql SQL             SQL query
  --fetch-size FETCH_SIZE
                        Fetch size, default: 1000 records
  --udf UDF             Custom UDF functions, the format fieldname:udf
```

## Examples

simple query
```
.sqlite2json --database metrics.sqlite3 --sql "SELECT * FROM sqlite_master;"
{"type": "table", "tbl_name": "definitions", "rootpage": 2, "name": "definitions", "sql": "CREATE TABLE definitions (v)"}
{"type": "table", "tbl_name": "metrics", "rootpage": 3, "name": "metrics", "sql": "CREATE TABLE metrics (metric_id, value)"}
```

query with udf
```
./sqlite2json --database metrics.sqlite3 \
    --sql "SELECT metric_id, group_concat(value) AS values FROM (SELECT metric_id, value FROM metrics LIMIT 10) GROUP BY metric_id;" \
    --udf "values:'{}'.split(',')"
    
{"metric_id": 100, "values": ["10", "14", "51", "62", "37", "18", "91"]}
{"metric_id": 815, "values": ["12", "34", "25", "65", "71", "86", "95"]}
```


