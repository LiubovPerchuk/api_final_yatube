##  ![yatube](https://user-images.githubusercontent.com/120508656/229375003-27d9b0fd-16be-41a7-b43d-6bec48625f87.JPG)   API for YaTube
   

### Описание
Api для социальной сети yatube https://github.com/LiubovPerchuk/hw05_final

### Реализован функционал дающий возможность:
- Подписываться на пользователя.
- Просматривать, создавать новые, удалять и изменять посты.
- Просматривать и создавать группы.
- Комментировать, смотреть, удалять и обновлять комментарии.
- Фильтровать по полям.


### Как запустить проект:

#### 1. Клонируем репозиторий и заходим в папку с проектом
   
    git@github.com:LiubovPerchuk/api_final_yatube.git
    
    
    cd yatube_api
    
    
#### 2. Создаем и активируем виртуальное окружение:
    
    python3 -m venv env
    
   * Если у вас Linux/macOS

    
    source env/bin/activate
    

   * Если у вас windows

    
    source env/scripts/activate
    

#### 3. Устанавливаем зависимости из файла requirements.txt:
    
    python3 -m pip install --upgrade pip
    
    pip install -r requirements.txt
    

#### 4. Выполняем миграции:
    
    python3 manage.py migrate
    
    
#### 5. Запускаем проект:

    
    python3 manage.py runserver
    
    
### Требования
    
    Django==3.2.16
    pytest==6.2.4
    pytest-pythonpath==0.7.3
    pytest-django==4.4.0
    djangorestframework==3.12.4
    djangorestframework-simplejwt==4.7.2
    Pillow==9.3.0
    PyJWT==2.1.0
    requests==2.26.0
    
