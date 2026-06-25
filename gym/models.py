from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    photo = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    join_date = models.DateField()
    expiry_date = models.DateField()
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Fitness', 'Fitness'),
        ('Nutrition', 'Nutrition'),
        ('Workout', 'Workout'),
        ('Health', 'Health'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Used for the URL (e.g. fitness-tips-for-2026)")
    author = models.CharField(max_length=100, default="FitZone Team")
    content = models.TextField()
    blog = models.ImageField(upload_to='blog/', null=True, blank=True, help_text="Thumbnail Image")
    video = models.FileField(upload_to='blog_videos/', null=True, blank=True, help_text="Optional: Upload an MP4 video")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Fitness')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
