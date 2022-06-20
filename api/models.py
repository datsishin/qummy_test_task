from django.db import models
from datetime import datetime as dt


class SecretKey(models.Model):
    encrypted_text = models.TextField()
    decrypted_text = models.TextField()
    created_at = models.DateTimeField(default=dt.now)

    # class Meta:
    #     def __str__(self):
    #         return self.encrypted_text, self.decrypted_text
