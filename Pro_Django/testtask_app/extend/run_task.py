import sys
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests
from os.path import dirname, abspath


@ddt
class InterfaceTest(unittest.TestCase):

    @unpack
    @file_data("test_data_list.json")
    def test_run_cases(self, url, method, headers, parameter_type, parameter_data, assert_type, assert_res):


        # 处理parameter_data
        if parameter_data != "":
            del_parameter = parameter_data.replace("'", '"')
            try:
                parameter_data = json.loads(del_parameter)
            except json.decoder.JSONDecodeError:
                return JsonResponse({"result": "参数类型错误"})

        # 处理headers
        if headers != "":
            del_headers = headers.replace("'", '"')
            try:
                headers = json.loads(del_headers)
            except json.decoder.JSONDecodeError:
                return JsonResponse({"result": "header类型错误"})

        if method == "get":
            if headers == "":
                if parameter_data != "":
                    r = requests.get(url, params=parameter_data)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
                else:
                    r = requests.get(url)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
            else:
                if parameter_data != "":
                    r = requests.get(url, params=parameter_data, headers=headers)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
                else:
                    r = requests.get(url,headers=headers)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)

        if method == "post":

            if parameter_type == "form-data":
                if headers == "":
                    r = requests.post(url, data=parameter_data)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
                else:
                    r = requests.post(url, data=parameter_data, headers=headers)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)

            if parameter_type == "json":
                if headers == "":
                    r = requests.post(url, json=parameter_data)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
                else:
                    r = requests.post(url, json=parameter_data, headers=headers)
                    if assert_type == "include":
                        self.assertIn(assert_res, r.text)
                    if assert_type == "equal":
                        self.assertEqual(assert_res, r.text)
        #
        # print(url)
        # print(method)
        # print(headers)
        # print(parameter_type)
        # print(parameter_data)
        # print(assert_type)
        # print(assert_res)

if __name__ == "__main__":

    unittest.main(verbosity=2)