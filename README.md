# ログ収集 & 可視化プロジェクト

##  概要
Pythonで生成したログを、AWS Lambda経由でS3に保存し、Athenaで可視化する。

##  使用技術
- AWS（S3, Lambda, API Gateway, Athena）
- Python
- GitHub

##  システム構成
1. Pythonスクリプトでログ送信
2. API Gatewayが受信し、LambdaでS3へ保存
3. Athenaで可視化

##  実行方法
```bash
python client/send_log.py

