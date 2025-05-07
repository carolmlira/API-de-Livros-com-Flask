# API-de-Livros-com-Flask

Este é um projeto simples de API REST feita com Flask que permite gerenciar uma coleção de livros. É possível visualizar, adicionar, editar e excluir livros a partir de requisições HTTP.

🚀 Tecnologias Utilizadas
Python 3

Flask

📦 Funcionalidades da API
A API trabalha com uma lista de livros no formato JSON. Cada livro possui:

json
Copiar
Editar
{
  "id": 1,
  "titulo": "Exemplo de Título",
  "autor": "Nome do Autor"
}
🔍 Ver todos os livros
Rota: GET /livros

Resposta: Lista com todos os livros.

🔎 Ver um livro pelo ID
Rota: GET /livros/<id>

Resposta: Um único livro com o ID correspondente.

Exemplo: /livros/1

✍️ Editar um livro
Rota: PUT /livros/<id>

Corpo (JSON):

json
Copiar
Editar
{
  "titulo": "Novo Título",
  "autor": "Novo Autor"
}
➕ Adicionar um novo livro
Rota: POST /livros/<id>

Corpo (JSON):

json
Copiar
Editar
{
  "id": 4,
  "titulo": "Novo Livro",
  "autor": "Novo Autor"
}
❌ Deletar um livro
Rota: DELETE /livros/<id>

Resposta: Lista atualizada sem o livro excluído.

▶️ Como executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/api-livros-flask.git
cd api-livros-flask
Instale as dependências:

bash
Copiar
Editar
pip install flask
Execute o projeto:

bash
Copiar
Editar
python nome_do_arquivo.py
Acesse a API em:

bash
Copiar
Editar
http://localhost:5000/livros
⚠️ Observações
A base de dados é apenas uma lista em memória; ao reiniciar a aplicação, os dados são resetados.

O endpoint de POST poderia ser melhor implementado para aceitar apenas /livros, sem a necessidade de <id> na URL.
