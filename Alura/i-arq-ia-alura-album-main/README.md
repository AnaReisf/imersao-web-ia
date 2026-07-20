# 🏆 Alura Album - Copa do Mundo Tech

O **Alura Album** é um tributo interativo à história e evolução da tecnologia e do desenvolvimento de software. Ele foi estruturado no formato de um álbum de figurinhas virtual e interativo, celebrando as mentes mais brilhantes nacionais e internacionais da Inteligência Artificial, Linguagens de Programação, Bancos de Dados, Sistemas Operacionais e Educadores de Tecnologia no Brasil.

---

## 🎯 Objetivo do Projeto
O objetivo deste projeto é proporcionar uma experiência rica de usuário (UX) e praticar a integração entre um frontend moderno e uma API backend (construída com FastAPI). O projeto combina:
*   Animações de virada de página snappier e fluidas.
*   Efeitos sonoros gerados dinamicamente via código.
*   Consumo de dados de uma API externa para preencher dinamicamente as figurinhas do álbum.

---

## 📁 Estrutura de Arquivos e Suas Funcionalidades

O projeto possui três arquivos frontend principais:

### 1. 📄 [index.html](index.html)
Define a estrutura semântica do álbum de figurinhas.
*   **Capa e Contracapa**: Páginas duras com efeitos visuais futuristas e estilizados.
*   **Seções/Páginas Temáticas**:
    *   **Páginas 1 (IA)**: Pioneiros da Inteligência Artificial (ex: Alan Turing, Geoffrey Hinton, Sam Altman).
    *   **Página 2 (Python)**: Arquitetos da Simplicidade (ex: Guido van Rossum, Tim Peters).
    *   **Página 3 (Banco de Dados)**: Criadores de tecnologias de persistência (ex: Edgar F. Codd, Salvatore Sanfilippo).
    *   **Página 4 (Sistemas Operacionais)**: Desenvolvedores de OS e sistemas base (ex: Linus Torvalds, Dennis Ritchie).
    *   **Páginas 5 e 6 (Brasil)**: Celebridades e educadores tech brasileiros (ex: Paulo e Guilherme Silveira, Rafaela Ballerini, Gustavo Guanabara, Vinicius Neves, etc.) e um espaço reservado especial para o usuário.
*   **Dependências**: Carrega a biblioteca de transição de páginas `St.PageFlip` a partir de uma CDN.

### 2. 🎨 [style.css](style.css)
Responsável por toda a estilização visual, atmosfera cyberpunk/escura e animações interativas do álbum:
*   **Tipografia**: Utiliza as fontes modernas *Inter* e *Outfit* do Google Fonts.
*   **Design de Interface (UI)**: Cores vibrantes (neon/magenta), sombras realistas para simular a profundidade do livro e layouts organizados em grade (*CSS Grid*) para os slots das figurinhas.
*   **Efeitos Visuais**: Efeitos hover nos slots de figurinha e efeitos de glitch na capa.

### 3. ⚙️ [app.js](app.js)
Contém toda a lógica e interatividade da aplicação:
*   **Integração com API Backend**: Busca assincronamente (`fetch`) as informações e imagens das figurinhas a partir do endpoint `/figurinhas` (configurado em `http://localhost:8000`). Preenche automaticamente cada slot com a figurinha correspondente se a API estiver online.
*   **Gerenciamento do PageFlip**: Configura e inicializa a biblioteca `St.PageFlip`, gerenciando dimensões, transições de dobra de página e os gestos manuais personalizados de arraste.
*   **Áudio Sintetizado (Web Audio API)**: Cria de forma dinâmica um efeito sonoro de virada de página de papel real (fricção e deslocamento de ar), misturando ruído branco e sweeps de frequência de forma a não depender de arquivos de áudio externos.
*   **Controles de Navegação**: Gerencia os botões de navegação lateral (Próximo/Anterior) e as teclas de seta no teclado (`ArrowLeft` e `ArrowRight`).

---

## 🛠️ Como Executar e Integrar

1.  **Frontend**:
    *   Abra o arquivo `index.html` diretamente no seu navegador ou use uma extensão de servidor local (como *Live Server* no VS Code).
2.  **Backend (Conexão)**:
    *   Por padrão, o arquivo `app.js` tenta buscar os dados na URL `http://localhost:8000`. 
    *   Certifique-se de que a API (FastAPI) do backend correspondente esteja em execução. Para iniciar o backend:
        ```bash
        cd backend/dia-3
        uvicorn main:app --reload
        ```
