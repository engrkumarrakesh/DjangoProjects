from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    GENERE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('romance', 'Romance'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('science', 'Science'),
        ('mystery', 'Mystery'),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100, choices=GENERE_CHOICES)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publication_date = models.DateField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)
    number_of_reviews = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
    

