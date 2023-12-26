from gsheetsdb import connect
import requests

conn = connect()
def SaeeAM_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows



