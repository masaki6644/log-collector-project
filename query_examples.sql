CREATE EXTERNAL TABLE IF NOT EXISTS logs_table (
  timestamp string,
  user_id string,
  action string,
  ip string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://mylog-storage-bucket/'
TBLPROPERTIES ('has_encrypted_data'='false');

