import pandas as pd
import random

from django.test import TestCase
from django.test.client import Client

class ServiceTestCase(TestCase):

    def test_service(self):
        client = Client()
        url = '/difference'
        number = random.randint(1, 100)
        res = client.get(url, data={
            'number': number
        })

        # check status code
        assert res.status_code == 200, f'Endpoint returns unexpected status code. {res.status_code}'
        res = res.json()

        # check columns
        df = pd.DataFrame([res])
        expected_columns =[
            'datetime',
            'value',
            'number',
            'occurrences',
        ]
        assert set(expected_columns) == set(df.columns), 'Endpoint returns unexpected columns'

        # check values
        assert res['number'] ==  number, f'Endpoint returns invalid number. Expected: {number}, Actual: {res["number"]}'

        sum1 = 0
        sum2 = 0
        for i in range(1, number+1):
            sum1 += (i ** 2)
        for i in range(1, number+1):
            sum2 += i
        sum2 = sum2 ** 2

        exp_value = sum2 - sum1
        assert res['value'] == exp_value, f'Endpoint returns invalid value. Expected: {exp_value}, Actual: {res["value"]}'

        assert res['occurrences'] == 1, f'Endpoint returns invalid occurrences. Expected: 1, Actual: {res["occurrences"]}'

        # try again, and check 'occurrences' if it is increased
        res = client.get(url, data={
            'number': number
        })

        # check status code
        assert res.status_code == 200, f'Endpoint returns unexpected status code. {res.status_code}'
        res = res.json()
        assert res['occurrences'] == 2, f'Endpoint returns invalid occurrences. Expected: 2, Actual: {res["occurrences"]}'






