from django.db import models

#class KeyMarket(models.Model):
#    #zip_code
#    pass
#
#class City(models.Model):
#    #zip_code_3
#    #name
#    #market foreign key
#    #distance to market center
#    pass
#
#class Industry(models.Model):
#    pass

class Commodity(models.Model):
    sctg_code = models.IntegerField(blank=False, default=0)
    description = models.CharField(max_length=100, blank=False, default="SCTG suppressed")
    sctg_group = models.CharField(max_length=5, blank=False, default="0000")
    
    def __str__(self):
        return self.description
