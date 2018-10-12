import random

from django.urls import reverse

import pytest
from faker import Faker
from rest_framework import status


fake = Faker()


@pytest.mark.django_db
@pytest.mark.parametrize('method,endpoint', [
    ('get', reverse('v1:reviews-list')),
    ('get', reverse('v1:reviews-detail', kwargs={'pk': 1})),
    ('post', reverse('v1:reviews-list'))
])
def test_route_is_unauthorized_for_anonymous(
    api_client, method, endpoint
):
    api_method = getattr(api_client, method)
    response = api_method(endpoint)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize('rating', [
    pytest.param(
        None,
        marks=pytest.mark.xfail(reason='required', raises=AssertionError)),
    pytest.param(
        0,
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    random.choice([1, 2, 3, 4, 5])
])
@pytest.mark.parametrize('title', [
    pytest.param(
        None,
        marks=pytest.mark.xfail(reason='required', raises=AssertionError)),
    pytest.param(
        '',
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    pytest.param(
        'T'*65,
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    'T'*64
])
@pytest.mark.parametrize('summary', [
    pytest.param(
        None,
        marks=pytest.mark.xfail(reason='required', raises=AssertionError)),
    pytest.param(
        '',
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    pytest.param(
        'T'*10001,
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    'T'*10000
])
@pytest.mark.parametrize('company', [
    pytest.param(
        None,
        marks=pytest.mark.xfail(reason='required', raises=AssertionError)),
    pytest.param(
        '',
        marks=pytest.mark.xfail(reason='invalid', raises=AssertionError)),
    fake.company()
])
def test_review_create(
    admin_api_client, rating, title, summary, company
):
    data = {
        'rating': rating,
        'title': title,
        'summary': summary,
        'company': {
            'name': company
        }
    }

    response = admin_api_client.post(reverse('v1:reviews-list'), data)
    assert response.status_code == status.HTTP_201_CREATED
