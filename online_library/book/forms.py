from django import forms

from online_library.book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class DeleteBookForm(BookForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'