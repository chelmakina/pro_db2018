# -*- coding: utf-8 -*-
from bottle import template, run, route, get
import faker
import json
f = faker.Faker('fa_IR')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('/phone/get')
def phone_gen():
    return f.phone_number()

@get('/name/get')
def name_gen():
    return f.name()

@get('/user/get')
def user_gen():
    return json.dumps({
        'name':f.name(),
        'phone':f.phone_number()
    })


run(host='localhost', port=8080, debug=True, reloader=True)