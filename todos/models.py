from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    NOT_ACTIVE = "NA" #using django choices for status field
    ACTIVE = "A"
    COMPLETED = "C"

    TASK_STATUS = (
        (NOT_ACTIVE, "Not Active"),
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=TASK_STATUS,
        default=NOT_ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True) #check the time when the fields were created and updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["status"]

    def __str__(self):
        return self.name
