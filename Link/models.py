from django.db import models
from django.utils.crypto import get_random_string

# Create your models here.

class Link(models.Model):
    link_address = models.CharField(max_length=1000)
    short_link = models.CharField(max_length=100, blank=True)


    def save(self, *args, **kwargs):
        if not self.short_link:
            # generate_short_link = get_random_string(5)
            generate_short_link = "MtIVB"
            check_short_link = Link.objects.filter(short_link = generate_short_link).first()
            while check_short_link:
                generate_short_link = get_random_string(5)
                check_short_link = Link.objects.filter(short_link = generate_short_link).first()

            self.short_link = generate_short_link

        super(Link, self).save(*args, **kwargs)
            
