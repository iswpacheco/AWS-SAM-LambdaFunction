import json
import numpy as np

def lambda_handler(event, context):

    arr = np.array([1, 2, 3, 4, 5])
    return {
        'statusCode': 200,
        'body': json.dumps({
        'message': "Hello World",
        'lib': str(arr[0])
        })
    }
