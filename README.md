README.md

# BiblioTech

**Repositório:** https://github.com/iagogomes07/bibliotech

**Integrantes:**

- Iago Pereira Gomes
- Saulo dos Santos
- Kaio Henrique

---

## Sobre o Projeto

O **BiblioTech** é um sistema responsável por gerir o funcionamento de uma biblioteca, permitindo cadastrar livros e usuários, controlar empréstimos e devoluções, realizar buscas e acompanhar a disponibilidade dos livros.

---

# 1. Escopo do Projeto

Fazem parte do escopo do projeto:

- Gerenciamento do cadastro de livros;
- Gerenciamento do cadastro de leitores;
- Consulta e pesquisa de livros;
- Consulta da disponibilidade dos livros;
- Registro de empréstimos;
- Registro de devoluções;
- Acompanhamento dos empréstimos realizados;
- Geração de relatórios relacionados ao acervo e aos empréstimos;
- Disponibilização de uma API REST própria para consulta de dados do sistema;
- Integração com uma API externa relacionada a informações de livros;
- Autenticação e controle de acesso conforme o perfil do usuário;
- Interface web responsiva para utilização em computadores e dispositivos móveis.

---

# 2. Usuários do Sistema

O uso do sistema se limita aos seguintes grupos:

### Bibliotecários

Principais usuários responsáveis pelo gerenciamento do acervo, cadastro de usuários, controle de empréstimos e devoluções e consulta de informações.

### Leitores / Usuários da Biblioteca

Utilizarão o sistema para consultar livros, verificar sua disponibilidade e acompanhar informações relacionadas aos seus empréstimos.

### Administrador do Sistema

Responsável pelo gerenciamento dos usuários e pela manutenção das configurações e informações administrativas da aplicação.

### Equipe de Desenvolvimento

Responsável pela análise, desenvolvimento, testes, manutenção e evolução do BiblioTech.

### Gestão da Biblioteca

Utilizará as informações e relatórios fornecidos pelo sistema para acompanhar o funcionamento da biblioteca e apoiar a tomada de decisões.

---

# 3. Principais Funcionalidades

## 3.1 Gerenciamento de Livros

- Cadastrar livros;
- Consultar livros;
- Alterar informações dos livros;
- Excluir livros;
- Pesquisar livros por diferentes critérios;
- Consultar a disponibilidade dos livros.

## 3.2 Gerenciamento de Leitores

- Cadastrar leitores;
- Consultar leitores;
- Alterar dados dos leitores;
- Excluir leitores;
- Consultar o histórico de empréstimos.

## 3.3 Gerenciamento de Empréstimos

- Registrar empréstimos;
- Registrar devoluções;
- Consultar empréstimos;
- Identificar livros disponíveis e emprestados;
- Acompanhar os prazos de devolução.

## 3.4 Relatórios

- Gerar relatório de livros cadastrados;
- Gerar relatório de empréstimos;
- Apresentar indicadores sobre livros disponíveis e emprestados;
- Permitir a visualização, exportação ou impressão dos relatórios.

## 3.5 API REST

- Disponibilizar informações selecionadas do sistema por meio de endpoints REST;
- Permitir consultas utilizando métodos HTTP;
- Retornar dados no formato JSON;
- Fornecer respostas com códigos HTTP adequados.

## 3.6 Integração Externa

- Consultar informações de livros por meio de uma API externa;
- Utilizar os dados obtidos pela API em uma funcionalidade real do sistema.

---

# 4. Restrições do Projeto

O projeto conta com as seguintes restrições:

- O backend da aplicação deverá ser desenvolvido utilizando **Python e Django**;
- O sistema deverá utilizar um **banco de dados relacional**;
- A API REST deverá ser implementada utilizando **Django REST Framework** ou tecnologia equivalente devidamente justificada;
- O projeto deverá possuir documentação e código versionados no **GitHub**;
- Informações sensíveis, como senhas, tokens, chaves de API e arquivos `.env`, não poderão ser armazenadas no repositório;
- A aplicação deverá possuir interface responsiva;
- A versão final deverá ser disponibilizada publicamente na Internet;
- O desenvolvimento deverá respeitar o prazo estabelecido para a entrega do projeto.

