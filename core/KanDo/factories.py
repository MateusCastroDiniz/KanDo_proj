import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from django.utils.timezone import now
from core.KanDo.models import Task
from core.KanDo.models import Board
from core.KanDo.models import Column



faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('safe_email')
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class BoardFactory(factory.django.DjangoModelFactory):
    board_name = factory.LazyAttribute(lambda x: faker.sentence())
    owner = factory.SubFactory(UserFactory)
    created_on = factory.LazyAttribute(lambda x: now())

    class Meta:
        model = Board


class ColumnFactory(factory.django.DjangoModelFactory):
    column_name = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())

    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = Column


class TaskFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 1
    description = factory.LazyAttribute(lambda x: faker.sentence())
    priority = 3
    column = factory.SubFactory(ColumnFactory)


    class Meta:
        model = Task
