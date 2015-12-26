from __future__ import absolute_import
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .nagariknews import nagarik_crawler
from datetime import datetime
from .onlinekhabar import onlinekhabar_crawler
from .models import News


logger = get_task_logger(__name__)

#periodic task that run every 30 minute
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def news():
	'''
	aggregrate all the news from each
	online nepali news portal
	'''
	logger.info("Start task")
	now =  datetime.now()
	source = 'online'
	allnews = []
	allnews.append(nagarik_crawler())
	allnews.append(onlinekhabar_crawler())
	for news_dict in list(reversed(allnews)):
		for news, url  in news_dict.items():
			#Save all the scrape news in database
			News.objects.create(title=news, url=url, source=source)
	
	