### Run Server

`pip install -r requirements.txt`
`python manage.py runserver` or `./runserver.sh`

### API

- `/api/` endpoint takes `json` data `{'code': <ezhilcode as string>}`,
returns Json Response and status code as `200`. Response contains two fields `is_success`
and `result`. `is_success` is field and indicates the program execution status.
`result` is string field contains output generated by the program. In case of failure,
`result` carries exception message.

### Accessing API

```python

In [46]: import requests

In [47]: code = u'பதிப்பி "வணக்கம்!"'

In [48]: r = requests.post("http://localhost:8000/api/", json={'code': code})

In [49]: r.json()
Out[49]:
{u'is_success': True,
 u'result': u'\u0bb5\u0ba3\u0b95\u0bcd\u0b95\u0bae\u0bcd!\n'}

In [50]: print(r.json()['result'])
வணக்கம்!

In [51]: !cat /tmp/add.n
பதிப்பி "வணக்கம்!"

In [52]: r = requests.post("http://localhost:8000/api/", json={'code': open('/tmp/add.n').read()})

In [53]: r.json()
Out[53]:
{u'is_success': True,
 u'result': u'\u0bb5\u0ba3\u0b95\u0bcd\u0b95\u0bae\u0bcd!\n'}

In [54]: print(r.json()['result'])
வணக்கம்!
```


