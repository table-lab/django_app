from django.shortcuts import render
import datetime
from django.shortcuts import redirect
from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    template_name = 'ag360l_app/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('ag360l_app:mycalendar', year=date.year, month=date.month, day=date.day)


from django.core.paginator import Paginator
def index(request, num=1):
    data = Schedule.objects.all().order_by('date','start_time').reverse()
    page = Paginator(data, 10)
    params = {
            'title': 'schedule',
            'message': 'schedule',
            'data': page.get_page(num),
        }
    return render(request, 'ag360l_app/index.html' , params)



def edit(request, num):
    obj = Schedule.objects.get(id=num)
    if (request.method == 'POST'):
        schedule = BS4ScheduleForm(request.POST, instance=obj)
        schedule.save()
        return redirect(to='/ag360l_app')
    params = {
        'title': 'schedule',
        'id' : num,
        'form':BS4ScheduleForm(instance=obj),
    }   
    return render(request, 'ag360l_app/edit.html' , params)

def create(request):
    if (request.method == 'POST'):
        obj = Schedule()
        schedule = BS4ScheduleForm(request.POST, instance=obj)
        schedule.save()
        return redirect(to='/ag360l_app')
    params = {
        'title': 'schedule',
        'form': BS4ScheduleForm(),
    }   
    return render(request, 'ag360l_app/create.html' , params)



