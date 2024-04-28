import boto3
import json
import os

class AWSProvider:
    def __init__(self):
        self.__client = boto3.client(
            'events',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_DEFAULT_REGION')
        )
    
    def enviar_evento_eventbridge(self, dna, is_mutant):
        evento = {
            "source": "my-application",
            "detail-type": "mutant-detected",
            "detail": json.dumps({
                "dna": dna,
                "is_mutant": is_mutant
            })
        }
        
        # Enviar el evento a EventBridge
        response = self.__client.put_events(Entries=[{
            "Source": evento["source"],
            "DetailType": evento["detail-type"],
            "Detail": evento["detail"]
        }])
        
        # Verificar la respuesta
        if response['FailedEntryCount'] == 0:
            print("Evento enviado exitosamente a EventBridge")
        else:
            print(f"Error al enviar el evento a EventBridge: {response}")