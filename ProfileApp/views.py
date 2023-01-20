from django.shortcuts import render,HttpResponse


def base(request):
    return render(request,"base.html")

def resume(request):
    return render(request,"resume.html")

def home(request):
    return render(request,"home.html")

def educational(request):
    return render(request,"educational.html")

def interests(request):
    return render(request,"interests.html")

def occupation(request):
    return render(request,"occupation.html")

def roleModel(request):
    return render(request,"roleModel.html")

def sale(request):
    return render(request,"sale.html")

def earphone(reqeust):
    return render(reqeust,"earphone.html")

def speaker(reqeust):
    return render(reqeust,"speaker.html")

def keyboard(reqeust):
    return render(reqeust,"keyboard.html")

def showData(requeust):
    name = "Wannada Mekjinda"
    nickname = "Aum"
    cardId = "1103100708234"
    stdId = "65342310197-3"
    age = "21"
    gender = "female"
    height = "155 cm"
    occupation = "Student"
    favoriteColor = "Pink"
    domicile = "SuphanBuri"
    products = [
        ["BOBBI BROWN รุ่น Crushed Lip Color",1300.00,'images/bobbibrow-rm.png'],
        ["CHANEL รุ่น LE ROUGE DUO ULTRA TENUE", 1500.00, 'images/chanel.png'],
        ["MAYBELLINE NEW YORK  รุ่น Ultimatte By Color Sensational Lipstick", 199.00, 'images/may.png'],
        ["NARS รุ่น Air Matte Lip Color",1100.00,'images/nars.png'],
        ["GUCCI รุ่น Rouge à Lèvres Mat Matte Lipstick",1700.00,'images/gucci-rm.png'],
        ["4u2 รุ่น EST.HARDER 2",299.00,'images/4u2-rm.png'],
        ["YSL รุ่น Rouge Pur Couture The Slim Velvet Radical",1550.00,'images/ysl-rm.png'],
        ["DIOR รุ่น Addict Lip Glow Lip Balm",1500.00,'images/dior.png'],
        ["L'OREAL PARIS  รุ่น Rouge Signature",299.00,'images/paris.png'],
        ["MAC รุ่น Powder Kiss Lipstick",970.00,'images/mac-rm.png']
    ]
    context = {'name':name,'nickname':nickname,'cardId':cardId,'stdId':stdId,'age':age,
               'gender':gender,'height':height,'occupation':occupation,'favoriteColor':favoriteColor,
               'domicile':domicile,'products':products}
    return render(requeust,"Mydata.html",context)
