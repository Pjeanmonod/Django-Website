from django.db import models

class JobVar(models.Model):

    INPUT_TEXT = "text"
    INPUT_UARRAY = "user_array"
    INPUT_DARRAY = "defined_array"
    INPUT_BOOL = "boolean"

    INPUT_TYPES = (
        (INPUT_TEXT, "text"),
        (INPUT_UARRAY, "user_array"),
        (INPUT_DARRAY, "defined_array"),
        (INPUT_BOOL, "boolean"),
    )  

    var_id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    input_type = models.CharField(
        max_length=13,
        choices=INPUT_TYPES,
        default='text',
    )
    
    def __str__(self):
        return self.name



class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    role_display_name = models.CharField(max_length=60)
    req_vars = models.ManyToManyField(JobVar)


    def __str__(self):
        return self.name


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    slug = models.CharField(max_length=60)
    jobs = models.ManyToManyField(Job)

    def __str__(self):
        return self.name
