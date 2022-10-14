<div align="center" id="top"> 
  <img src="./static/img/retake-logo-mini-png.png" alt="Test Retake" width="100" height="100" />

  &#xa0;

  <!-- <a href="https://testretake.netlify.app">Demo</a> -->
</div>

<h1 align="center">Test Retake Brasil</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ailsonazevedo/test-retake?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ailsonazevedo/test-retake?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ailsonazevedo/test-retake?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/ailsonazevedo/test-retake?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/test-retake?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/test-retake?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/test-retake?color=56BEB8" /> -->
</p>

 <!-- Status  -->

<!-- <h4 align="center"> 
	🚧  Test Retake 🚀 Under construction...  🚧
</h4>  -->

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/ailsonazevedo" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Este projeto tem como objetivo de cadastrar, editar e remover Processos Judiciais. Conta também com um\
scraping, onde são cadastrados no banco as informações recebidas.

Tela de Login admin:\
<img src="https://i.ibb.co/yfvVNNZ/tela-login.png" alt="Tela login" />

Tela do ambiente admin:\
<img src="https://i.ibb.co/ftD2dM1/tela-admin.png" alt="Tela admin" />

Tela Inicial:\
<img src="https://i.ibb.co/WtQfxKz/tela-home.png" alt="Tela home" />

Tela de Processos:\
<img src="https://i.ibb.co/BrpHnQK/tela-process.png" alt="tela processos" />

## :sparkles: Features ##

:heavy_check_mark: Cadastrar Processos\
:heavy_check_mark: Editar Processos\
:heavy_check_mark: Remover Processos\
:heavy_check_mark: Cadastrar Partes\
:heavy_check_mark: Remover Partes\
:heavy_check_mark: Scraping de Processos

## :rocket: Technologies ##

Tecnologias e libs usadas no projeto:

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [django-bootstrap5](https://django-bootstrap-v5.readthedocs.io/en/latest/#)
- [django-jazzmin](https://django-jazzmin.readthedocs.io/)
- [Docker](https://www.docker.com/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, Para rodar o projeto você vai precisar do [Git](https://git-scm.com), [Docker](https://www.docker.com/) 
e [Python 3.10](https://www.python.org/) instalados.

## :checkered_flag: Starting ##

```bash
# Clone do projeto
$ git clone https://github.com/ailsonazevedo/test-retake

# entrar na pasta raiz do projeto
$ cd test-retake
```
Para baixar a imagem do docker:
```bash
$ docker run ailsonazevedo1/test-retake
```
Digite o seguinte comando para iniciar o container
```bash
$ docker-compose up
```
Se desejar fazer o build de uma nova imagem, digite o seguinte comando no seu terminal:
```bash
$ docker-compose up --build
```
Pronto, após iniciar o container o projeto estará disponível na seguinte url:
```bash
$ http://127.0.0.1:8000/
```
Criando um usuário no django pelo container
```bash
$ docker ps
```
Copie o id do seu container, aqui o meu id é este marcado em vermelho:\
<img src="https://i.ibb.co/QFfyFC5/tela-docker-ps.png" alt="docker ps"/>

Em seguida rode o segundo comando para entrar no modo interativo:
```bash
$ docker exec -it "containerid" sh
```
<img src="https://i.ibb.co/DQR6ndm/tela-docker-exec.png" alt="docker exec"/>

Após entrar no modo interativo basta criar o super usuário
```bash
$ python manage.py createsuperuser
```
<img src="https://i.ibb.co/RNCVV3P/tela-sh-createuser.png" alt="create user" />

Para sair do modo interativo basta digitar:
```bash
$ exit
```


<h2>Rodando Localmente:</h2>

Caso deseje rodar o projeto em uma Máquina Virtual local, siga os seguintes passos:\
1 - Crie uma Máquina Virtual
```
$ python -m venv nomedamaquina
```
2 - Ative a Máquina Virtual
```bash
# Se você usa Windows
$ nomedamaquina/Scripts/active

# Se você usa Linux
$ source nomedamaquina/bin/activate
```
3 - Instalar as Dependências
```bash
# Ele irá instalar todas as dependências encontradas no Pipfile
$ pipenv install
```
4 - Crie as Migrações
```bash
$ python manage.py migrate
```
5 - Crie um Usuário Admin
```bash
$ python manage.py createsuperuser
```
6 - Agora é só iniciar o servidor
```bash
$ python manage.py runserver
```
Url para acessar:
```bash
$ http://127.0.0.1:8000/
```
## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/ailsonazevedo" target="_blank">Ailson Azevedo</a>

&#xa0;

<a href="#top">Back to top</a>
