import boto3

# Configurar el cliente de DynamoDB en una región específica
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Nombre de la tabla que deseas crear
table_name = 'tabla-Danny-Cano-2'



try:
    response = dynamodb.delete_table(TableName=table_name)
    print(f"La tabla '{table_name}' ha sido eliminada correctamente.")
except dynamodb.exceptions.ResourceNotFoundException:
    print(f"La tabla '{table_name}' no existe o ya ha sido eliminada anteriormente.")
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar la tabla '{table_name}': {e}")