---

# 5. Premissas

O projeto considera as seguintes premissas:

- Os usuários possuirão acesso à Internet para utilizar a aplicação web;
- Os dados cadastrados no sistema serão fornecidos e mantidos pela biblioteca;
- Os usuários possuirão informações válidas para realização dos cadastros;
- A biblioteca terá acesso a computadores ou dispositivos móveis compatíveis com navegadores modernos;
- A API externa escolhida estará disponível durante o desenvolvimento e utilização da aplicação;
- Os usuários responsáveis pelo gerenciamento da biblioteca receberão orientação básica para utilização do sistema;
- Os dados utilizados durante o desenvolvimento e demonstração poderão ser fictícios;
- O sistema será desenvolvido inicialmente para atender às necessidades de uma biblioteca.

---

# 6. Riscos Iniciais

| Risco                                         | Probabilidade | Impacto | Estratégia de Mitigação                                                                         |
| --------------------------------------------- | ------------- | ------- | ----------------------------------------------------------------------------------------------- |
| Atraso no desenvolvimento                     | Média         | Alto    | Dividir as atividades entre os integrantes e acompanhar o progresso por meio de um backlog.     |
| Indisponibilidade da API externa              | Média         | Médio   | Escolher uma API confiável e implementar tratamento para falhas de conexão e indisponibilidade. |
| Falhas na integração entre frontend e backend | Média         | Alto    | Realizar testes frequentes das funcionalidades e das APIs durante o desenvolvimento.            |
| Perda ou inconsistência de dados              | Baixa         | Alto    | Utilizar banco de dados relacional e realizar validações nas informações recebidas.             |
| Dificuldade na implementação da API REST      | Média         | Médio   | Definir previamente os endpoints e utilizar Django REST Framework.                              |
| Problemas de segurança                        | Média         | Alto    | Utilizar autenticação, validação de dados e manter informações sensíveis fora do código-fonte.  |
| Falta de conhecimento técnico da equipe       | Média         | Médio   | Dividir responsabilidades e realizar pesquisas e testes durante o desenvolvimento.              |
| Alterações de requisitos durante o projeto    | Média         | Médio   | Registrar alterações e avaliar seus impactos antes de incorporá-las ao projeto.                 |

---

# 7. Critérios de Sucesso

O BiblioTech será considerado bem-sucedido se:

- Permitir o cadastro, consulta, alteração e exclusão das principais informações do sistema;
- Permitir pesquisar livros de maneira eficiente;
- Permitir registrar empréstimos e devoluções corretamente;
- Apresentar a disponibilidade dos livros de forma clara;
- Gerar pelo menos um relatório com informações consolidadas da biblioteca;
- Disponibilizar uma API REST própria funcional e documentada;
- Integrar uma API externa de maneira útil para o usuário;
- Validar os dados inseridos e apresentar mensagens adequadas em caso de erro;
- Possuir uma interface responsiva e consistente com a identidade visual definida;
- Funcionar corretamente no ambiente de hospedagem previsto para a entrega final;
- Manter os documentos e o código do projeto organizados e versionados no GitHub;
- Atender aos requisitos definidos na Fase 1 e manter correspondência entre a documentação e a implementação da Fase 2.

---

# 8. Atores e Casos de Uso

O sistema possui três atores principais:

### Leitor

Responsável principalmente pela consulta das informações disponíveis no sistema, como:

- Pesquisar livros;
- Consultar livros;
- Consultar disponibilidade;
- Consultar informações relacionadas aos seus empréstimos.

### Bibliotecário

Responsável pelas principais operações de gerenciamento da biblioteca:

