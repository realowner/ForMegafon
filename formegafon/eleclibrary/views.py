from django.shortcuts import render, redirect

from .models import Authors, Books
from .forms import BookForm, AuthorForm


def index(request):
    authors = Authors.objects.all()
    books = Books.objects.all()
    
    return render(request, 'eleclibrary/index.html', {
        'authors': authors,
        'books': books
    })
    
def addbook(request):
    form = BookForm()
    
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            book = Books(title=form_data['title'], desc=form_data['desc'])
            book.save()
            return redirect('index')
        
    return render(request, 'eleclibrary/addbook.html', {
        'form': form
    })

def editbook(request, book_id):
    book = Books.objects.get(id=book_id)
    form = BookForm(instance=book)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('index')
    
    return render(request, 'eleclibrary/editbook.html', {
        'form': form,
        'book': book
    })
    
def deletebook(request, book_id):
    book = Books.objects.get(id=book_id)
    book.delete()
    return redirect('index')

def addauthor(request):
    form = AuthorForm()
    
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            author = Authors(full_name=form_data['full_name'], country=form_data['country'])
            author.save()
            for book in form_data['books']:
                author.books.add(book.id)
            return redirect('index')
        
    return render(request, 'eleclibrary/addauthor.html', {
        'form': form
    })

def editauthor(request, author_id):
    author = Authors.objects.get(id=author_id)
    form = AuthorForm(instance=author)
    
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.save()
            return redirect('index')
        
    return render(request, 'eleclibrary/editauthor.html', {
        'form': form,
        'author': author
    })

def deleteauthor(request, author_id):
    author = Authors.objects.get(id=author_id)
    author.delete()
    return redirect('index')
