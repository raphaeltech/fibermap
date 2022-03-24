from django.contrib.auth.models import AbstractUser
from stdimage.models import StdImageField

class User(AbstractUser):  
    image = StdImageField(upload_to='users', variations={'thumb': (90, 90)}, null=True, blank=True)

# Create your models here.