- Cadastrar livros;
- Alterar livros;
- Excluir livros;
- Cadastrar leitores;
- Consultar leitores;
- Alterar leitores;
- Excluir leitores;
- Consultar histórico;
- Registrar empréstimos;
- Registrar devoluções;
- Consultar empréstimos;
- Gerar relatórios.

### Administrador

Responsável principalmente por:

- Realizar login;
- Gerenciar usuários;
- Acessar funcionalidades administrativas.

### Diagrama de Casos de Uso

O diagrama de casos de uso apresenta o **BiblioTech – Sistema de Biblioteca** como limite do sistema.

À esquerda estão os atores **Leitor** e **Bibliotecário**, enquanto o **Administrador** aparece à direita.

Os atores estão conectados às funcionalidades que podem executar. O Bibliotecário concentra as operações relacionadas ao gerenciamento do acervo, leitores, empréstimos, devoluções e relatórios. O Leitor possui acesso principalmente às funcionalidades de consulta, enquanto o Administrador possui acesso às operações administrativas.

---

# 9. Arquitetura e Componentes

## 9.1 Interface Web

A interface web contará com:

- Tela de login;
- Tela inicial;
- Cadastro de livros;
- Cadastro de leitores;
- Empréstimos;
- Devoluções;
- Consultas;
- Relatórios.

### Tecnologias previstas

**HTML, CSS e JavaScript**, utilizando os recursos de templates do Django.

---

## 9.2 Django

O Django será responsável por:

- Receber as requisições;
- Direcionar as URLs;
- Executar as regras do sistema;
- Validar informações;
- Acessar o banco de dados;
- Controlar autenticação;
- Retornar as páginas e respostas.

---

## 9.3 Regras de Negócio

As principais áreas das regras de negócio serão:

- Gerenciamento de livros;
- Gerenciamento de leitores;
- Empréstimos;
- Devoluções;
- Disponibilidade;
- Relatórios.

---

## 9.4 Fluxo de Dados

O usuário acessa o BiblioTech por meio da interface web.

As requisições são encaminhadas pelo Django para as funcionalidades correspondentes.

Quando necessário, a aplicação consulta ou modifica os dados armazenados no banco de dados.

Para consultas disponibilizadas a outros sistemas, a aplicação utiliza a API REST própria.

Durante determinadas operações relacionadas aos livros, o sistema poderá realizar consultas à API externa e utilizar os dados obtidos em funcionalidades do BiblioTech.

---

# 10. API REST

A API REST será a interface para que outros sistemas possam consultar dados do BiblioTech.

A API deverá retornar informações em formato **JSON**.

Ao ser procurado um livro, por exemplo, a API poderá retornar:

- ID;
- Título;
- Autor;
- Disponibilidade.

Os principais recursos serão:

- Livros;
- Leitores;
- Empréstimos;
- Categorias.

---

## 10.1 Endpoints Previstos

