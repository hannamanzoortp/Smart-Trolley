from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from SmartTrolleyApp.forms import *
from SmartTrolleyApp.models import *

# Create your views here.
# ////////////////////////////////////////// ADMIN ///////////////////////////////////

class LoginPage(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
            username=request.POST['username']
            password=request.POST['password']
            login_obj=LoginTable.objects.get(Username=username,Password=password)
            if login_obj.Type=="ADMIN":
                return HttpResponse('''<script>alert("welcome to admin home");window.location="/adminboard"</script>''')
            elif login_obj.Type=="Staff":
                return HttpResponse('''<script>alert("welcome to staff home");window.location="/staffhome"</script>''')
        
class AddProductPage(View):
    def get(self,request):
        return render(request,"Admin/add product.html")
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.save()
            return HttpResponse('''<script>alert("PRODUCT added succesfully");window.location="/view_product"</script>''')

    

class ViewStaffPage(View):
    def get(self,request):
        obj = StaffTable.objects.all()
        return render(request,"Admin/viewstaff.html", {'val': obj})
        
class AddStaffPage(View):
    def get(self,request):
        return render(request,"Admin/addstaff.html")
    def post(self, request):
        form = StaffForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            login_obj = LoginTable.objects.create(Username=request.POST['Username'], Password=request.POST['Password'],Type="Staff")
            login_obj.save()
            f.Login=login_obj
            f.save()
            return HttpResponse('''<script>alert("staff added succesfully");window.location="/view_staff"</script>''')

class AdminBoardPage(View):
    def get(self,request):
        return render(request,"Admin/adminboard.html")
    
class EditProductPage(View):
    def get(self,request,p_id):
        obj=ProductTable.objects.get(id=p_id)
        return render(request,"Admin/editproduct.html",{'val':obj,'date': str(obj.ManufacturingDate), 'expdate': str(obj.ExpiryDate)})
    def post(self, request, p_id):
        obj= ProductTable.objects.get(id=p_id)
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("product edit succesfully");window.location="/view_product"</script>''')
class DeleteProductPage(View):
       def get(self,request, p_id):
            obj = ProductTable.objects.get(id=p_id)
            obj.delete()
            return HttpResponse('''<script>alert("delete product succesfully");window.location="/view_product"</script>''')


class EditStaffPage(View):
    def get(self,request, s_id):
        obj = StaffTable.objects.get(id=s_id)
        return render(request,"Admin/editstaff.html",{'val': obj})
    def post(self, request, s_id):
        obj= StaffTable.objects.get(id=s_id)
        form = StaffForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("staff edit succesfully");window.location="/view_staff"</script>''')
        
class DeleteStaffPage(View):
    def get(self,request, s_id):
        obj = StaffTable.objects.get(id=s_id)
        obj.delete()
        return HttpResponse('''<script>alert("delete staff succesfully");window.location="/view_staff"</script>''')
class ViewProductPage(View):
    def get(self,request):
        obj = ProductTable.objects.all()
        return render(request,"Admin/viewproduct.html",{'val': obj})
class RegistrationPage(View):
    def get(self,request):
        return render(request,"Admin/registration.html")   
    

    
 # ////////////////////////////////// STAFF //////////////////////////////////////////////////


class CrossCheckPage(View):
    def get(self,request, c_id):
        obj = CartTable.objects.filter(id=c_id)
        return render(request,"Staff/crosscheck.html")
    
class ViewUserPage(View):
    def get(self,request):
        obj = CartTable.objects.all()
        return render(request,"Staff/viewuser.html", {'val': obj})
    
class StaffhomePage(View):
    def get(self,request):
        return render(request,"Staff/staffhome.html")  
    
class ProductDetailsPage(View):
    def get(self,request):
        return render(request,"Staff/productdetails.html")  

     
    

    
 


    
