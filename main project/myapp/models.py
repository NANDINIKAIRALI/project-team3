from django.db import models

# Create your models here.
class Job(models.Model):
    job_name=models.CharField(max_length=50,blank=False,null=False)
    job_description=models.TextField(blank=False,null=False)
    company_name=models.CharField(max_length=50,blank=False,null=False)
    company_description=models.TextField(blank=False,null=False)
    closing_date=models.DateField(auto_now=False,auto_now_add=False)
    def __str__(self):
        return self.job_name