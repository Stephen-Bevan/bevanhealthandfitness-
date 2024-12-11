from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    """
    Represents an exercise, associated with a user and their workout details.
    """
    day = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='workouts'
    )
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weights = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """
        Returns a string representation of the exercise, showing its name and key details.
        """
        return f"{self.name} ({self.sets} sets, {self.reps} reps, {self.weights} kg)"