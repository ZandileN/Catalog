from django.db import models
import uuid  #required for unique book instances
# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class book(models.Model):
    """
    Model representing a book 
    """
    title = models.CharField(max_length=20)
    author= models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary= models.TextField(max_length=1000, help_text="Enter summary of book")
    isbn= models.CharField('ISBN',max_length=50, help_text="13 character ISBN")
    genre= models.ManyToManyField(Genre, max_length=100, help_text="Select genre for this book")

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
         """
        String for representing the Model object.
        """

         return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """

        return reverse('book-detail', args=[str(str.id)])

class bookinstance (models.Model):

         id= models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="unique ID for this particular book across whole liabrary")
         book = models.ForeignKey('book', on_delete=models.SET_NULL, null=True) 
         imprint = models.CharField(max_length=200)
         due_back = models.DateField(null=True, blank=True)
         LOAN_STATUS=(
                        ('m', 'Maintenance'),
                        ('o', 'on loan'),
                        ('a', 'Available'),
                        ('r', 'Reserved')
                      )
         status = models.CharField(max_length=1, choices= LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

class Meta:
        Ordering = ["due_back"]

        def __str__(self):
            return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
     """
    Model representing an author.
    """
     first_name =models.CharField(max_length=100)
     last_name =models.CharField(max_length=100)
     date_of_birth= models.DateField(null=True)
     date_of_death= models.DateField(null=True)

     def get_absolute_url(self):
         return reverse ('author-detail',args=[str(self.id)])

     def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)