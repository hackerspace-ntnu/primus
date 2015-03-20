from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    lowest_best = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


class Result(models.Model):
    player = models.CharField(max_length=128, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    time = models.DateTimeField(blank=False, null=False)
    contest = models.ForeignKey(to=Contest, blank=False, null=False, related_name='results')

    def __str__(self):
        return "{}: {}".format(self.player, self.value)