from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class Complaint(models.Model):

    title = models.CharField(max_length=200)

    description = models.CharField(max_length=500)

    COMPLAINT_TYPE_CHOICES =[
        ("Cleanliness","cleanliness"),
        ("Staff Behavior","staff behavior"),
        ("Waiting Time","waiting time"),
        ("Billing","billing"),
        ("Equipment","equipment")
    ]


    complaint_type = models.CharField(
        max_length=100,
        choices=COMPLAINT_TYPE_CHOICES
    )

    department = models.CharField(max_length=100)

    PRIORITY_CHOICES =[
        ("Low","low"),
        ("Medium","medium"),
        ("High","high"),
        ("Critical","critical")
    ]

    priority = models.CharField(
        max_length=100,
        choices=PRIORITY_CHOICES
    )

    STATUS_CHOICES = [
        ("Submitted","submitted"),
        ("Under Review","under review"),
        ("In Progress","in progress"),
        ("Resolved","resolved")
    ]


    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES
    )

    reported_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="complaints"
    )

    def __str__(self):
        return f"{self.title}"