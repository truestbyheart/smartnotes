from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from notes.forms import NotesCreateForm
from notes.models import Note


class NotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/notes.html'
    login_url = '/login/'
    context_object_name = 'notes'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NotesCreateForm
    template_name = 'notes/notes_create.html'
    login_url = '/login/'
    success_url = "/smart/notes"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
