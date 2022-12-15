from __future__ import absolute_import
from .celery import app
from ..test_api.models import get_distributions, sending_message


@app.task(name='check_database')
def check_database():
    for distriburion in get_distributions():
        for message in distriburion.message.all():
            if sending_message(message.id,
                               message.client.phone_number,
                               distriburion.TEXT) == 20:
                message.is_status()
                message.set_sent_at_now()


app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'check_database',
        'schedule': 10.0,
    }
}
