from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()  # Changed to PositiveIntegerField for validation
    category = models.CharField(
        max_length=50,
        choices=[
            ('language', 'Programming Language'),
            ('framework', 'Framework'),
            ('frontend', 'Frontend Technologies'),
            ('backend', 'Backend & Databases'),
            ('tool', 'Tools & Platforms'),
            ('other', 'Other Skills'),
        ]
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.ManyToManyField(Technology, related_name='projects')
    github_link = models.URLField(verbose_name="GitHub Repository")
    live_link = models.URLField(blank=True, null=True, verbose_name="Live Demo")
    date_created = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


# ✅ New Model: Learning Resource
class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(help_text="YouTube/Blog/Website URL")
    category = models.CharField(
        max_length=50,
        choices=[
            ('youtube', 'YouTube Playlist'),
            ('blog', 'Blog Article'),
            ('website', 'Learning Website'),
            ('pdf', 'PDF/Notes'),
            ('other', 'Other'),
        ]
    )
    date_added = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Learning Resource"
        verbose_name_plural = "Learning Resources"

    def __str__(self):
        return self.title
