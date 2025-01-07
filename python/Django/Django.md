# Django란?
## 기본 작동 방식
```
urls.py(메인) -> 하위 urls.py(앱별) -> views.py
```
## Django 프로젝트 시작하기
### 프로젝트 만들기
- Django 프로젝트 폴더를 만든다(`mkdir`등의 방법으로)
```shell
django-admin startproject 프로젝트이름 프로젝트폴더
```
- `프로젝트이름`과 `프로젝트폴더`를 잘 채우면 된다
#### 어떤게 생성될까?
- manage.py
- settings.py : Django의 설정 파일이다
- urls.py : 경로를 지정하는 파일이다. Spring Boot의 DispatcherServlet과 비슷하다
- ...
### 애플리케이션 생성
```shell
python manage.py startapp 애플리케이션이름
```
- 프로젝트 폴더 내부에 애플리케이션 폴더가 생성된다
- 이후, urls.py, view.py, templates... 등을 이용하여 시작한다
## views.py
- 클라이언트의 요청을 처리하고 응답을 반환하는 로직을 담당하는 파일
- 자바의 Controller와 비슷하다
## response
### HttpResponse
- 기본적인 Http 응답을 반환할 때 사용한다
```python
# 기본 텍스트 응답
def basic_view(request):
    return HttpResponse("Hello, World!")

# HTML 포함 응답
def html_view(request):
    html = "<h1>Hello</h1><p>This is HTML response</p>"
    return HttpResponse(html)
```
### JsonResponse
- JSON 데이터를 반환할 때 사용한다
```python
def json_dict_view(request):
    data = {
        "message": "Hello",
        "items": [1, 2, 3],
        "success": True
    }
    return JsonResponse(data)
```
### render
- 템플릿(html)을 렌더링 하여 반환할 때 사용한다. Forward 방식이다
- 템플릿에 컨텍스트(데이터)를 전달할 수 있다
```python
def render_view(request):
    context = {
        'name': '홍길동',
        'age': 20,
        'items': ['apple', 'banana', 'orange']
    }
    return render(request, 'myapp/template.html', context)
```
### redirect
- 다른 URL로 Redirect 할 때 사용한다
- 해당 프로젝트의 상대경로 또는 직접적인 URL 경로를 사용할 수 있다
```python
# URL 직접 지정
def redirect_view1(request):
    return redirect('/home/')

# URL 이름 사용
def redirect_view2(request):
    return redirect('home')  # urls.py에서 name='home'으로 지정된 URL로 이동

# 외부 URL로 리다이렉트
def redirect_external(request):
    return redirect('https://www.example.com')
```
### 응답 상태코드 설정
- 모든 응답에서 status 코드를 지정할 수 있다
```python
# HttpResponse에서 상태코드 설정
def status_view1(request):
    return HttpResponse("Not Found", status=404)

# JsonResponse에서 상태코드 설정
def status_view2(request):
    return JsonResponse({"error": "Bad Request"}, status=400)

# render에서 상태코드 설정
def status_view3(request):
    return render(request, 'error.html', status=500)
```