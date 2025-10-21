from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.db.models import Q


class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.GET.get('q')
        genre = self.request.GET.get('genre')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        if genre:
            queryset = queryset.filter(genre__name__icontains=genre)
        return queryset.order_by('-rating')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = self.object
            comment.author = request.user
            comment.save()
        return redirect('movie_detail', pk=self.object.pk)


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
