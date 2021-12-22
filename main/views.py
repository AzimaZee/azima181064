from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        masukx = int(request.POST['titik x'])
        masuky = int(request.POST['titik y'])
        pusatx = int(request.POST['pusat x'])
        pusaty = int(request.POST['pusat y'])
        k = int(request.POST['skala'])
        keluarx = k*(masukx-pusatx)+pusatx
        keluary = k*(masuky-pusaty)+pusaty
        keluar = [str(keluarx) + ',' + str(keluary)]
        context = {'keluar': keluar,
                   }
        return render(request, 'main/home.html', context)

    else:
        return render(request, 'main/home.html', {})