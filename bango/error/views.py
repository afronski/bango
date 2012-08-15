# -*- coding: utf-8-*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response

class Err(object):
    """Klasa bazowa dla utrzymania porzadku"""
    def __init__(self, type, text = ''):
        self.type = type
        self.text = unicode(text)

def err404(request):
    return render_to_response('error_template/base.xhtml', { 'error': Err(404, u'Nie znaleziono strony.') })

def err500(request):
    return render_to_response('error_template/base.xhtml', { 'error': Err(500, u'Wystąpił błąd serwera.') })
