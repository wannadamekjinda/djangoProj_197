from django import forms


class ProductForm(forms.Form):
    COLOR_LIST = [
                ('Black','Black'),
                ('Red', 'Red'),
                ('Silver', 'Silver'),
                ]

    BAT_LIST = [('5000 mAh', '5000 mAh'),
                     ('6000 mAh', '6000 mAh'),
                     ('8000 mAh', '8000 mAh'),
                     ('12000 mAh', '12000 mAh'),]

    WAR_LIST = [
        ('1 ปี','1 ปี'),
        ('2 ปี','2 ปี'),
        ('3 ปี','3 ปี')
    ]


    brand = forms.CharField(max_length=30, label="ยี่ห้อ"
                         ,required=True,widget=forms.TextInput(attrs={'size' : '35'}))

    model = forms.CharField(max_length=30, label="รุ่น"
                         , required=True, widget=forms.TextInput(attrs={'size': '35'}))

    warranty = forms.CharField(max_length=30, label="ประกัน",
                            required=True, widget=forms.Select(choices=WAR_LIST))

    color = forms.CharField(max_length=30, label="สี",
                              required=True, widget=forms.Select(choices=COLOR_LIST))

    battery = forms.CharField(max_length=30,label="แบตเตอรรี่",
                             required=True,widget=forms.RadioSelect(choices=BAT_LIST))

    price = forms.FloatField(label="ราคา" ,required=True,
                              widget=forms.NumberInput(attrs={'size':'13'}))
