from django.shortcuts import render
from dashboard.forms import FormBarang
# # Create your views here.

def tambah_barang(request):
    titelnya="addbrg"
    form=FormBarang()
    konteks={
        'form':form,
            'titel':titelnya,
    }
    return render(request,'tambah_barang.html',konteks)

def blog(request):
    titelnya="Blog"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog.html',konteks)

def blogdetail(request):
    titelnya="Blog Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog-detail.html',konteks)

def contact(request):
    titelnya="Contact"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'contact.html',konteks)

def projectdetail(request):
    titelnya="Project Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'project-detail.html',konteks)