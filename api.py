from google.cloud import bigquery
import os

credentials_path = 'C:/Users/arthur.boyer/google data studio/pythonKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'stage-psud.test.garden-sensor'

rows_to_insert = [
    {u'sensorName':'garden-001', u'temperature':88.0, u'humidity':32.1},
    {u'sensorName':'garden-002', u'temperature':90.2, u'humidity':34.0},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print('New rows have been added.')
else:
    print(f'Encountered errors while inserting rows: {errors}')
