from django.db import models


def upload_path(instance, filename):
    return f"testimonials/{filename}"


class Testimonial(models.Model):
    profile_iamge = models.ImageField(upload_to=upload_path)
    name = models.CharField(max_length=80)
    job_position = models.CharField(max_length=80)
    social_media_address = models.URLField()
    description = models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.description[:50]}"

    def __repr__(self):
        return f"{self.name}, {self.description[:50]}"
