from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.UUIDField(primary_key=True, max_length=10, blank=True)
    real_name = models.CharField(max_length=48)
    tz = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class Activity_Period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_time)

    class Meta:
        ordering = ['start_time']
        verbose_name = 'Activity'
        verbose_name_plural = "Activities"