| Recurso    | Método | Endpoint                    | Descrição                                             |
| ---------- | ------ | --------------------------- | ----------------------------------------------------- |
| Categoria  | GET    | `/api/v1/categorias/`       | Lista todas as categorias cadastradas.                |
| Categoria  | GET    | `/api/v1/categorias/{id}/`  | Consulta uma categoria específica.                    |
| Categoria  | POST   | `/api/v1/categorias/`       | Cadastra uma nova categoria.                          |
| Categoria  | PUT    | `/api/v1/categorias/{id}/`  | Atualiza uma categoria existente.                     |
| Categoria  | PATCH  | `/api/v1/categorias/{id}/`  | Atualiza parcialmente uma categoria.                  |
| Categoria  | DELETE | `/api/v1/categorias/{id}/`  | Exclui uma categoria.                                 |
| Livro      | GET    | `/api/v1/livros/`           | Lista os livros cadastrados.                          |
| Livro      | GET    | `/api/v1/livros/{id}/`      | Consulta um livro específico.                         |
| Livro      | POST   | `/api/v1/livros/`           | Cadastra um novo livro.                               |
| Livro      | PUT    | `/api/v1/livros/{id}/`      | Atualiza um livro existente.                          |
| Livro      | PATCH  | `/api/v1/livros/{id}/`      | Atualiza parcialmente um livro.                       |
| Livro      | DELETE | `/api/v1/livros/{id}/`      | Exclui um livro.                                      |
| Leitor     | GET    | `/api/v1/leitores/`         | Lista os leitores cadastrados.                        |
| Leitor     | GET    | `/api/v1/leitores/{id}/`    | Consulta um leitor específico.                        |
| Leitor     | POST   | `/api/v1/leitores/`         | Cadastra um novo leitor.                              |
| Leitor     | PUT    | `/api/v1/leitores/{id}/`    | Atualiza um leitor existente.                         |
| Leitor     | PATCH  | `/api/v1/leitores/{id}/`    | Atualiza parcialmente um leitor.                      |
| Leitor     | DELETE | `/api/v1/leitores/{id}/`    | Exclui um leitor.                                     |
| Empréstimo | GET    | `/api/v1/emprestimos/`      | Lista os empréstimos registrados.                     |
| Empréstimo | GET    | `/api/v1/emprestimos/{id}/` | Consulta um empréstimo específico.                    |
| Empréstimo | POST   | `/api/v1/emprestimos/`      | Registra um novo empréstimo.                          |
| Empréstimo | PATCH  | `/api/v1/emprestimos/{id}/` | Atualiza informações do empréstimo, como a devolução. |

---

## 10.2 Códigos HTTP

| Código HTTP | Nome                  | Descrição                                                        |
| ----------- | --------------------- | ---------------------------------------------------------------- |
| `200`       | OK                    | Requisição realizada com sucesso.                                |
| `201`       | Created               | Recurso criado com sucesso.                                      |
| `204`       | No Content            | Requisição realizada com sucesso, sem conteúdo para retornar.    |
| `400`       | Bad Request           | Requisição inválida ou dados enviados incorretamente.            |
| `401`       | Unauthorized          | Usuário não autenticado ou credenciais inválidas.                |
| `403`       | Forbidden             | Usuário autenticado, mas sem permissão para realizar a operação. |
| `404`       | Not Found             | Recurso solicitado não foi encontrado.                           |
| `500`       | Internal Server Error | Erro interno inesperado no servidor.                             |

---

## 10.3 Autenticação e Autorização

Os endpoints que modificam dados ou acessam informações restritas deverão exigir autenticação.

O sistema deverá verificar o perfil do usuário para determinar quais operações podem ser realizadas.

Por exemplo, somente usuários com perfil de **Bibliotecário** poderão cadastrar, alterar ou excluir livros e registrar empréstimos.

---

## 10.4 Tratamento de Erros

Em caso de erro, a API deverá retornar uma resposta JSON informando o problema.

Exemplo:

```json
{
  "erro": "Livro não encontrado.",
  "codigo": 404
}
```

A API deverá validar os dados recebidos antes de realizar alterações no banco de dados.

---

# 11. API Externa

A API externa escolhida para o BiblioTech será a **Google Books API**, disponibilizada pelo Google.

Ela será utilizada para consultar informações bibliográficas de livros e auxiliar o processo de cadastro do acervo.

## 11.1 Endpoint Externo Previsto

Para realizar pesquisas será utilizado:

```text
GET https://www.googleapis.com/books/v1/volumes?q={termo}
```

A API também permite consultas específicas por título, autor e ISBN utilizando os recursos de pesquisa disponibilizados pela própria API.

---

## 11.2 Dados Utilizados

O BiblioTech poderá utilizar principalmente:

- Título;
- Autores;
- Editora;
- Data de publicação;
- Categorias;
- Identificadores ISBN;
- Descrição;
- Imagem da capa, quando disponibilizada.

---

## 11.3 Fluxo da Integração

