from django.shortcuts import render
from .nagariknews import nagarik_crawler
from .onlinekhabar import onlinekhabar_crawler
from .models import News
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewsSerializers

def news(request):
	'''
	aggregrate all the news from each
	online nepali news portal
	'''
	source = 'online'
	allnews = []
	allnews.append(nagarik_crawler())
	allnews.append(onlinekhabar_crawler())
	for news_dict in list(reversed(allnews)):
		for news, url  in news_dict.items():
			#Save all the scrape news in database
			News.objects.create(title=news, url=url, source=source)
		
	return render(request, 'news/index.html', {'allnews':allnews, 'source': source})

@api_view(['GET', 'POST'])
def news_list(request):
    """
    List all news
    """
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializers(news, many=True)
        return Response(serializer.data)

    else:
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'POST':
    #     serializer = TaskSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(
    #             serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Get, udpate, or delete a specific task
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(
#                 serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)