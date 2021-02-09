"""service controller
"""
import logging
import datetime
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse

from database.models import *

def get_diff(request):
    """Calculate difference between
        the square of the sum of the same first n natural numbers
    And
        the sum of the squares of the first n natural numbers

    This first checks database if the number is requested before.
    If then return the stored values after add 1 to the occurrences.
    If not, calculate the difference value and store it in database with occurrences as 1.

    Args:
        request
            HttpRequest Object which contains number as a parameter in the query
    Returns:
        Dictionary with
            datetime
            value
            number
            occurrences
    """
    try:
        if 'number' not in request.GET:
            return JsonResponse({
                'code': 8001,
                'description': 'number is required'
            }, status=400)

        number = int(request.GET['number'])
        if number <= 0 or number > 100:
            return JsonResponse({
                'code': 8002,
                'description': 'invalid number'
            }, status=400)

        if len(TBLServiceLog.objects.filter(number=number)) > 0:
            # if number is already requested at least once
            log = TBLServiceLog.objects.filter(number=number)[0]
            log.occurrences += 1
            log.save()
        else:
            sum1 = 0
            sum2 = 0
            for i in range(1, number+1):
                sum1 += (i ** 2)
            for i in range(1, number+1):
                sum2 += i
            sum2 = sum2 ** 2
            diff = sum2 - sum1
            log = TBLServiceLog()
            log.number = number
            log.value = diff
            log.occurrences = 1
            log.save()

        res = {
            'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'value': log.value,
            'number': number,
            'occurrences': log.occurrences,
        }

        return JsonResponse(res)

    except Exception as e:
        logging.error(str(e))
        return JsonResponse({
            'code': 9001,
            'description': 'Unknown error'
        }, status=500)