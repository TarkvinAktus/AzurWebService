# standard library
import datetime
import urllib.parse

# django
from django.views.generic import ListView
from django.db.models import Count
from django.shortcuts import render

# local django
from mainApp.models import StatisticsUrl



class StatisticsUrlListView(ListView):
    model = StatisticsUrl

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        url_parameters_dict = dict(self.request.GET.lists())
        context_data['url_param'] = url_parameters_dict
        return context_data

    def get_queryset(self):
        queryset = StatisticsUrl.objects.all()
        url_parameters = self.request.GET

        if url_parameters != {}:
            # date filter
            daterange = url_parameters['daterange']
            daterange = urllib.parse.unquote(daterange)
            
            if daterange != '':
                #split string and get two lists of MM, DD and YYYY
                daterange = daterange.split('-')
                start_date = daterange[0].split('/')
                end_date = daterange[1].split('/')
                #GET in format MM-DD-YYYY
                #Increment last argument to include last date in range in filter
                #Input in format YYYY-MM-DD+1
                queryset = queryset.filter(date_time__range=(datetime.datetime(int(start_date[2]), int(start_date[0]), int(start_date[1])), datetime.datetime(int(end_date[2]), int(end_date[0]), int(end_date[1])+1)))

            # key filter
            key_name = url_parameters['key_name']
            if key_name != '':
                queryset = queryset.filter(key_name__contains = key_name)

            # domain filter
            domain = url_parameters['domain']
            if domain != '':
                queryset = queryset.filter(url_domain = domain)

            # code filter
            status_code = url_parameters['status_code']
            if status_code != '':
                if(status_code == '4XX'):
                    queryset = queryset.filter(status_code__lte=499).filter(status_code__gte=400)
                else:
                    queryset = queryset.filter(status_code = int(status_code))
            
            # size filter
            size = url_parameters['size']
            if size != '':
                queryset = queryset.filter(byte_size__gte = int(size))

            ### group filters ###

            groupValues = []
            countColumn = ''

            # group by date 
            group_date = url_parameters.get('group_date', None)
            if group_date == 'true':
                groupValues.append('date_time')
                countColumn = 'date_time' 

            # group by key name 
            group_name = url_parameters.get('group_name', None)
            if group_name == 'true':
                groupValues.append('key_name')
                countColumn = 'key_name'

            # group by domain
            group_domain = url_parameters.get('group_domain', None)
            if group_domain == 'true':
                groupValues.append('url_domain')
                countColumn = 'url_domain'

            # group by status_code 
            group_status_code = url_parameters.get('group_status_code', None)
            if group_status_code == 'true':
                groupValues.append('status_code')
                countColumn = 'status_code'

            if countColumn != '':
                queryset = queryset.values(*groupValues).annotate(total=Count(countColumn)).order_by()


        return queryset

