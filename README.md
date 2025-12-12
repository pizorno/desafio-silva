## 🌱 A Silva

Aqui, a tecnologia impulsiona nossa missão de restauração ecológica em uma escala que realmente faz a diferença. Conectamos quem produz mudas e sementes nativas com os grandes esforços de reflorestamento. Se você se identifica com um propósito de impacto real no meio ambiente e quer usar suas habilidades para viabilizar produção, compra, venda com agilidade, qualidade, diversidade e volume, queremos você no nosso time.

---

## Perfil

Procuramos pessoas desenvolvedoras que adoram resolver desafios e construir soluções, desejam usar suas habilidades para transformar o mundo participando de uma missão real de restauração.

---

## Projeto

Seu desafio é criar um **Catálogo de Espécies Nativas**. A ideia central é desenvolver uma solução que permita a organização e apresentação das espécies.

Você tem **total liberdade para definir a arquitetura e a abordagem para resolver este problema**. Isso pode incluir desde uma aplicação front-end que exibe os dados até a construção de uma API para servir essas informações ou uma combinação dos dois. Queremos saber como você pensa, resolve um problema e constrói a solução.

---

## Instruções

- Faça um **fork** deste repositório para o desenvolvimento.
- Neste repositório, em `src/data/`, há um arquivo chamado `species.json` com os dados para você trabalhar na solução. Você pode tanto carregá-los em um banco de dados quanto usar o próprio arquivo diretamente no seu projeto.
- No `README.md`, deixe instruções precisas de como podemos executar os testes e rodar a aplicação localmente.
- Quando se sentir confortável com a sua solução, abra um **Pull Request** ou nos mande o link do seu projeto.

---

## Funcionalidades

Gostaríamos de ser capazes de executar as seguintes ações na sua aplicação:

1. Listar todas as espécies cadastradas.
2. Buscar por espécies que contenham o termo ou parte dele nos campos que fazem parte do registro da espécie.
3. Navegar entre as páginas, se necessário.
4. Adicionar novas espécies e atualizar existentes.

Exemplo de alguns pontos que vamos observar no seu projeto:

- [*Twelve Factor*](https://12factor.net/pt_br/).
- Organização e Clareza.
- Testes automatizados.

Caso encontre dificuldade em algum desses pontos, **não deixe de entregar**! Para esta posição, estamos observando mais do que apenas a exatidão da solução.

---

## 🛠️ Tecnologias

Nossa filosofia é escolher a stack com melhor *fit* para entrega de uma determinada funcionalidade ou produto.  
Por isso, você tem total liberdade para usar aquilo que se sentir mais confortável para entregar este desafio. Use a linguagem e as tecnologias que facilitem o desenvolvimento da sua solução com qualidade e domínio.

---

## 📬 Próximos Passos

Ao finalizar sua solução, envie um e-mail para **talentos@silvabrasil.bio** com o link do seu **Pull Request**, perfil do **LinkedIn** e seu **currículo** (caso tenha nos encontrado pelo GitHub).  
Se o seu processo já estiver em andamento, envie o link na thread de e-mail já iniciada.

**Boa sorte! Estamos ansiosos para ver como você resolve problemas e pensa em soluções.** :seedling:

---

# 🌿 Catálogo de Espécies Nativas

Este é um sistema desenvolvido em **Django** para catalogar, listar e gerenciar espécies de plantas nativas. O projeto utiliza **Bootstrap 5** para estilização e conta com um sistema de importação de dados via JSON.

## 📋 Pré-requisitos

Certifique-se de ter instalado em sua máquina:
* Python (versão 3.8 ou superior)
* Pip (gerenciador de pacotes do Python)

---

## 🚀 Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clonar ou Baixar o Projeto
Navegue até a pasta do projeto no seu terminal:
```bash
cd catalogo_nativas

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)
Isso mantém as dependências do projeto isoladas.

Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

### 3. Instalar Dependências
Instale o Django e também o django-widget-tweaks:

pip install django
pip install django-widget-tweaks

### 4. Configurar o Banco de Dados
Crie as tabelas necessárias no banco de dados SQLite (padrão do Django):

python manage.py makemigrations
python manage.py migrate

📦 Importação de Dados (species.json)
O projeto possui um comando personalizado para carregar as espécies automaticamente a partir de um arquivo JSON.

Passo a Passo para Importar:
Preparar o Arquivo: Certifique-se de que o arquivo species.json (com os dados das espécies) esteja salvo na raiz do projeto (na mesma pasta onde está o arquivo manage.py).
Executar o Comando de Importação: No terminal, com o ambiente virtual ativado, rode:

python manage.py importar_especies

Se tudo der certo, você verá uma mensagem verde: "X espécies importadas com sucesso!"
Nota: Este script utiliza update_or_create. Isso significa que se você rodar o comando novamente, ele não duplicará os dados, apenas atualizará as informações se houver mudanças no JSON.

▶️ Rodando a Aplicação
Após configurar o banco e importar os dados, inicie o servidor de desenvolvimento:

python manage.py runserver
Acesse o sistema no seu navegador através do endereço: 👉 http://127.0.0.1:8000/

🛠️ Funcionalidades
Listagem: Visualização de todas as espécies em cards.
Busca: Filtro por nome comum, nome científico ou bioma.
Paginação: Navegação otimizada entre as páginas de resultados.
CRUD: Adicionar novas espécies e editar as existentes.
Design: Interface responsiva e limpa com Bootstrap 5.

📂 Estrutura do Projeto
catalogo_nativas/: Configurações principais do projeto.
core/: Aplicação principal.
models.py: Definição do banco de dados.
views.py: Lógica das páginas (List, Create, Update).
management/commands/importar_especies.py: Script de importação do JSON.
templates/core/: Arquivos HTML.
species.json: Arquivo de dados para carga inicial.

### Resumo rápido dos comandos para você executar agora:

1.  Crie o arquivo `species.json` na raiz com o conteúdo do anexo.
2.  `pip install django`
3.  `pip install django-widget-tweaks`
4.  `python manage.py makemigrations`
5.  `python manage.py migrate`
6.  `python manage.py importar_especies`
7.  `python manage.py runserver`