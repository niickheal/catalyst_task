from django.db import models

class Upload(models.Model):
    name = models.TextField(null =True, blank = True)
    domain = models.TextField(null =True, blank = True)
    year_founded = models.IntegerField(null =True, blank = True)
    industry = models.TextField(null =True, blank = True)
    size_range = models.TextField(null =True, blank = True)
    city = models.TextField(null =True, blank = True)
    state = models.TextField(null =True, blank = True)
    country = models.TextField(null =True, blank = True)
    linkedin_url = models.TextField(null =True, blank = True)
    current_employee_estimate = models.IntegerField(null =True, blank = True)
    total_employee_estimate = models.IntegerField(null =True, blank = True)

    def __str__(self):
        return str(self.name+'_'+self.industry)