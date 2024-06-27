import boto3
  
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Crear cliente para dynamodb

# Nombre de la tabla en DynamoDB
table_name = 'tabla-Danny-Cano'
table = dynamodb.Table(table_name)

# Leer un elemento específico por clave primaria
response = table.get_item(Key={'Id': '2'})

# Imprimir la respuesta
print(response['Item'])

# Leer todos los elementos de la tabla
response = table.scan()

print(response['Items'])


#como crear un registro

new_item = {
    'Id': '5',
    'nombre': 'Omar',
    'Ciudad': 'Medellin',
    'Edad':87,
    # Agrega más atributos según la estructura de tu tabla
}

# Crear el registro en la tabla
table.put_item(Item=new_item)

# Leer todos los elementos de la tabla
response = table.scan()

print(response['Items'])


# Leer un elemento específico por clave primaria
response = table.get_item(Key={'Id': '5'})
print("Elemento antes de actualizar:",response['Item'])
response = table.update_item(
    Key={
        'Id':'5'
    },
    UpdateExpression='SET Edad= :val1',
    ExpressionAttributeValues={
        ':val1': 18
    }
  
)

# Leer un elemento específico por clave primaria
response = table.get_item(Key={'Id': '5'})
# Imprimir la respuesta
print("Elemento actualizado:",response['Item'])