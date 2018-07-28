from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy,reverse
from django.views import generic
from .models import Bookmarks

class IndexView(generic.ListView):
  model = Bookmarks
  template_name = 'bookmarks/index.html'
  context_object_name = 'bookmarks'

class BookmarkCreate(CreateView):
  model = Bookmarks
  fields = ['name','url','desc','tags']
  template_name = 'bookmarks/add.html'
  context_object_name = 'fields'
  success_url = reverse_lazy('index')

class BookmarkUpdate(UpdateView):
    model = Bookmarks
    fields = ['name','url','desc','tags']
    template_name = 'bookmarks/update.html'
    context_object_name = 'fields'
    success_url = reverse_lazy('index')

class BookmarkDelete(DeleteView):
  model = Bookmarks
  success_url = reverse_lazy('index')
  def get_object(self, queryset=None):
    """ Hook to ensure object is owned by request.user. """
    obj = super(BookmarkDelete, self).get_object()
    return obj  