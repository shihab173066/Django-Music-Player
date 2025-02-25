from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.TextField()  # Stores the title of the song as a text field (not limited in length).
    artist = models.TextField()  # Stores the artist's name as a text field (not limited in length).
    image = models.ImageField()  # Stores the album/song cover image (requires Pillow library for image handling).
    audio_file = models.FileField(blank=True,null=True) #stores the audio file
    audio_link = models.CharField(max_length=200, blank=True, null=True)  
    # Stores an optional external audio link (e.g., YouTube, Spotify) with a max length of 200 characters.
    
    lyrics = models.TextField(blank=True, null=True)  
    # Stores the lyrics of the song. `blank=True` allows it to be empty in forms, and `null=True` allows null values in the database.
    
    duration = models.CharField(max_length=20)  
    # Stores the song duration as a string (e.g., "03:45"), with a max length of 20 characters.
    paginate_by = 2

    def __str__(self):
        return f"{self.title} - {self.artist}"  # Returns a readable string representation of the song.

