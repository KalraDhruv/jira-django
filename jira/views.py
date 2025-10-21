from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bug
from django.views.generic import DetailView


def home(request):
    context = {
        'bugs': Bug.objects.all()
    }
    return render(request, 'jira/home.html', context)

class BugDetailView(DetailView):
    model = Bug
    template_name = 'jira/bug_detail.html' 
    context_object_name = 'bug'

@login_required
def update_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)

    if request.method == 'POST':
        if 'assign_self' in request.POST:
            bug.assigned_to = request.user
            bug.save()
            return redirect('bug-detail', pk=bug.pk)

        new_status = request.POST.get('status')
        if new_status and new_status in [choice[0] for choice in Bug.STATUS_CHOICES]:
            bug.status = new_status
            bug.save()
            return redirect('bug-detail', pk=bug.pk)

    return redirect('bug-detail', pk=bug.pk)
