from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'newsapp/home.html')

def business_view(request):
    h1 ="Targeting Vivek Ramaswamy for being Hindu is chilling"
    h2 = "jio ka paisa badh gay hai"
    h3 = "Ethanol blending badhega , carburater bike chhod do"

    type = 'business'
    my_dict = {'type':type,'h1':h1,'h2':h2,'h3':h3}
    return render(request,'newsapp/news.html',context=my_dict)

def sports_view(request):
    h1 = "Shashi Tharoor furious over Vaibhav Suryavanshi's omission from Team India"
    h2 ="Shubman Gill not selected again as alternate squad of dropped players picked for T20"
    h3 = "Returning to the Vijay Hazare Trophy after seven years, Rohit Sharma impressed fans not"
    type = 'sports'
    my_dict = {'type':type,'h1':h1,'h2':h2,'h3':h3}

    return render(request,'newsapp/news.html',context=my_dict)

def entertainment_view(request):
    h1 = "Dhurandhar box office collection day 21: Ranveer Singh film takes big jump on"
    h2 = "'Akhanda 2' box office collections day 14: Nandamuri Balakrishna's film gets Christmas boost; movie earns Rs 1.65 crore"
    h3 = "37.4K Followers Ranveer out of Don 3, Akshaye Khanna exits Drishyam 3"
    type = 'entertainment'
    my_dict = {'type':type,'h1':h1,'h2':h2,'h3':h3}
    return render(request,'newsapp/news.html',context=my_dict)