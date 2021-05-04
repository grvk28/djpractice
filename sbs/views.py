from django.shortcuts import render,redirect,get_object_or_404
from .forms import m,m1,n,n1
from .models import Items,t1
#, ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import UpdateView,DeleteView
#from django.urls import reverse
import csv, sqlite3
from django.http import StreamingHttpResponse
import pandas as pd
from django.http import HttpResponse

def i(request):
    csv_fp = open(f'sbs/data.csv', 'r')
    reader = csv.reader(csv_fp)
    read = pd.read_csv("sbs/data.csv")
    fields = []
    rows = []
    with open('sbs/data.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
# Following command skips the first row of the CSV file:
        fields = next(data)
        for row in data:
            #print(row[1])
            li=row
            a=li[0]
            b=li[1]
            c=li[2]
            d=li[3]
            e=li[4]
            f=li[5]
            g=li[6]
            h=li[7]
            i=li[8]
            j=li[9]
            k=li[10]
            l=li[11]
            m=li[12]
            n=li[13]
            o=li[14]
            p=li[15]
            q=li[16]
            r=li[17]
            s=li[18]
            #uncomment below line to add more entries into table
            #t1.objects.create(business_code=a, cust_number=b, name_customer=c, clear_date=d, buisness_year=e, doc_id=f, posting_date=g, document_create_date=h, document_create_date1=i, due_in_date=j, invoice_currency=k, document_type=l, posting_id=m, area_business=n, total_open_amount=o, baseline_create_date=p, cust_payment_terms=q, invoice_id=r, isOpen=s)
            #print(s)
            #print(', '.join(row))
    #print("\nTotal no. of rows: %d"%(data.line_num))
    #print('Field names are:')
    #print(', '.join(field for field in fields))

    #headers = [col for col in reader.fieldnames]
    #out = [row for row in reader]
    #print(out[0])
    myitems=t1.objects.all()
    context={
        'It': myitems
        #"Quantity":myitems.Quantity
        #'status': myitems.status
    }
    return render(request, 'h.html', context)

# Create your views here.


def add1(request):
    #n=forms.n
    list2 = n() 
    if request.method =="POST":
        form = n(request.POST) 
        if form.is_valid():
            business_code=form.cleaned_data.get('business_code')
            cust_number=form.cleaned_data.get('cust_number')
            name_customer=form.cleaned_data.get('name_customer')
            clear_date=form.cleaned_data.get('clear_date')
            buisness_year=form.cleaned_data.get('buisness_year')
            doc_id=form.cleaned_data.get('doc_id')
            posting_date=form.cleaned_data.get('posting_date')
            document_create_date=form.cleaned_data.get('document_create_date')
            document_create_date1=form.cleaned_data.get('document_create_date1')
            due_in_date=form.cleaned_data.get('due_in_date')
            invoice_currency=form.cleaned_data.get('invoice_currency')
            document_type=form.cleaned_data.get('document_type')
            posting_id=form.cleaned_data.get('posting_id')
            area_business=form.cleaned_data.get('area_business')
            total_open_amount=form.cleaned_data.get('total_open_amount')
            baseline_create_date=form.cleaned_data.get('baseline_create_date')
            cust_payment_terms=form.cleaned_data.get('cust_payment_terms')
            invoice_id=form.cleaned_data.get('invoice_id')
            isOpen=form.cleaned_data.get('isOpen')
            t1.objects.create(business_code=business_code, cust_number=cust_number, name_customer=name_customer, clear_date=clear_date, buisness_year=buisness_year, doc_id=doc_id, posting_date=posting_date, document_create_date=document_create_date, document_create_date1=document_create_date1, due_in_date=due_in_date, invoice_currency=invoice_currency, document_type=document_type, posting_id=posting_id, area_business=area_business, total_open_amount=total_open_amount, baseline_create_date=baseline_create_date, cust_payment_terms=cust_payment_terms, invoice_id=invoice_id, isOpen=isOpen)
            #obj = views.objects.get('index')
            return redirect(i)
      
    return render(request,"add1.html",{'form':list2})


class update1(UpdateView):
    model=t1
    form_class=n1
    template_name='update1.html'
    redirect=i

def delete1(request,id):
    obj=t1.objects.filter(id=id).delete()
    #t1.objects.all().delete() #deletes all the rows of the table
    return redirect(i)

def dl(request,id): #row downloader
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="row.csv"'

    writer = csv.writer(response)
    writer.writerow(['business_code','cust_number','name_customer','clear_date','buisness_year','doc_id','posting_date','document_create_date','document_create_date','due_in_date','invoice_currency','document_type','posting_id','area_business','total_open_amount','baseline_create_date','cust_payment_terms','invoice_id','isOpen'])
    users = t1.objects.filter(id=id).values_list('business_code','cust_number','name_customer','clear_date','buisness_year','doc_id','posting_date','document_create_date','document_create_date','due_in_date','invoice_currency','document_type','posting_id','area_business','total_open_amount','baseline_create_date','cust_payment_terms','invoice_id','isOpen')
    for user in users:
        writer.writerow(user)

    return response
    #return redirect(i)

def filter2(request):
    query=request.GET.get('q')
    result=t1.objects.filter(invoice_id=query)
    context={
        'It':result
    }
    
    return render(request,"h.html",context)

@login_required
def index(request):
    user=request.user
    myitems=Items.objects.filter(user=user)
    context={
        'It': myitems
        #"Quantity":myitems.Quantity
        #'status': myitems.status
    }
    return render(request,"index.html",context)

def index1(request):
    return render(request,"index.html")

@login_required
def add(request):
    user=request.user
    list1 = m() 
    if request.method =="POST":
        form = m(request.POST) 
        if form.is_valid():
            Item=form.cleaned_data.get('Item')
            Quantity=form.cleaned_data.get('Quantity')
            status=form.cleaned_data.get('status')
            date=form.cleaned_data.get('date')
            Items.objects.create(user=user,Item=Item, Quantity=Quantity,slug=user.username, status=status,date=date)
            #obj = views.objects.get('index')
            return redirect(index)
      
    return render(request,"add.html",{'form':list1})

class update(UpdateView):
    model=Items
    form_class=m1
    template_name='update.html'
    redirect=index
    

@login_required
def delete(request,id):
    obj=Items.objects.filter(id=id).delete()
    return redirect(index)
            #print(form.errors)
    #return reverse("index")

@login_required  
def filter(request):
    query=request.GET.get('q')
    result=Items.objects.filter(date=query)
    user=request.user
    re=result.filter(user=user)
    context={
        'It':re
    }
    
    return render(request,"index.html",context)



            