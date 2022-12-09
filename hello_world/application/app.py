import json
import boto3
from botocore.exceptions import ClientError
from application.csv_handler import handle_csv
from application.database.connection import Dabatase
from application.database.cessao_fundo import Cessao_Fundo
from sqlalchemy import insert

def lambda_handler(event, context):
    # TODO implement
    # Read csv
    data = get_file_from_s3('csv-storage-ede', 'arquivo_exemplo.csv')
    
    fetched_csv = handle_csv(data)
    
    db = Dabatase()

    # tabela = db.db.table('cessao_fundo',Dabatase.metadata)
    Cessao_Fundo.create(db.engine)
    
    try:
        db.connection.execute(insert(Cessao_Fundo), fetched_csv['data'])
    except Exception as e:
        print(e)    
    # here each item will be added in database.    

    return {
        'statusCode': 200,
        'success': fetched_csv['success'],
        'error': fetched_csv['error']['count']
        # 'body': json.dumps(fetched_csv['data'])
    }

def get_file_from_s3(ABucket, AKey):
    s3 = boto3.client('s3')
    csv_file = s3.get_object(Bucket=ABucket, Key=AKey)
    data = csv_file['Body'].read().decode('ISO-8859-1').splitlines()
    return data
