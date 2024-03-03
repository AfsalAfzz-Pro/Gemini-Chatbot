from django.shortcuts import render,HttpResponse
from gemini import first_talk,generate_response
import markdown
from django.http import JsonResponse

import json
from django.http import JsonResponse

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re


# Create your views here.
def HomePage(request):
    response = first_talk()
    return render (request, 'index.html', {'response':response.text})


    
def SubmitPage(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        prompt = data.get('message')
        print("hleoooooooooooooooooooo")
        print(prompt) 
        response = generate_response(prompt)
        print(response)
        
        markdown_text = markdown.markdown(response.text)
        print(type(markdown_text))
        string = markdown_text
        print(string)


        json_data = {'response123': markdown_text}
        return JsonResponse(json_data)



        # r1 = render(request, 'index.html', {'response123': markdown_text})
        # return r1
  

def WelcomePage(request):
    return render(request, 'welcome.html')