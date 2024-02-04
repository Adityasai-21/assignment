from kombu import Exchange, Queue
from kombu.common import Broadcast

BROKER_URL = 'sqla+mysql://root:Saisriram@28@localhost:3306/news_articles'
CELERY_RESULT_BACKEND = 'db+mysql://root:Saisriram@28@localhost:3306/news_articles'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ENABLE_UTC = True
CELERYD_TASK_SOFT_TIME_LIMIT = 600

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Broadcast('broadcast_tasks'),
    Queue('default', Exchange('default'), routing_key='default'),
)
