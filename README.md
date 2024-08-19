# Residência prática_01:

## 🔎 Sobre o Projeto

Este projeto consiste em uma API RESTful para uma biblioteca, desenvolvida utilizando Django e Django Rest Framework. O principal objetivo da API é permitir a gestão de livros, oferecendo funcionalidades como criação, leitura, atualização e exclusão (CRUD) de registros de livros. Com isso, é possível realizar operações como adicionar novos livros, visualizar a lista de livros disponíveis, editar informações de livros existentes e remover livros da biblioteca.

A API foi projetada para ser simples e intuitiva, facilitando a integração com outras aplicações ou o uso em sistemas que necessitem de uma base de dados de livros. Além disso, o projeto inclui a configuração do CORS (Cross-Origin Resource Sharing) para permitir que outras aplicações possam consumir a API de forma segura.

Esta aplicação foi feita com o intuito de aprender mais sobre a criação de APIs com Django, gerando uma solução prática para a gestão de livros em uma aplicação web.

##

## 🖼️ Imagens:

### Exemplo de uma requisição GET para retornar todos os livros:

![PREVIEW1][preview-preview1]

##

## 🔨 Construído com:

* 💻 VS Code
* 🐍 Python : 3.11.9 
* 🛠️ Django Rest Framework

##

## 👨🏽‍💻 Tecnologias Utilizadas:

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python" style="vertical-align:top; margin:4px"> <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="django" style="vertical-align:top; margin:4px">

##

# ⭐️ Começando:

### Para obter uma cópia local e executar os projeto, siga as etapas a seguir:

##

### 💻 Pré-requisitos:

* Git
```sh
sudo apt-get install git
```
##

* Python
```sh
sudo apt-get install python3.11.9
```
##

* Pip
```sh
sudo apt-get install python3-pip
```

##

* Conda (Anaconda/Miniconda)
    Certifique-se de que o Conda esteja instalado em seu sistema. Se não estiver, você pode baixar e instalar aqui: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

##

### 🚀 Instalação:
 
1. Clone o repositório
```sh
git clone https://github.com/MarcusCSPereira/Residencia_Django_biblioteca-API.git
```
##

2. Navegue até o diretório do projeto:
```sh
cd Residencia_Django_biblioteca-API
```
##

3. Crie um ambiente virtual usando o Conda com Python 3.11.9 e ative-o:
```sh
conda create --name biblioteca_api python=3.11.9
conda activate biblioteca_api
```
##

4. Instale as dependências necessárias (Django, Django Rest Framework, e CorsHeader):
```sh
pip install django djangorestframework corsheaders

```
##

<!-- USAGE EXAMPLES -->
### 🐍 Utilizando o projeto:

1. Navegue até o diretório do projeto:
```sh
cd Residencia_Django_biblioteca-API
```

##

2. Inicie o servidor utilizando o seguinte comando na linha de comando:
```sh
python3 manage.py runserver
```

##

3. Acesse a URL disponibilizada pelo terminal:

    Ex: http://127.0.0.1:8000/

##

4. Agora utilize o projeto com as urls ou utilize http://localhost:8000/ em algum software de teste de API's como o Insomnia ou o Postman para testar as requisições:

    Ex:

    http://127.0.0.1:8000/livros
    http://127.0.0.1:8000/livros/3

    Uma requisição POST pelo insomnia criando um livro:

    ![PREVIEW2][preview-preview2]

##

<!-- CONTACT -->
## 📫 Contato

<div align="left">
  <a href="https://www.linkedin.com/in/marcus-césar-santos-pereira-70991a28a/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="47" height="35" alt="linkedin logo"  />
  </a>
  <a href="contato.marcuscspereira@gmail.com" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/gmail/default.svg" width="47" height="35" alt="gmail logo"  />
  </a>
  <a href="https://www.instagram.com/_marcus.cesar/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/instagram/default.svg" width="47" height="35" alt="instagram logo"  />
  </a>
</div>

<!-- MARKDOWN LINKS & IMAGES -->
[preview-preview1]: preview/preview_1.png
[preview-preview2]: preview/preview2.png

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
