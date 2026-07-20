# Hogwarts Album - API de Figurinhas ⚡🧙‍♂️

Este repositório contém a versão final do backend e a documentação do projeto **Hogwarts Album**, um álbum de figurinhas interativo e mágico inspirado no universo de Harry Potter. A aplicação integra uma API moderna em **FastAPI** (Python) com um frontend dinâmico.

---

## 🎯 Objetivo do Projeto

O objetivo do projeto é gerenciar e servir dinamicamente as informações e imagens das 40 figurinhas colecionáveis do álbum mágico de Hogwarts. A API permite que o frontend consulte quais figurinhas estão disponíveis e carregue as respectivas imagens de forma otimizada de acordo com o ID de cada personagem, criatura ou lenda do mundo bruxo.

---

## 📂 Estrutura de Arquivos e Funcionalidades

O projeto está dividido entre a API (Backend) e a Interface (Frontend).

### 🖥️ Backend (FastAPI)

Localizado no diretório do servidor (`Backend/`), é composto por:

1. **`main.py`**: O núcleo do servidor FastAPI. Suas principais funções são:
   * **Configuração de CORS**: Habilita o middleware de CORS (`CORSMiddleware`) permitindo que o frontend faça requisições à API de qualquer origem.
   * **Banco de Dados (Em Memória)**: Uma lista contendo as 40 figurinhas do álbum estruturadas com `id`, `nome`, `categoria` (as casas de Hogwarts, professores, criaturas, etc.) e o link para a imagem (`imagem_url`).
   * **Endpoint `GET /figurinhas`**: Retorna a lista completa de figurinhas colecionáveis cadastradas no sistema.
   * **Endpoint `GET /figurinhas/{id}/imagem`**: Rota que busca dinamicamente o arquivo de imagem dentro do diretório de figurinhas usando a biblioteca `glob` para encontrar o arquivo correto pelo prefixo (ex: `01[!0-9]*` para o ID 1). Se o ID não existir, retorna um erro `404 (Not Found)`.

2. **`figurinhas/`**: Pasta contendo os arquivos físicos das 40 imagens (como `01-harry-potter.jpg`, `02-alvo-dumbledore.jpg`, até `40-voce.jpg`).

---

### 🎨 Frontend (HTML/CSS/JavaScript)

Responsável por renderizar a interface visual do álbum com efeito 3D de virada de página:

1. **`index.html`**: Estrutura as páginas do álbum mágico, organizadas nas seguintes categorias (páginas):
   * **Membros de Grifinória** (Figurinhas 1 a 5)
   * **Membros de Sonserina** (Figurinhas 6 a 10)
   * **Corvinal** (Figurinhas 11 a 15)
   * **Lufa-Lufa** (Figurinhas 16 a 20)
   * **Professores e Funcionários** (Figurinhas 21 a 25)
   * **Criaturas Mágicas** (Figurinhas 26 a 30)
   * **Aliados** (Figurinhas 31 a 35)
   * **Lendas & Você** (Figurinhas 36 a 40)

2. **`app.js`**: Contém a lógica de interação:
   * Inicializa a biblioteca `St.PageFlip` para proporcionar a animação de folhear o livro físico.
   * Realiza a requisição `fetch` ao backend local (`http://localhost:8000/figurinhas`) ao carregar a página.
   * Mapeia as figurinhas retornadas e insere dinamicamente as imagens nos slots correspondentes (`#01` a `#40`).

3. **`style.css`**: Define a identidade visual mágica com fontes personalizadas, sombras, transições suaves e design adaptado para simular um livro real.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **FastAPI** (Framework web moderno e rápido)
* **Uvicorn** (Servidor ASGI para rodar a aplicação Python)
* **HTML5, CSS3 e JavaScript ES6**
* **St.PageFlip** (Biblioteca JS para simulação de páginas)

---

## 🚀 Como Executar o Projeto Localmente

### 1. Preparar o Backend

1. Certifique-se de ter o Python instalado.
2. Navegue até o diretório `Backend` e instale as dependências necessárias:
   ```bash
   pip install fastapi uvicorn
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn main:app --reload
   ```
   *O backend estará rodando no endereço: `http://localhost:8000`*

### 2. Abrir o Frontend

1. Com o backend rodando, abra o arquivo `index.html` em seu navegador de preferência.
2. O álbum fará a chamada automática para carregar as figurinhas da API e as colará nos respectivos espaços mágicos! ✨
