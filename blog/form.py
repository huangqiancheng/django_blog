from django import forms

class CommentForm(forms.Form):
    # TextInput,Textarea为控件
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'名字'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'邮箱'}))
    comments = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'留言....'}))