#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

basic_url = 'https://api.github.com'


def build_rul(endpoint):
	return '/'.join([basic_url, endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str), indent=4)

def request_method():
	url = build_rul('user/emails')
	response = requests.get(url, auth=('TyYouth', 'hua852456'))
	print("headers: ")
	print(response.request.headers)
	print("url: ")
	print(response.url)
	print('status code')
	print(response.status_code)
	print("reason:")
	print(response.reason)
	print("content")
	print(response.json())


if __name__ == '__main__':
	request_method()