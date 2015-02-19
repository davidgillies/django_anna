from django.shortcuts import render
from django.http import HttpResponse
import json
import simplejson
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("""<h1>
    Hello World</h1>""")


def get_template(output_type):
    return {'select': 'my_app/select.html', 'radio':'my_app/radio.html', 'cam_radio':'my_app/cam_radio.html'}[output_type]


@csrf_exempt
def json_post(request):
    """Method takes posted json returns json with surname and forenames"""
    if request.method == 'POST':
        JSONdata = request.body
        json_dict = simplejson.JSONDecoder().decode(JSONdata)
        response_data = {}
        response_data['surname'] = json_dict['surname']
        response_data['forenames'] = json_dict['forenames']
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    if request.method == 'GET':
        response_data = {}
        response_data['surname'] = 'Melachrou'
        response_data['forenames'] = 'Anna'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def normal_post(request):
    """Method takes standard POST, e.g. not json, returns json with surname and forenames"""
    if request.method == 'POST':
        response_data = {}
        response_data['surname'] = request.POST.get('surname')
        response_data['forenames'] = request.POST.get('forenames')
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    if request.method == 'GET':
        response_data = {}
        response_data['surname'] = 'Melachrou'
        response_data['forenames'] = 'Anna'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        
def basic_get(request):
    use_template = get_template(request.GET.get('output_type', ''))
    options = {1:['Cambridge','idsurgery_Cambridge'], 2:[ 'Wisbech','idsurgery_Wisbech'], 3:[ 'Ely', 'idsurgery_Ely'], 4:[ 'Glasgow', 'idsurgery_Glasgow']}
    result ={'question': "Q1", 'options': options, 'var_name': "my_var", 'obj_id': 2 }
    return render(request, use_template, result)
