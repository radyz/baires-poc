from django.contrib.auth import get_user_model

import factory
from factory import fuzzy

from reviews.models import Review,  Company


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%s' % n)
    email = factory.Sequence(lambda n: 'user_%s@test.com' % n)
    password = factory.PostGenerationMethodCall(
        'set_password', 'defaultpassword')

    class Meta:
        model = get_user_model()


class CompanyFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=10)

    class Meta:
        model = Company


class ReviewFactory(factory.django.DjangoModelFactory):

    rating = 1
    title = factory.Sequence(lambda n: 'Title_%s' % n)
    summary = factory.Sequence(lambda n: 'Summary_%s' % n)
    ip_address = '127.0.0.1'
    company = factory.SubFactory(CompanyFactory)
    reviewer = factory.SubFactory(UserFactory)

    class Meta:
        model = Review
