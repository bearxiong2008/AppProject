#!/usr/bin/env python3
# -*- coding: utf-8 -*

#hello.py

def application(environ,start_response):
	start_response('200 ok',[('Content-Type','text/html')])
	return [b'<h1>Hello,web!</h1>']
	