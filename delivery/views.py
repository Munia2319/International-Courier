from functools import partial
import json
import urllib3
import requests
from urllib import response
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from delivery import serializers
from delivery.models import additional_charges, currency_rate, delivery_rate,products,payment,order_info
import enum
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from  delivery.serializers import order_Serializer
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
'''@login_required
def login(request):
    return HttpResponse(
        f"Welcome {request.user.username} {request.user.first_name} {request.user.last_name}. Hello, world. You're at the polls index."
    )'''

"""class UserViewSet(APIView):
        def get(self,request):
                order_detail_view=order_details.objects.all()
                serializer=order_Serializer(order_detail_view,many=True)
                return response(serializer.data)
        def post(self):
                pass"""
@login_required
@api_view(['PUT',])
def api_view(request):
        order_info=''
        current_user=request.user
        user_name=current_user.username
        user_id=current_user.id
        '''if request.method == 'GET':
                order_detail=order_detail.objects.all()
                serializer = order_Serializer(order_detail,many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
                serializer = order_Serializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
        try:
               order_info=neww_order_info.objects.get(id=1)
        except order_info.DoesNotExist:
                return Response(status=status.HTTP_400_NOT_FOUND)

        if request.method == 'PUT':
                serializer = order_Serializer(order_info,data=request.data)
                #data={"delivery_status":"now_complete"}
                if serializer.is_valid():
                    serializer.save()
                    response_data={}
                    payment_status="complete"
                    order_id=1
                    response_data['payment_status']=payment_status
                    response_data['order_id']=order_id
                    #data["state"]="update successful"
                    #return render(request,"test.html")
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def return_api(request):

        order_id=4
        payment_status=""
        status=""
        response_data={}
        order_id=request.GET.get('order_id')
        payment_status=request.GET.get('payment_status')
        response_data['payment_status']=payment_status

        if((order_info.objects.filter(id=order_id).update(payment_status=payment_status))==0):

                response_data['status']="not successful"
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
                response_data['status']="success"
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        #neww_order_info.objects.filter(id=order_id).update(payment_status='ok_now')

@login_required
def pending_delivery(request):
        username=request.user.username
        #username="dynamic"
        pending_order=[]
        pickup_address=[]
        pending_order_pickup_address=""
        pending_order_info=""
        products_row=products.objects.all()
        order_details_row=order_info.objects.raw('SELECT * FROM delivery_order_info WHERE user_name = %s;',[username])
        for elements in order_details_row:
                if elements.delivery_status=="pending" and elements.payment_status=="done" :
                        pending_order_recipient_name=elements.recipient_name
                        pending_order_pickup_address=elements.pick_street_name+", "+elements.pick_town+", "+elements.pick_country
                        pending_order_recipient_address=elements.street_name+", "+elements.town+", "+elements.country
                        pending_order_sender_name=elements.sender_name
                        pending_order_products=elements.product_details
                        pending_order_info="Sender-name: "+pending_order_sender_name+"------"+"Recipient-name: "+pending_order_recipient_name+"------"+"Products: "+pending_order_products+"------"+"Pickup-address: "+pending_order_pickup_address+"------"+"Recipient address: "+pending_order_recipient_address
                        pending_order.append(pending_order_info)

        context={"pickup_address":pickup_address,"products":products_row,"pending_order":pending_order}
        return render(request,"pending_delivery.html",context)

@login_required
def completed_delivery(request):
        username=request.user.username
        #username="dynamic"
        completed_order=[]
        pickup_address=[]
        completed_order_pickup_address=""
        completed_order_info=""
        products_row=products.objects.all()
        order_details_row=order_info.objects.raw('SELECT * FROM delivery_order_info WHERE user_name = %s;',[username])
        for elements in order_details_row:

                if elements.delivery_status=="complete" and elements.payment_status=="done":
                        completed_order_recipient_name=elements.recipient_name
                        completed_order_pickup_address=elements.pick_street_name+", "+elements.pick_town+", "+elements.pick_country

                        completed_order_recipient_address=elements.street_name+", "+elements.town+", "+elements.country
                        completed_order_sender_name=elements.sender_name
                        completed_order_products=elements.product_details
                        completed_order_info="Sender-name: "+ completed_order_sender_name+"------"+"Recipient-name: "+completed_order_recipient_name+"---"+"Pickup-address: "+completed_order_pickup_address+"-----------"+"Products: "+ completed_order_products+"------"+"Pickup-address: "+ completed_order_pickup_address+"------"+"Recipient address: "+ completed_order_recipient_address
                        pickup_address.append(completed_order_pickup_address)
                        completed_order.append(completed_order_info)


        context={"pickup_address":pickup_address,"products":products_row,"completed_order":completed_order}
        return render(request,"completed_delivery.html",context)

@login_required
def pending_payment(request):
        username=request.user.username
        #username="dynamic"
        pending_order=[]
        pickup_address=[]
        pending_order_pickup_address=""
        pending_order_info=""
        products_row=products.objects.all()
        order_details_row=order_info.objects.raw('SELECT * FROM delivery_order_info WHERE user_name = %s;',[username])
        for elements in order_details_row:
         if elements.delivery_status=="pending" and elements.payment_status=="pending" :
                        pending_order_recipient_name=elements.recipient_name
                        pending_order_pickup_address=elements.pick_street_name+", "+elements.pick_town+", "+elements.pick_country
                        pending_order_sender_name=elements.sender_name
                        pending_order_products=elements.product_details
                        pending_payment_url=elements.payment_URL
                        pending_order_recipient_address=elements.street_name+", "+elements.town+", "+elements.country
                        pending_order_info="Sender-name: "+pending_order_sender_name+"------"+"Recipient-name: "+pending_order_recipient_name+"------"+"Pickup-address: "+pending_order_pickup_address+"-----------"+"Go Back to payment: "+pending_payment_url+"-----------"+"Products: "+pending_order_products+"-----------"+"Recipient address: "+pending_order_recipient_address
                        pickup_address.append(pending_order_pickup_address)
                        pending_order.append(pending_order_info)
        context={"pickup_address":pickup_address,"products":products_row,"pending_order":pending_order}
        return render(request,"pending_payment.html",context)

@login_required
def home_page(request):
        current_user=request.user
        username=request.user.username
        user_id=current_user.id
        fullname=current_user.first_name + " " + current_user.last_name
        #user_id=1
        #username="dynamic"
        products_row=products.objects.all()
        order_info=""

        #order_info=order_info.objects.get(id=user_id)
        context={"products":products_row, "fullname":fullname}
        return render(request,"home_page.html",context)
@csrf_protect
@login_required
def second_page(request):

        #----------------------declaration and initialization of all variables-----------------------------
        username=request.user.username
        current_user=request.user
        user_id=current_user.id
        fullname=current_user.first_name + " " + current_user.last_name
        #username="dynamic"
        selected_product_list=[]
        product_type_container=[]
        estimated_rate=0.0
        estimated_weight=0.0
        estimated_cost=0.0
        rate=0.0
        partial_payment_rate=0.0

        #-----------------------enum for charges_scheme_type------------------------------------
        class charges_scheme_type(enum.Enum):
                flat=0
                percentage=1
                per_kilo=2

        charges_in_flat=charges_scheme_type.flat.value
        charges_in_percentage=charges_scheme_type.percentage.value
        charges_in_perKilo=charges_scheme_type.per_kilo.value

        #-------------------------------enum for product_type(traditional,nontraditional)-----------------------------------------
        class product_type(enum.Enum):
                traditional=0
                non_traditional=1

        traditional_goods=product_type.traditional.value
        non_traditional_goods=product_type.non_traditional.value


        #-------------------------fetching all values from homepage's form using request.POST.get()------------------------------

        country=request.POST.get('parent')
        delivery_speed=request.POST.get('delivery_speed')
        height=request.POST.get('height')
        length=request.POST.get('length')
        weight=request.POST.get('weight')
        width=request.POST.get('width')
        state=request.POST.get('child')
        pickup_date_1=request.POST.get('pickup_date_1')
        pickup_date_2=request.POST.get('pickup_date_2')
        delivery_type=request.POST.get('delivery_type')
        weight=request.POST.get('weight')
        selected_product_list.append(request.POST.getlist('goods_type'))
        height_float=0.0
        length_float=0.0
        width_float=0.0
        weight_float=0.0

        if height=="0.0" and width=="0.0" and length=="0.0":
                weight_float=float(weight)
                volumetric_weight=weight_float

        else:

        #------------------------converting height,length and width string type to float for calculation-------------------

                height_float=float(height)
                length_float=float(length)
                width_float=float(width)

        #---------------------------------calculating volumetric weight-------------------------------------------------------------------

                volumetric_weight=(height_float*length_float*width_float)/5000

        #--------------------------fetching estimated_rate and estimated_weight for the particular volumetric_weight-----------------------------
        if delivery_type=="DOX" and estimated_weight<=2 and estimated_weight>=0.5:
                delivery_type="DOX"
                delivery_type_print="Documents"
        else:
                delivery_type="WPX"
                delivery_type_print="Package"

        delivery_rate_row=delivery_rate.objects.raw('SELECT * FROM delivery_delivery_rate WHERE country = %s AND weight >= %s AND delivery_type=%s order by weight LIMIT 1;',[country,volumetric_weight,delivery_type])

        for elements in delivery_rate_row:
            estimated_rate=elements.amount
            estimated_weight=elements.weight

        partial_payment_row=payment.objects.raw('SELECT * FROM delivery_payment;')

        for elements in partial_payment_row:
            partial_payment_rate=elements.lowest_payment_rate

        #------------------------------------starting of calculation of total_cost of delivery--------------------------------------------

        #------------------------------estimation of weight charge and adding it to the delivery-cost----------------------------------------
        if(estimated_weight<=30):
                estimated_cost=estimated_rate
        elif(estimated_cost>30):
                estimated_cost=estimated_rate*volumetric_weight

        x1=estimated_cost

        #------------------------------estimation of covid charge and adding it to the delivery-cost-------------------------------------

        if country=='Australia'or country=='Newzeland':
                covid_charge=0.0
                estimated_cost=estimated_cost+covid_charge
        else:
                covid_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="COVID-CHARGE-SCHEME";')
                for elements in covid_charge_row:
                        if(elements.scheme_type==charges_in_flat):
                                estimated_cost=estimated_cost+elements.charge_per_transaction
                        elif(elements.scheme_type==charges_in_perKilo):
                                estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                        elif(elements.scheme_type==charges_in_percentage):
                                estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))

        x2=estimated_cost
        #--------------------------estimation of fuel charge and adding it to the delivery-cost-----------------------------------------

        fuel_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="FUEL-CHARGE-SCHEME";')
        for elements in fuel_charge_row:
                if(elements.scheme_type==charges_in_flat):
                        estimated_cost=estimated_cost+elements.charge_per_transaction
                elif(elements.scheme_type==charges_in_perKilo):
                        estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                elif(elements.scheme_type==charges_in_percentage):
                        estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))

        x3=estimated_cost
        #------------------estimation of heavy item charge and adding it to the delivery-cost-----------------------------------------

        if volumetric_weight>40:
                heavy_item_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="HEAVY-ITEM-CHARGE-SCHEME(40+kg)";')

                for elements in heavy_item_charge_row:
                        if(elements.scheme_type==charges_in_flat):
                                estimated_cost=estimated_cost+elements.charge_per_transaction
                        elif(elements.scheme_type==charges_in_perKilo):
                                estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                        elif(elements.scheme_type==charges_in_percentage):
                                estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))

        x4=estimated_cost

        #----------------------estimation of pickup charge and adding it to the delivery-cost----------

        pickup_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="PICK-UP-CHARGE-SCHEME";')

        for elements in pickup_charge_row:
                if(elements.scheme_type==charges_in_flat):
                        estimated_cost=estimated_cost+elements.charge_per_transaction
                elif(elements.scheme_type==charges_in_perKilo):
                        estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                elif(elements.scheme_type==charges_in_percentage):
                        estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))

        x5=estimated_cost

        #-----------------finding if the non traditional items are included to customer's selected product list------------------------
        product_row=""
        product=""
        for selected_product in selected_product_list:
              product_list=selected_product
              for i in range(len(product_list)):
                      product=product_list[i]
                      product_row=products.objects.raw('SELECT * FROM delivery_products WHERE product_name = %s;',[product])
                      for j in product_row:
                              product_type=j.product_type
                              product_type_container.append(product_type)

        if non_traditional_goods in product_type_container:
                product_type=non_traditional_goods
                if volumetric_weight>10:
                        pickup_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="NON-TRADITIONAL-CAHRGE-SCHEME(10+kg)";')

                        for elements in pickup_charge_row:
                                if(elements.scheme_type==charges_in_flat):
                                        estimated_cost=estimated_cost+elements.charge_per_transaction
                                elif(elements.scheme_type==charges_in_perKilo):
                                        estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                                elif(elements.scheme_type==charges_in_percentage):
                                        estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))

                else:
                        pickup_charge_row=additional_charges.objects.raw('SELECT * FROM delivery_additional_charges WHERE scheme_name ="NON-TRADITIONAL-CAHRGE-SCHEME(upto-10kg)";')

                        for elements in pickup_charge_row:
                                if(elements.scheme_type==charges_in_flat):
                                        estimated_cost=estimated_cost+elements.charge_per_transaction
                                elif(elements.scheme_type==charges_in_perKilo):
                                        estimated_cost=estimated_cost+((elements.charge_per_transaction)*volumetric_weight)
                                elif(elements.scheme_type==charges_in_percentage):
                                        estimated_cost=estimated_cost+(estimated_cost*(elements.charge_per_transaction/100))
        else:
                product_type=traditional_goods

        estimated_cost_in_USD=round(estimated_cost,2)

        currency_rate_row=''

        currency_rate_row=currency_rate.objects.raw('SELECT * FROM delivery_currency_rate;')
        for rate in currency_rate_row:
                rate=rate.rate
        estimated_cost_in_BDT=round((estimated_cost_in_USD*rate),2)
        part_pay=100

        return render(request,"second_page.html",{"delivery_type_print":delivery_type_print,"part_pay":part_pay,"user_id":user_id,"username":username,"partial_payment_rate":partial_payment_rate,"weight":weight,"vol":volumetric_weight,"estimated_rate":estimated_rate,"delivery_rate_row":delivery_rate_row,"rate":rate,"x5":x5,"x1":x1,"x2":x2,"x3":x3,"x4":x4,"volumetric_weight":volumetric_weight,"estimated_cost_in_USD":estimated_cost_in_USD,"estimated_cost_in_BDT":estimated_cost_in_BDT,"covid_charge_row":covid_charge_row,"product_type":product_type,"product_type_container":product_type_container,"product_row":product_row,"product":product,"product_list":product_list,"non_traditional_goods":non_traditional_goods,"traditional_goods":traditional_goods,"delivery_speed":delivery_speed,"height":height,"weight":weight,"width":width,"country":country,"state":state,"pickup_date_1":pickup_date_1,"pickup_date_2":pickup_date_2,"length":length,"delivery_type":delivery_type,"estimated_weight":estimated_weight,"fullname":fullname})

@login_required
def test_page(request):
        current_user=request.user
        current_username=request.user.username
        fullname=current_user.first_name + " " + current_user.last_name
        order_id=current_user.id
        #tracking_id=1
        username="delivery_user"
        security_code="uwvefjpwmves"
        deliveryURL="https://7tonexpress.com:8443/"
        deliveryOrderId=23
        recipient_name=request.POST.get('recipient_name')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        state=request.POST.get('state')
        delivery_type=request.POST.get('delivery_type')
        house_number=request.POST.get('house_number')
        apartment_number=request.POST.get('apartment_number')
        town=request.POST.get('town')
        zip_code=request.POST.get('zip_code')
        street_name=request.POST.get('street_name')
        pickup_date_1=request.POST.get('pickup_date_1')
        pickup_date_2=request.POST.get('pickup_date_2')
        estimated_cost=request.POST.get('estimated_cost')
        product_list=request.POST.get('product_list')
        volumetric_weight=request.POST.get('volumetric_weight')
        estimated_weight=request.POST.get('estimated_weight')
        email_1=request.POST.get('email_1')
        email_2=request.POST.get('email_2')
        sender_name=request.POST.get('sender_name')
        sender_phn=request.POST.get('sender_phn')
        sender_email=request.POST.get('sender_email')
        pick_country=request.POST.get('pick_country')
        pick_state=request.POST.get('pick_state')
        pick_house_number=request.POST.get('pick_house_number')
        pick_apartment_number=request.POST.get('pick_apartment_number')
        pick_town=request.POST.get('pick_town')
        pick_zip_code=request.POST.get('pick_zip_code')
        pick_street_name=request.POST.get('pick_street_name')
        delivery_type_print=request.POST.get('delivery_type_print')
        #delivery_company_phn=request.POST.get('delivery_company_phn')
        po_box=request.POST.get('po_box')
        partial_payment=request.POST.get('partial_payment')
        partial_payment=float(partial_payment)
 #context={"username":username,"security_code":security_code,"amount":estimated_cost,"description":product_list,"deliveryOrderId":deliveryOrderId,"deliveryURL":deliveryURL}

        if request.method == 'POST':
                 order_details_row=''
                 response_url=""
                 #order_id=0.0
                 tracking_id="null"
                 order=order_info( tracking_id= tracking_id,user_name=current_username,sender_name=sender_name,sender_phn_number=sender_phn,sender_email=sender_email,pick_country=pick_country,pick_state=pick_state,
                 pick_town=pick_town,pick_house_number=pick_house_number,pick_street_name=pick_street_name,pick_apartment_number=pick_apartment_number,pick_zip_code=pick_zip_code,recipient_name=recipient_name,recipient_email_1=email_1,recipient_email_2=email_2,recipient_phone=phone,country=country,state=state,town=town,house_number=house_number,street_name=street_name,apartment_number=apartment_number,
                 zip_code=zip_code,delivery_type=delivery_type,product_details=product_list,pickup_date_start=pickup_date_1,pickup_date_end=pickup_date_2,delivery_status="pending",payment_status="pending",estimated_weight=estimated_weight,
                 estimated_cost=estimated_cost,volumetric_weight=volumetric_weight,payment_URL=response_url,po_box=po_box,payment_done=partial_payment)
                 order.save()

                 res_string='https://seller.buy-now.biz/ecommerce/generateurl-deliverapp?amount='+str(partial_payment)+'&description=delivery_package&deliveryOrderId='+str(order.id)+'&deliveryURL=https://7tonexpress.com:8443/payment_success/&security_code=uwvefjpwmves&user_name='+str(username)
                 response=requests.post(res_string)
                 # return redirect(str(res_string))
                 #response=requests.post('https://seller.etaka.online/ecommerce/generateurl-deliverapp?amount='+estimated_cost+'&description='+product_list+'&deliveryOrderId='+order_id+'&deliveryURL=https://courier.etaka.online:8443/delivery/order-received/2227/?key=wc_order_giBlyJPRT7eRc&security_code=uwvefjpwmves&user_name='+username)
                 #return HttpResponse(response)

                 url=""
                 jsn=""
                 response_data=response.json()
                 # return redirect(response_data["error"])
                 # return redirect(response_data["error"])

                 response_url=response_data["url"]
                 #print(str(response_data + "******************"))
                 order_info.objects.filter(id=order.id).update(payment_URL=response_url)

                 '''order_info( tracking_id= tracking_id,user_name=username,recipient_name=recipient_name,phone=phone,country=country,state=state,town=town,house_number=house_number,street_name=street_name,apartment_number=apartment_number,
                 zip_code=zip_code,delivery_type=delivery_type,product_details=product_list,pickup_date_start=pickup_date_1,pickup_date_end=pickup_date_2,delivery_status="pending",payment_status="pending",estimated_weight=estimated_weight,
                 estimated_cost=estimated_cost,volumetric_weight=volumetric_weight,payment_URL=response_url).save()'''
                 '''neww_order_info( tracking_id= tracking_id,user_name=username,sender_phn_number=sender_phn,recipient_name=recipient_name,phone=phone,recipient_email_1=email_1,recipient_email_2=email_2,country=country,state=state,town=town,house_number=house_number,street_name=street_name,apartment_number=apartment_number,
                 zip_code=zip_code,delivery_type=delivery_type,product_details=product_list,pickup_date_start=pickup_date_1,pickup_date_end=pickup_date_2,delivery_status="pending",payment_status="pending",estimated_weight=estimated_weight,
                 estimated_cost=estimated_cost,volumetric_weight=volumetric_weight,payment_URL=response_url,company_phn_number=delivery_company_phn,po_box=po_box,payment_done=partial_payment).save()
                 order_details_row=neww_order_info.objects.raw('SELECT * FROM delivery_neww_order_info WHERE user_name = %s;',[username])'''

                 order_details_row=order_info.objects.raw('SELECT * FROM delivery_order_info WHERE user_name = %s;',[username])
                 for elements in order_details_row:
                        order_id=elements.id
                 #buy_now_api(username=username,security_code=security_code,amount=estimated_cost,description=product_list,deliveryOrderId=deliveryOrderId,deliveryURL=deliveryURL).save()
                 #response = requests.get('https://eotwpn3er7w2909.m.pipedream.net',data=country)
                 #r =requests.get('https://eotwpn3er7w2909.m.pipedream.net', params =context)
                 #response=requests.post('https://eotwpn3er7w2909.m.pipedream.net', params=context)

                 if response.status_code==200:

                        #res="https://etaka.online/o?i=aHNj&a=13.16&c=1&t=7&v=SyyPIIdm&s=3a5b28708f6645708b16&d=description&is_commerce=commerceTrue&ecommerceOrderId=22&ecommerceURL=https://market.buy-now.biz/fcommerce/checkout/order-received/2227/?key=wc_order_giBlyJPRT7eRc"
                         #response_data['url'] save in database
                        return redirect(response_data["url"])

                        #return render(request,"test.html",{"url":url,"rest_str":res_string,"id":order_id,"estimated_weight":estimated_weight,"volumetric_weight":volumetric_weight,"product_list":product_list,"pickup_date_1":pickup_date_1,"pickup_date_2":pickup_date_2,"estimated_cost":estimated_cost,"street_name":street_name,"house_number":house_number,"apartment_number":apartment_number,"town":town,"zip_code":zip_code,"delivery_type":delivery_type,"recipient_name":recipient_name,"phone":phone,"country":country,"state":state
                        #})

        else:

                return render(request,"third_page.html",{"delivery_type_print":delivery_type_print,"estimated_weight":estimated_weight,"volumetric_weight":volumetric_weight,"product_list":product_list,"pickup_date_1":pickup_date_1,"pickup_date_2":pickup_date_2,"estimated_cost":estimated_cost,"street_name":street_name,"house_number":house_number,"apartment_number":apartment_number,"town":town,"zip_code":zip_code,"delivery_type":delivery_type,"recipient_name":recipient_name,"phone":phone,"country":country,"state":state,"fullname":fullname
                })

@login_required
def third_page(request):

    #-------------------------fetching all values from secondpage's form using request.POST.get()------------------------------
        username=request.user.username
        fullname=request.user.first_name + " " + request.user.last_name
        #username="dynamic"
        sender_name=request.POST.get('sender_name')
        sender_phn=request.POST.get('sender_phn')
        sender_email=request.POST.get('sender_email')

        pick_country=request.POST.get('parent')
        pick_state=request.POST.get('child')
        pick_house_number=request.POST.get('pick_house_number')
        pick_apartment_number=request.POST.get('pick_apartment_number')
        pick_town=request.POST.get('pick_town')
        pick_zip_code=request.POST.get('pick_zip_code')
        pick_street_name=request.POST.get('pick_street_name')

        delivery_type_print=request.POST.get('delivery_type_print')
        height=request.POST.get('height')
        width=request.POST.get('width')
        length=request.POST.get('length')
        weight=request.POST.get('weight')
        recipient_name=request.POST.get('recipient_name')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        state=request.POST.get('state')
        delivery_type=request.POST.get('delivery_type')
        house_number=request.POST.get('house_number')
        apartment_number=request.POST.get('apartment_number')
        town=request.POST.get('town')
        zip_code=request.POST.get('zip_code')
        street_name=request.POST.get('street_name')
        pickup_date_1=request.POST.get('pickup_date_1')
        pickup_date_2=request.POST.get('pickup_date_2')
        estimated_cost=request.POST.get('estimated_cost')
        product_list=request.POST.get('product_list')
        volumetric_weight=request.POST.get('volumetric_weight')
        estimated_weight=request.POST.get('estimated_weight')
        email_1=request.POST.get('email_1')
        email_2=request.POST.get('email_2')
        delivery_company_phn=request.POST.get('delivery_company_phn')
        po_box=request.POST.get('po_box')
        partial_payment=request.POST.get('partial_payment_in_tk')
        #if isinstance(partial_payment, str):
        if partial_payment=='':
                partial_payment=estimated_cost
                due_payment=0
        else:
                partial_payment=round(float(partial_payment),2)
                due_payment=request.POST.get('due_payment')

        partial_payment=round(float(partial_payment),2)
        due_payment=round(float(due_payment),2)

        return render(request,"third_page.html",{"delivery_type_print":delivery_type_print,"pick_country":pick_country,"pick_state":pick_state,"pick_house_number":pick_house_number,"pick_apartment_number":pick_apartment_number,
                "sender_name":sender_name,"sender_email":sender_email,"due_payment":due_payment,"username":username,"pick_town":pick_town,"pick_zip_code":pick_zip_code,"pick_street_name":pick_street_name,
                "email_2": email_2,"email_1": email_1,"sender_phn":sender_phn,"delivery_company_phn": delivery_company_phn,"po_box":po_box,"partial_payment":partial_payment,"estimated_weight":estimated_weight,"volumetric_weight":volumetric_weight,"product_list":product_list,"pickup_date_1":pickup_date_1,"pickup_date_2":pickup_date_2,"estimated_cost":estimated_cost,"street_name":street_name,"house_number":house_number,"apartment_number":apartment_number,"town":town,"zip_code":zip_code,"delivery_type":delivery_type,"height":height,"weight":weight,"width":width,"recipient_name":recipient_name,"phone":phone,"country":country,"state":state,"length":length,"fullname":fullname
        })

def success_payment(request):
        return render(request,"test.html")

'''def save_page(request):
        #username=request.user.username
        username="delivery_user"
        security_code="uwvefjpwmves"
        deliveryURL="https://courier.etaka.online:8443/delivery/order-received/2227/?key=wc_order_giBlyJPRT7eRc"
        deliveryOrderId=23
        recipient_name=request.POST.get('recipient_name')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        state=request.POST.get('state')
        delivery_type=request.POST.get('delivery_type')
        house_number=request.POST.get('house_number')
        apartment_number=request.POST.get('apartment_number')
        town=request.POST.get('town')
        zip_code=request.POST.get('zip_code')
        street_name=request.POST.get('street_name')
        pickup_date_1=request.POST.get('pickup_date_1')
        pickup_date_2=request.POST.get('pickup_date_2')
        estimated_cost=request.POST.get('estimated_cost')
        product_list=request.POST.get('product_list')
        volumetric_weight=request.POST.get('volumetric_weight')
        estimated_weight=request.POST.get('estimated_weight')
        email_1=request.POST.get('email_1')
        email_2=request.POST.get('email_2')
        sender_phn=request.POST.get('sender_phn')
        delivery_company_phn=request.POST.get('delivery_company_phn')
        po_box=request.POST.get('po_box')
        partial_payment=request.POST.get('partial_payment')

        if request.method == 'POST':

                 tracking_id=1
                 response_url="url"

                 neww_order_info( tracking_id= tracking_id,user_name=username,sender_phn_number=sender_phn,recipient_name=recipient_name,phone=phone,recipient_email_1=email_1,recipient_email_2=email_2,country=country,state=state,town=town,house_number=house_number,street_name=street_name,apartment_number=apartment_number,
                 zip_code=zip_code,delivery_type=delivery_type,product_details=product_list,pickup_date_start=pickup_date_1,pickup_date_end=pickup_date_2,delivery_status="pending",payment_status="pending",estimated_weight=estimated_weight,
                 estimated_cost=estimated_cost,volumetric_weight=volumetric_weight,payment_URL=response_url,company_phn_number=delivery_company_phn,po_box=po_box,payment_done=partial_payment).save()




        return render(request,"third_page.html",{"po_box":po_box,"partial_payment":partial_payment,"email_2":email_2,"email_1":email_1,"sender_phn":sender_phn,"delivery_company_phn":delivery_company_phn,"estimated_weight":estimated_weight,"volumetric_weight":volumetric_weight,"product_list":product_list,"pickup_date_1":pickup_date_1,"pickup_date_2":pickup_date_2,"estimated_cost":estimated_cost,"street_name":street_name,"house_number":house_number,"apartment_number":apartment_number,"town":town,"zip_code":zip_code,"delivery_type":delivery_type,
        "recipient_name":recipient_name,"phone":phone,"country":country,"state":state
                })
'''
