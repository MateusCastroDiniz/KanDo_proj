# Projeto KanDo
O KanDo é um KanBan, ainda em desenvolvimento com o objetivo de familiarizar estudantes de tecnologia com o método KanBan.

## Instalação do Projeto:
Siga os comandos a seguir:

<ul>
    <li>Clone esse repositório para o seu desktop ou pasta de preferência com o comando `git clone git@github.com:MateusCastroDiniz/KanDo_proj.git` </li>
    <li>Entre na pasta clonada e crie um virtual enviroment com o comando `python3 -m venv venv`</li>
    <li>Ative seu ambiente virtual com o comando `source venv/bin/activate`</li>
    <li>Rode o comando `pip install -r requirements.txt`</li>
    <li>Inicie o projeto com o comando `python3 manage.py runserver`</li>
</ul>

### Estrutura do projeto:
```commandline
.
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── KanDo
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── factories.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_task_task_slug.py
│   │   │   ├── 0003_alter_task_task_slug.py
│   │   │   ├── 0004_alter_task_task_slug.py
│   │   │   ├── 0005_remove_task_task_slug.py
│   │   │   ├── 0006_alter_task_status.py
│   │   │   ├── 0007_alter_board_owner_alter_task_description.py
│   │   │   ├── 0008_alter_board_owner_alter_column_board_and_more.py
│   │   │   ├── 0009_alter_board_board_name.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-310.pyc
│   │   │       ├── 0002_alter_task_task_slug.cpython-310.pyc
│   │   │       ├── 0003_alter_task_task_slug.cpython-310.pyc
│   │   │       ├── 0004_alter_task_task_slug.cpython-310.pyc
│   │   │       ├── 0005_remove_task_task_slug.cpython-310.pyc
│   │   │       ├── 0006_alter_task_status.cpython-310.pyc
│   │   │       ├── 0007_alter_board_owner_alter_task_description.cpython-310.pyc
│   │   │       ├── 0008_alter_board_owner_alter_column_board_and_more.cpython-310.pyc
│   │   │       ├── 0009_alter_board_board_name.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   └── urls.cpython-310.pyc
│   │   ├── tests
│   │   │   ├── __pycache__
│   │   │   │   └── test_task.cpython-310-pytest-7.4.4.pyc
│   │   │   └── test.py
│   │   ├── urls.py
│   │   └── views
│   │       ├── board_view.py
│   │       ├── __init__.py
│   │       └── __pycache__
│   │           ├── board_view.cpython-310.pyc
│   │           └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
    ├── test_board.py
    ├── test_columns.py
    ├── test_task.py
    └── views
        ├── __init__.py
        └── test_board_view.py



```