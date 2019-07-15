from django.shortcuts import render
# dummy data.
posts = [
  {
    'author': 'John Cena',
    'title': 'Blog Post 1',
    'content': 'blah',
    'date_posted': 'July 15, 2018'
  },
  {
    'author': 'John Wick',
    'title': 'Blog Post 2',
    'content': 'blah2',
    'date_posted': 'July 16, 2018'
  }
]
def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)
  #context is a variable past on to the template, it has accessible: to the variable
def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
