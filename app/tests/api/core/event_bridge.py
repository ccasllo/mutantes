import boto3
import json
import os

def enviar_evento_eventbridge(dna, is_mutant):
    client = boto3.client(
        'events',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
        )

    # Construir el evento a enviar
    evento = {
        "source": "my-application",
        "detail-type": "mutant-detected",
        "detail": json.dumps({
            "dna": dna,
            "is_mutant": is_mutant
        })
    }
    
    # Enviar el evento a EventBridge
    response = client.put_events(Entries=[{
        "Source": evento["source"],
        "DetailType": evento["detail-type"],
        "Detail": evento["detail"]
    }])
    
    # Verificar la respuesta
    if response['FailedEntryCount'] == 0:
        print("Evento enviado exitosamente a EventBridge")
    else:
        print(f"Error al enviar el evento a EventBridge: {response}")


if __name__ == '__main__':
    dna = '["ATGCGA","CCGTTC","TTATGT","AGAAGG","CCCCTA","TCACTG"]'
    is_mutant = True

    enviar_evento_eventbridge(dna, is_mutant)