1. O bibliotecário acessa a opção de busca externa de livros.
2. O usuário informa o título, autor ou ISBN.
3. O BiblioTech envia uma requisição para a Google Books API.
4. A API externa processa a pesquisa.
5. A API retorna os resultados em JSON.
6. O BiblioTech interpreta os dados recebidos.
7. O sistema apresenta os resultados ao bibliotecário.
8. O bibliotecário seleciona o livro desejado.
9. Os dados disponíveis são utilizados para facilitar o preenchimento do cadastro.
10. O bibliotecário confirma o cadastro no BiblioTech.

---

# 12. Banco de Dados

O banco de dados será responsável por armazenar os dados do sistema.

Inicialmente teremos entidades como:

- Livro;
- Leitor;
- Usuário;
- Empréstimo;
- Categoria.

---

## 12.1 Tecnologias

| Componente     | Tecnologia             |
| -------------- | ---------------------- |
| Backend        | Python                 |
| Framework      | Django                 |
| API REST       | Django REST Framework  |
| Frontend       | HTML, CSS e JavaScript |
| Banco de dados | Banco relacional       |
| Versionamento  | Git + GitHub           |
| API externa    | API pública de livros  |
| Modelagem      | draw.io                |

---

## 12.2 Tabela Usuário

| Campo    | Tipo    | Chave  |
| -------- | ------- | ------ |
| `id`     | INT     | PK     |
| `nome`   | VARCHAR |        |
| `email`  | VARCHAR | UNIQUE |
| `senha`  | VARCHAR |        |
| `perfil` | VARCHAR |        |

---

## 12.3 Tabela Livro

| Campo            | Tipo    | Chave  |
| ---------------- | ------- | ------ |
| `id`             | INT     | PK     |
| `titulo`         | VARCHAR |        |
| `autor`          | VARCHAR |        |
| `isbn`           | VARCHAR | UNIQUE |
| `editora`        | VARCHAR |        |
| `ano_publicacao` | INT     |        |
| `categoria`      | VARCHAR |        |
| `quantidade`     | INT     |        |

---

## 12.4 Tabela Leitor

| Campo           | Tipo    | Chave  |
| --------------- | ------- | ------ |
| `id`            | INT     | PK     |
| `nome`          | VARCHAR |        |
| `cpf`           | VARCHAR | UNIQUE |
| `email`         | VARCHAR | UNIQUE |
| `telefone`      | VARCHAR |        |
| `data_cadastro` | DATE    |        |

---

## 12.5 Tabela Empréstimo

| Campo                     | Tipo    | Chave |
| ------------------------- | ------- | ----- |
| `id`                      | INT     | PK    |
| `livro_id`                | INT     | FK    |
| `leitor_id`               | INT     | FK    |
| `data_emprestimo`         | DATE    |       |
| `data_prevista_devolucao` | DATE    |       |
| `data_devolucao`          | DATE    | NULL  |
| `status`                  | VARCHAR |       |

---

## 12.6 Tabela Categoria

| Campo       | Tipo    | Chave  |
| ----------- | ------- | ------ |
| `id`        | INT     | PK     |
| `nome`      | VARCHAR | UNIQUE |
| `descricao` | VARCHAR |        |

---

# 13. Relacionamentos e DER

O Diagrama Entidade-Relacionamento apresenta cinco entidades principais:

- **Categoria**
- **Livro**
- **Empréstimo**
- **Leitor**
- **Usuário**

### Relacionamentos

**Categoria → Livro**

Uma categoria pode possuir vários livros. Cada livro está relacionado a uma categoria.

```text
Categoria (1) ───────── (N) Livro
```

**Livro → Empréstimo**

Um livro pode aparecer em vários empréstimos ao longo do tempo. Cada registro de empréstimo referencia um livro.

```text
Livro (1) ───────────── (N) Empréstimo
```

**Leitor → Empréstimo**

Um leitor pode realizar vários empréstimos. Cada empréstimo pertence a um leitor.

