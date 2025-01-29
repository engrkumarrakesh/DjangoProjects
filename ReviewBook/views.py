from django.shortcuts import render, redirect
from ReviewBook.models import Book
from ReviewBook.forms import BookForm
from django.contrib import messages

# Create your views here.
# class ReviewView(View):
#     def get(self, request):
#         return render(request, 'review.html')
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully')
            return redirect('book_create')
    else:
        form = BookForm()
    return render(request, 'book/book_create.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books':books})

def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book/book_detail.html', {'book':book})

def book_update(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_update.html', {'form':form})


# Delete with GET method, No confirmation required
# def book_delete(request, pk):
#     book = Book.objects.get(id=pk)
#     book.delete()
#     return redirect('book_list')

def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_list.html', {'book':book})

