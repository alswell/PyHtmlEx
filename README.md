# PyHtmlEx
A python lib to generate variable html elements.
#### Examples:
```
cd pyhtmlex/demo
python main.py
```
Then, a html file will be generated under directory "pyhtmlex/demo", just open it with your browser!
- You can just open "pyhtmlex/demo/resume.html" and "pyhtmlex/demo/code.html" to see result as well.
* * *
You can also use this lib with Django, the member function "generate" will "yield" the html content:
```
from django.http import StreamingHttpResponse

def main(request):
    body, styles = body_main()
    head = lazy_head("my PyHtmlEx", styles)
    return StreamingHttpResponse(Html(head, body).generate())

```

