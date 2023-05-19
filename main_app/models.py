from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation


class Dwelling(models.Model):

    class DwellingStatus(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        POSTED = 'PT', 'Posted'

    class DwellingType(models.TextChoices):
        room = 'RM', 'Room'
        house = 'HS', 'House'
        apartment = 'AP', 'Apartment'
        guesthouse = 'GH', 'Guesthouse'

    class DwellingBan(models.TextChoices):
        ACTIVE = 'AC', 'Active'
        BANNED = 'BN', 'Banned'

    title = models.CharField(max_length=100)
    card_description = models.CharField(max_length=500)
    full_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    posted = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    #images
    dwelling_type = models.CharField(max_length=2, choices=DwellingType.choices)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #location
    dwelling_post_status = models.CharField(max_length=2, choices=DwellingStatus.choices, default=DwellingStatus.DRAFT)
    dwelling_ban_status = models.CharField(max_length=2, choices=DwellingBan.choices, default=DwellingBan.ACTIVE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dwellings')

    class Meta:
        ordering = ['-posted']
        indexes = [models.Index(fields=['-posted']), ]
    
    def __str__(self):
        return self.title


class DwellingRentStatus(models.Model):

    class RentStatus(models.TextChoices):
        ACTIVE = 'A', 'Active'
        COMPLETED = 'C', 'Completed'
        BOOKED = 'B', 'Booked'

    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentings')
    dwelling = models.ForeignKey(Dwelling, on_delete=models.CASCADE, related_name='rent_status')
    created = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    rent_status = models.CharField(max_length=1, choices=RentStatus.choices, default=RentStatus.BOOKED)

    def __str__(self):
        return self.rent_status


class ReviewDwelling(models.Model):
    review = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = GenericRelation(Rating)
    dwelling_order = models.ForeignKey(DwellingRentStatus, on_delete=models.CASCADE, related_name='renter_review')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dwellings_reviews')

    class Meta:
        ordering = ['-posted']
        indexes = [models.Index(fields=['-posted']), ]


class ReviewRenter(models.Model):
    review = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = GenericRelation(Rating)
    dwelling_order = models.ForeignKey(DwellingRentStatus, on_delete=models.CASCADE, related_name='owner_review')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='renters_reviews')

    class Meta:
        ordering = ['-posted']
        indexes = [models.Index(fields=['-posted']), ]
