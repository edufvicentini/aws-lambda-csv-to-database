import boto3
from botocore.exceptions import ClientError
from application.csv_handler import handle_csv
from application.database.connection import Dabatase
from application.database.cessao_fundo import Cessao_Fundo
from sqlalchemy import insert

def lambda_handler(event, context):
    # TODO implement
    # Read csv
    try:
        data = get_file_from_s3(event['bucket_name'], event['object_key'])
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {
                'message': 'error trying to get file from s3',
                'error': e.args[0]  
            }  
        } 
        
    try:    
        fetched_csv = handle_csv(data)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {
                'message': 'error converting csv data',
                'error': e.args[0]  
            }  
        }
    
    try:
        db = Dabatase()
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {
                'message': 'database connection error',
                'error': e.args[0]
            }   
        }
    # # tabela = db.db.table('cessao_fundo',Dabatase.metadata)
    if not db.engine.dialect.has_table(db.connection, Cessao_Fundo.__tablename__):
        Cessao_Fundo.create(db.engine)
    
    try:
        db.connection.execute(insert(Cessao_Fundo), fetched_csv['data'])  # here each item will be added in database.  
    except Exception as e:
        return {
        'statusCode': 200,
        'body': {
            'message': 'error inserting into database',
            'error': e.args[0]
        }
    } 
    
    return {
        'statusCode': 200,
        'body': {
            'success': fetched_csv['success'],
            'error': fetched_csv['error']['count'],
            'error_list': fetched_csv['error']['error_list']
        }
    }

def get_file_from_s3(ABucket, AKey):
    s3 = boto3.client('s3')
    csv_file = s3.get_object(Bucket=ABucket, Key=AKey)
    data = csv_file['Body'].read().decode('ISO-8859-1').splitlines()
    return data
