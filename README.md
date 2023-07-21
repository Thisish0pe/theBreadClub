# 🍞 The bread club 
* 혹시 빵 좋아하시나요? 우리 함께 내 인생 빵집 공유하고 빵지순례 해봐요!

## 1. 목표 및 기능
### 1.1 목표
* Django를 이용하여 CRUD 기능을 구현할 수 있다.

### 1.2 기능
* 게시글 CRUD
* 댓글 CRD
* 게시글 제목, 작성자, 도시 카테고리 검색 기능
* 회원가입 및 로그인
* 게시글 및 댓글 작성, 수정, 삭제 권한 부여

## 2. 개발 환경 및 일정
### 2.1 개발 환경
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white"/>

### 2.2 개발기간
* 2023 년  07 월  17 일  -  2023 년  7 월  20 일

## 3. 프로젝트 ERD 및 구조
### 3.1 Entity Relationship Diagram
![default](image_README/breadpilgrimage_DB.png)
### 3.2 프로젝트 구조
```
./
├── app/
│   ├── init.py
│   ├── pycache/
│   ├── asgi.py
│   ├── settings.py
│   ├── static/
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── blog/
│   ├── init.py
│   ├── pycache/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py*
├── media/
│   └── images/
├── static/
│   └── myapp/
├── templates/
│   ├── base.html
│   └── index.html
├── user/
│   ├── init.py
│   ├── pycache/
│   ├── admin.py
│   ├── apps.py
│   ├── fomrs.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── venv/
├── bin/
├── include/
├── lib/
└── pyvenv.cfg
```
## 4. 상세 페이지 설명
### 메인페이지
* 로그인 여부 상관없이 모든 유저 입장 가능한 페이지
![default](image_README/the%20bread%20club_index.png)

### 게시글 목록 페이지
* 로그인 여부 상관없이 모든 유저가 게시글 및 댓글 열람 가능
![default](image_README/the%20bread%20club_view.png)

### 게시글 작성 및 수정 페이지
* 로그인한 유저만 가능한 페이지
* 작성자만 게시글 수정, 삭제 가능
* 로그인하지 않은 유저의 경우, 로그인 페이지 창 렌더링
![default](image_README/the%20bread%20club_write%26edit.png)

### 댓글 작성 및 수정 페이지
* 로그인한 유저만 가능한 페이지
* 작성자만 댓글 수정, 삭제 가능
![default](image_README/the%20bread%20club_comment.png)

### 로그인 및 회원가입 페이지
* 사전에 로그인되어있는 유저의 경우, 메인페이지 렌더링
![default](image_README/the%20bread%20club_join%26login.png)

## 5. 개발과정과 느낀점
* 
