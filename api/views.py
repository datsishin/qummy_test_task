import os

from base64 import b64encode
import requests
import json
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response

from api.models import SecretKey


def get_encrypted_data(self):
    url = os.getenv('URL_WITH_INITIAL_DATA')
    response = requests.get(url).json()
    encrypted_data = []

    for i in range(0, len(response), 1):
        SecretKey.objects.create(
            encrypted_text=response[i]
        )
        encrypted_data.append(response[i])
    return JsonResponse(encrypted_data, safe=False, status=status.HTTP_201_CREATED)


def take_decrypted_data(self):
    url = os.getenv('URL_WITH_DECRYPTER')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    data_for_auth = b64encode(b'username:password').decode('ascii')
    headers = {'Authorization': 'Basic %s' % data_for_auth}
    # headers = {'Authorization': 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='}
    response = requests.post(url, headers=headers).json()
    return JsonResponse(response, safe=False)
    # return HttpResponse(data_for_auth)