```text
Leitor (1) ──────────── (N) Empréstimo
```

A entidade **Usuário** representa os usuários responsáveis pelo acesso ao sistema e possui informações de nome, e-mail, senha e perfil.

---

# 14. Regras de Negócio

### Regra 1 — Livro Indisponível

Um livro não poderá ser emprestado quando não houver exemplar disponível.

### Regra 2 — Devolução

Quando um empréstimo for devolvido, `data_devolucao` será preenchida e o status passará para **Devolvido**.

### Regra 3 — Empréstimo Ativo

Um empréstimo ainda não devolvido terá:

```text
data_devolucao = null
```

### Regra 4 — ISBN

O ISBN deverá ser único quando informado.

### Regra 5 — E-mail

O e-mail do usuário/leitor deverá ser único.

---

# 15. Identidade Visual

| Elemento                   | Definição                                    |
| -------------------------- | -------------------------------------------- |
| Nome                       | BiblioTech                                   |
| Slogan                     | **A modernidade que abraça a tradição**      |
| Elemento gráfico principal | Livro aberto                                 |
| Estilo visual              | Moderno, elegante, minimalista e tecnológico |
| Tema da interface          | Dark Mode                                    |

---

## 15.1 Paleta de Cores

O amarelo pastel será utilizado principalmente na identidade visual e em elementos suaves da interface.

Já o amarelo mais intenso será utilizado em botões, ícones, menus selecionados e informações que necessitem de maior destaque.

| Utilização          | Cor              | Código    |
| ------------------- | ---------------- | --------- |
| Cor principal       | Amarelo pastel   | `#FFE8A3` |
| Cor secundária      | Azul acinzentado | `#475569` |
| Cor de fundo        | Preto            | `#000000` |
| Cor de destaque     | Amarelo          | `#FFC107` |
| Elementos e cartões | Cinza escuro     | `#1E1E1E` |
| Textos principais   | Branco           | `#FFFFFF` |

---

## 15.2 Tipografia

Para manter uma aparência moderna e uma boa legibilidade, serão utilizadas duas fontes principais:

- **Poppins:** títulos, menus, botões e elementos de destaque;
- **Inter:** textos, formulários, tabelas e demais informações da interface.

---

## 15.3 Logotipo

O logotipo do **BiblioTech** será composto pelo símbolo de um livro aberto, representando a leitura e o conhecimento, combinado com elementos gráficos modernos que representam a tecnologia.

O nome **BiblioTech** acompanhará o símbolo, utilizando branco e amarelo como cores predominantes.

O slogan:

**A modernidade que abraça a tradição**

poderá aparecer abaixo da marca em aplicações que possuam espaço suficiente.

---

## 15.4 Padrão da Interface

A interface seguirá um padrão visual consistente em todas as telas.

O fundo será predominantemente preto, enquanto cartões, tabelas e campos utilizarão diferentes tons de cinza escuro.

O amarelo será utilizado estrategicamente para destacar:

- Botões principais;
- Item selecionado no menu;
- Ícones importantes;
- Indicadores;
- Links e ações;
- Informações que necessitem da atenção do usuário.

A navegação principal será realizada através de um **menu lateral**, permitindo acesso rápido às funcionalidades do sistema.

---

# 16. Protótipo da Tela de Login

A tela de login será responsável pelo acesso dos usuários ao BiblioTech.

Ela deverá apresentar:

- Logotipo do BiblioTech;
- Slogan do sistema;
- Campo de e-mail;
- Campo de senha;
- Opção **“Lembrar de mim”**;
- Botão **“Entrar”**;
- Opção de recuperação de senha.

A proposta visual poderá utilizar uma imagem de biblioteca como elemento complementar, reforçando a relação entre tecnologia e tradição presente na identidade do projeto.

---

# 17. Protótipo do Dashboard

Após realizar o login, o usuário será direcionado ao **Dashboard**, que apresentará uma visão geral das principais informações do sistema.

