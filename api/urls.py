from django.urls import path, include

from api import views

urlpatterns = [
    # path('get-encrypted-data', views.EncryptedData.as_view({'get': 'get_encrypted_data'})),
    path('get-encrypted-data', views.get_encrypted_data),
    path('take-decrypted-data', views.take_decrypted_data),
]
