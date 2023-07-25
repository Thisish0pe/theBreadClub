# 🍞 The bread club 
 👨‍🍳 혹시 빵 좋아하시나요? 우리 함께 나의 인생 빵집 공유하고 빵지순례 해봐요!

## 1. 목표 및 기능
### 1.1 목표
* Django를 이용하여 CRUD 기능을 구현할 수 있다.

### 1.2 기능
* 게시글 CRUD
* 댓글 CRD
* 게시글 제목, 작성자, 도시 카테고리 검색 기능
* 회원가입 및 로그인
* 유저 권한 부여 - 게시글 및 댓글 작성, 수정, 삭제
* 게시글 조회 수

## 2. 개발 환경 및 일정
### 2.1 개발 환경
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white"/>

### 2.2 개발기간
* 2023 년  07 월  17 일  -  2023 년  7 월  20 일

## 3. 프로젝트 ERD 및 구조
### 3.1 Entity Relationship Diagram
![breadpilgrimage_DB](https://github.com/Thisish0pe/theBreadClub/assets/130428546/793928da-e6d6-4414-925f-c4ebd8274ebb)

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
* 로그인 여부 상관없이 모든 유저가 게시글 및 댓글 열람 가능
![thebreadclub_메인창](https://github.com/Thisish0pe/theBreadClub/assets/130428546/2063c31f-f092-460b-b635-1abae0f04098)


### 게시글 작성 및 수정 페이지
* 로그인한 유저만 가능한 페이지
* 작성자만 게시글 수정, 삭제 가능
* 로그인하지 않은 유저의 경우, 로그인 페이지 창 렌더링
<img width="1355" alt="thebreadclub_글 작성 및 수정" src="https://github.com/Thisish0pe/theBreadClub/assets/130428546/faa0d2d7-fb4e-4f15-8576-bb4b0e06e540">


### 댓글 작성 및 수정 페이지
* 로그인한 유저만 가능한 페이지
* 작성자만 댓글 수정, 삭제 가능
![thebreadclub_댓글창](https://github.com/Thisish0pe/theBreadClub/assets/130428546/7461c93f-8016-47b2-a53f-857be00b7994)


### 로그인 및 회원가입 페이지
* 사전에 로그인되어있는 유저의 경우, 메인페이지 렌더링
<img width="1686" alt="thebreadclub_회원가입 및 로그인" src="https://github.com/Thisish0pe/theBreadClub/assets/130428546/ccd72c9b-dbcf-4396-b9c9-5f541dc8d61f">

## 5. 전체적인 기능
gif 준비중입니다 :)

## 6. 개선점
* 사진 업로드 시, 사진 크기를 유저가 한 번에 볼 수 있도록 줄이고, 여러 사진을 원하는 위치에 업로드할 수 있는 기능이 필요합니다.

* 개인 프로필 페이지 CRUD 구현 및 좋아요 기능, 대댓글 구현을 추가하여 본인을 소개하고 유저들끼리의 활발한 커뮤니케이션이 가능한 장이 될 수 있도록 하여 웹이 더욱 활발하게 사용될 수 있도록 하는 것이 필요합니다.

* 비밀번호 수정을 가능하게 하여 보안성을 높이는 것이 필요합니다.

## 7. 느낀점
* Django 와 친해지는 계기가 되었습니다.

    * 배운 것을 토대로 새로운 기능을 구현하는 값진 경험이었습니다. 사진 업로드, 검색창 구현 등 처음 시도해보는 기능들을 구현하는 과정에서 공식문서와 친해지고, 구글링하는 법을 익힐 수 있는 값진 경험이었습니다.

* ERD 의 중요성을 깨달을 수 있었습니다.

    * 구현 시작에 급급해하는 것이 아닌 ERD 구현에 충분한 시간을 들이는 것의 중요성을 배울 수 있었습니다. ERD 를 탄탄하게 구축해둔다면 혼란스러워하지 않고 코딩을 할 수 있기 때문에 되려 시간을 절약할 수 있을 것입니다. 이번 프로젝트의 경우, 그러지 못하여 불필요한 수정의 과정을 많이 거쳐 시간을 효율적으로 사용하지 못했다는 점이 아쉬웠습니다.
    * 큰 그림과 세부사항을 구체적으로 형상화 시켜야 어느 한 부분에서만 시간을 크게 할애하지 않고 전체적으로 프로젝트를 완성시킬 수 있음을 배웠습니다.
