## Projeto criado no intuito de aprender mais sobre a api [Face Recognition](https://github.com/ageitgey/face_recognition), criada por [Adam Geitgey](https://github.com/ageitgey). 

> **Foram utilizados:** Flask e Face Recognition.
 

## 1. Instalando a Virtualenv:
```
~$ sudo pip3 install virtualenv
```
#
## 2. Clonando o repositório:
```
~$ git clone https://github.com/rodrigogmartins/face-recognition.git`
```
#
## 3. Criando e configurando a Virtualenv para o Python3:
```
~$ cd face-recognition
~$ mkdir venv
~$ virtualenv --python='/usr/bin/python3' venv
```
#
## 4. Ambiente virtual:
   1. #### Iniciando:
        ```
        ~$ source venv/bin/activate
        ```
   1. #### Parando:
        ```
        (venv) ~$ deactivate
        ```
#
## 5. Dependências:
   1. #### Instalando:
        ```
        (venv) ~$ pip install -r requirements.txt
        ```
   1. #### Desinstalando:
        ```
        (venv) ~$ pip uninstall -r requirements.txt
        ```
   1. #### Salvando lista de dependências, já instaladas, ao arquivo *requirements.txt*:
        ```
        (venv) ~$ pip freeze > requirements.txt
        ```
#
## 6. Rodando o programa:
```
(venv) ~$ python runserver.py
```
#
## Autor: [Rodrigo Martins.](https://github.com/ageitgey)
#

## Face Recognition: [repository link.](https://github.com/ageitgey/face_recognition)
## Adam Geitgey (The Face Recognition creator): [GitHub link.](https://github.com/ageitgey)
