from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Skill, Project, Technology, ContactMessage


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    skills = Skill.objects.all().order_by('order')
    featured_projects = Project.objects.filter(featured=True).order_by('-date_created')[:6]

    return render(request, 'portfolio/index.html', {
        'skills': skills,
        'projects': featured_projects,
        'technologies': Technology.objects.all()
    })


def about(request):
    return render(request, 'portfolio/about.html')


def projects(request):
    all_projects = Project.objects.all().order_by('-date_created')
    context = {
        'projects': all_projects,
        'technologies': Technology.objects.all()
    }
    return render(request, 'portfolio/projects.html', context)

def skills(request):
    all_skills = Skill.objects.all().order_by('order')
    context = {
        'skills': all_skills
    }
    return render(request, 'portfolio/skills.html', context)



def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(id=project.id).distinct()[:3]

    context = {
        'project': project,
        'related_projects': related_projects
    }
    return render(request, 'portfolio/project_detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Optional: Send mail if configured
        # send_mail(...)

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'portfolio/contact.html')