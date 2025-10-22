from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Film, Genre
from .forms import FilmForm, CommentForm
from django.shortcuts import render, redirect

class FilmListView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        queryset = Film.objects.all().order_by('-rating')
        search = self.request.GET.get('search')
        genre = self.request.GET.get('genre')
        if search:
            queryset = queryset.filter(title__icontains=search)
        if genre:
            queryset = queryset.filter(genre__name=genre)
        return queryset


class FilmDetailView(DetailView):
    model = Film
    template_name = 'CineBoard/film_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        context['comments'] = film.comments.all()
        if self.request.user.is_authenticated:
            context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        film = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.film = film
            comment.save()
        return redirect('film_detail', pk=film.pk)


class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('film_list')


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('film_list')


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = 'CineBoard/film_confirm_delete.html'
    success_url = reverse_lazy('film_list')




from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})




