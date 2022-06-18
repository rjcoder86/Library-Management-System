# Library Management System


## Functions
### Admin
- Create Admin account and Login.
- Can view all books
- Can add new book
- Can edit existing book information
- Can delete particular book

### Student
- Create account and Login.
- Can View all books
---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6)
- Create mysql database and add details in settings.py file
- Open Terminal and Execute Following Commands :

```
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```


## API References


- Login and Register APIs
```
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/register/
```
Authorized APIs for Role Base Access
- CRUD APIs
```
http://127.0.0.1:8000/api/addbook/
http://127.0.0.1:8000/api/allbooks/
http://127.0.0.1:8000/api/editbook/id/
http://127.0.0.1:8000/api/deletebook/id/

```
## Drawbacks / LoopHoles
- Anyone can be Admin.