O Dashboard deverá apresentar indicadores como:

- Total de livros;
- Total de leitores;
- Empréstimos ativos;
- Empréstimos atrasados;
- Livros mais emprestados;
- Empréstimos recentes.

O menu lateral permitirá acesso às áreas de:

- Início;
- Livros;
- Leitores;
- Empréstimos;
- Relatórios;
- Usuários.

---

# 18. Protótipo do Catálogo de Livros

A tela de catálogo será utilizada para consultar e administrar os livros cadastrados no BiblioTech.

Deverá possuir:

- Campo de pesquisa;
- Filtro por título;
- Filtro por autor;
- Filtro por ISBN;
- Filtro por categoria;
- Filtro por disponibilidade;
- Botão **“Cadastrar livro”**;
- Listagem dos livros;
- Indicação de disponibilidade;
- Opções para visualizar, editar e excluir registros.

Os resultados serão apresentados em formato de tabela, facilitando a consulta e administração do acervo.

---

# 19. Backlog do Produto

| Funcionalidade            | Descrição                                                     | Prioridade |
| ------------------------- | ------------------------------------------------------------- | ---------- |
| Login                     | Permitir a autenticação dos usuários no sistema.              | Alta       |
| Gerenciar usuários        | Cadastrar, consultar, alterar e excluir usuários.             | Média      |
| Gerenciar livros          | Cadastrar, consultar, alterar e excluir livros.               | Alta       |
| Pesquisar livros          | Pesquisar livros por título, autor, ISBN e categoria.         | Alta       |
| Consultar disponibilidade | Verificar se existem exemplares disponíveis para empréstimo.  | Alta       |
| Gerenciar categorias      | Cadastrar, consultar, alterar e excluir categorias de livros. | Média      |
| Gerenciar leitores        | Cadastrar, consultar, alterar e excluir leitores.             | Alta       |
| Registrar empréstimo      | Registrar o empréstimo de um livro para um leitor.            | Alta       |
| Registrar devolução       | Registrar a devolução de um livro emprestado.                 | Alta       |
| Consultar empréstimos     | Consultar empréstimos ativos, devolvidos e atrasados.         | Alta       |
| Histórico do leitor       | Consultar o histórico de empréstimos de cada leitor.          | Média      |
| Dashboard                 | Exibir indicadores gerais da biblioteca.                      | Média      |
| Gerar relatórios          | Gerar informações sobre livros, leitores e empréstimos.       | Média      |
| API REST                  | Disponibilizar recursos do sistema através de uma API REST.   | Alta       |
| Integração Google Books   | Consultar informações de livros através da API externa.       | Média      |
| Interface responsiva      | Adaptar a interface para computadores, tablets e celulares.   | Média      |
| Tratamento de erros       | Exibir mensagens adequadas e tratar erros do sistema.         | Alta       |
| Deploy                    | Publicar o BiblioTech em ambiente acessível pela internet.    | Alta       |

---

# 20. Etapas de Desenvolvimento

| Etapa                   | Atividades Principais                                                     |
| ----------------------- | ------------------------------------------------------------------------- |
| **1 – Preparação**      | Criar repositório, configurar Django, banco de dados e estrutura inicial. |
| **2 – Base do sistema** | Implementar autenticação, usuários, livros, categorias e leitores.        |
| **3 – Empréstimos**     | Implementar empréstimos, devoluções e regras de disponibilidade.          |
| **4 – API REST**        | Criar os endpoints e implementar autenticação e tratamento de erros.      |
| **5 – API Externa**     | Integrar a consulta de livros com a Google Books API.                     |
| **6 – Interface**       | Implementar login, dashboard, catálogo e gerenciamento de empréstimos.    |
| **7 – Testes**          | Realizar testes funcionais e corrigir problemas encontrados.              |
| **8 – Finalização**     | Realizar deploy, revisar documentação e preparar apresentação.            |

---
