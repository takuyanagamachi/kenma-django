from django import forms

CHOICES = (
    ('タイトルを選択してください','タイトルを選択してください'),
    ('粉砕刃','粉砕刃'),
    ('チッパーナイフ','チッパーナイフ'),
    ('スリッター', 'スリッター'),
    ('裁断刃','裁断刃'),
    ('製袋刃','製袋刃'),
    ('台切り','台切り'),
    ('その他','その他'),
)

class ContactForm(forms.Form):
   name = forms.CharField(label='お名前', max_length=50, required=True,)
   email = forms.EmailField(label='メールアドレス', required=True,)
   select = forms.ChoiceField(widget=forms.Select,choices=CHOICES,label="タイトル")
   message = forms.CharField(label='メッセージ', required=True, widget=forms.Textarea)
