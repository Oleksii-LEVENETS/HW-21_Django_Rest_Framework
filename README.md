# HW-21_Django_Rest_Framework  
=============================  
ДЗ 21. Django Rest Framework  
Створено: 14.03.2023 21:29  
Заняття 24. Django Rest Framework  

1. Жду ссылки на репозитории с проектом использующим DRF.  
2. В проекте реализовать:  
- минимум 2 модели с связями (Пост, Комментарий)  
- модели Поста и Комментария должны принадлежать Пользователю (FK-связь)  
- Сериализаторы для этих моделей  
- CRUD использующий viewset для работы с этими моделями так, что бы:  
     - просматривать Посты и Комментарии могли все  
     - добавлять Посты и Комментарии могли только залогиненные пользователи  
     - изменять или удалять Посты или Комментарии могли только их Владельцы (при удалении Поста все комментарии 
       удаляются вне зависимости от их Владельцов - on_delete=Cascade)

3. При желании можете использовать аутентификацию по токену.
   - ссылки:
       https://www.django-rest-framework.org/api-guide/authentication/
       https://dj-rest-auth.readthedocs.io/en/latest/index.html
       https://dj-rest-auth.readthedocs.io/en/latest/installation.html
       https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
       https://django-allauth.readthedocs.io/en/latest/installation.html
=============================

![Screenshot 2023-03-18 at 22.00.12.png](static%2FScreenshot%202023-03-18%20at%2022.00.12.png)


```bash
python3 manage.py migrate
```
# Option_1
```bash
python3 manage.py createsuperuser  
```
```bash
python3 manage.py create_users 5   
```
```bash
python3 manage.py create_new_models  
```

or

# Option_2
```bash
python3 manage.py loaddata blog/fixtures/user.json
```
```bash
python3 manage.py loaddata blog/fixtures/fresh_db.json
```

```bash
python3 manage.py runserver
```
