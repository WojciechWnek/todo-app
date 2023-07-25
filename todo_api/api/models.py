from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True, editable=False)
    owner = models.ForeignKey(
        'auth.User', related_name='task', on_delete=models.CASCADE, default=None)

    # Override modles save method with my own
    def save(self, *args, **kwargs):
        if not self._state.adding:
            from datetime import datetime
            self.edited_at = datetime.now()

        super().save(*args, **kwargs)
