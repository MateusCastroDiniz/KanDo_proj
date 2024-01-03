from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

PRIORITY = (
    (0, 'No important'),
    (1, 'Important'),
    (2, 'Urgent'),
    (3, 'Emergency'),
)


class Task(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_post')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
