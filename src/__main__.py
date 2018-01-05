#!/usr/bin/env python3

import os
import sys
import json
import logging
import sqlite3
 

logger = logging.getLogger(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 
def sqlite2json(db, query, udfs=dict()):

    if not os.path.isfile(db):
        logger.error('The database does not exist, {}'.format(db))
        sys.exit(1)

    connection = sqlite3.connect(db)
    connection.row_factory = dict_factory    
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor.fetchall():
        for fname in set(row.keys()).intersection(udfs.keys()):
            row[fname] = eval(udfs[fname].format(row[fname]))
        print(json.dumps(row))
    connection.close()


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--database', required=True, help='the path to sqlite3 database')
parser.add_argument('--sql', required=True, help='SQL query')
parser.add_argument('--udf', action='append', help='Custom UDF functions, the format fieldname:udf')
args = parser.parse_args()

udfs = dict()
if args.udf:
    udfs = dict([udf.split(':',1) for udf in args.udf])

sqlite2json(args.database, args.sql, udfs)
    