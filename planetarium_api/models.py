from django.db import models
from django.contrib.auth import get_user_model


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.created_at}"


class ShowTheme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.astronomy_show.title} {self.planetarium_dome.name} {self.show_time}"
        )


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE)
    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.row} {self.seat}"
