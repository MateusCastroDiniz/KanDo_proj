from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = (
    (0, 'To-do'),
    (1, 'Doing'),
    (3, 'Finished'),
    (4, 'Not finished'),
    (5, 'Aborted')
)

PRIORITY = (
    (0, 'No important'),
    (1, 'Important'),
    (2, 'Urgent'),
    (3, 'Emergency'),
)


class Board(models.Model):
    board_name = models.CharField(max_length=180)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']

    def create_column(self, column_name, description, status, priority):
        return Column.objects.create(column_name=column_name, owner=self.owner, description=description, status=status,
                                     priority=priority, board=Board.objects.get(board_name=self.board_name))


    def __str__(self):
        return self.board_name


class Column(models.Model):
    column_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='board', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def create_task(self, title, author, description, status, priority):
        return Task.objects.create(title=title, author=author,
                                   description=description, status=status,
                                   priority=priority, column=Column.objects.get(column_name=self.column_name))

    def __str__(self):
        return self.column_name


class Task(models.Model):
    title = models.CharField(max_length=200)
    task_slug = str(title).replace(' ', '-')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_post')
    description = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    column = models.ForeignKey(Column, related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


@receiver(post_save, sender=Board)
def create_initial_column(sender, instance, created, **kwargs):
    if created:
        Column.objects.create(board=instance, column_name='To-Do')
        Column.objects.create(board=instance, column_name='Doing')
        Column.objects.create(board=instance, column_name='Finished')