import requests

api_server = 'http://api_server:5000'

def test_add_key():
    test_key = 'test_key1'
    res = requests.get(f'{api_server}/cnt/{test_key}')
    assert res.status_code == 200
    cnt = res.json()['count']

    res = requests.get(f'{api_server}/cnt/{test_key}')
    assert res.status_code == 200
    assert res.json()['count'] == cnt + 1


class TestMySimpleApp:
    def test_add_invalid_form(self):
        data = {
            'op1': 1,
        }
        res = requests.post(f'{api_server}/op/add', data=data)
        assert res.status_code in [400, 500]

    def test_add_invalid_method(self):
        data = {
            'op1': 1,
            'op2': 2,
        }
        res = requests.get(f'{api_server}/op/add', data=data)
        assert res.status_code == 405

    def test_add(self):
        data = {
            'op1': 1,
            'op2': 3,
        }
        res = requests.post(f'{api_server}/op/add', data=data)
        res.raise_for_status()
        assert res.json()['sum'] == data['op1'] + data['op2']
