Casino Roleta

Este projeto é um jogo de roleta simples desenvolvido com Python (Flask) para o backend e HTML, CSS, e JavaScript para o frontend. O objetivo é criar uma roleta interativa onde os jogadores podem fazer apostas e girar a roleta para tentar ganhar.
Funcionalidades

    Interface de Usuário: Uma interface simples para girar a roleta e fazer apostas.
    Backend: Processa as apostas e simula o jogo da roleta.
    Resultados: Mostra os resultados do jogo e atualiza o saldo do jogador.

Estrutura do Projeto

O projeto é dividido nas seguintes partes:

    Backend (Flask)
    Frontend (HTML, CSS, JavaScript)
    Arquivos de Estilo e Scripts

1. Backend (Flask)

O backend é responsável por processar as apostas, simular o jogo e fornecer os dados necessários ao frontend.
Principais Arquivos

    app.py: Arquivo principal do Flask que define as rotas e a lógica do jogo.
    tabuleiro.py: Contém a lógica do jogo da roleta.
    logica_button.py: Manipula o estado dos botões e o saldo do jogador.

Como Executar

    Instale as dependências:
    
    pip install flask
    
Execute o servidor Flask:

    python app.py

    Acesse o aplicativo:

    Abra seu navegador e vá para http://127.0.0.1:5000/.

2. Frontend (HTML, CSS, JavaScript)

O frontend é responsável pela interface do usuário e pela interação com o backend.
Principais Arquivos

    templates/tabuleiro.html: Página HTML que exibe a interface do jogo.
    static/tabuleiro.css: Arquivo de estilo para a página HTML.
    static/tabuleiro.js: Script JavaScript para manipular a interação do usuário e atualizar a interface.

Estrutura do HTML

    Container Principal: Contém a barra superior, a tela da roleta e a seção lateral para mensagens.
    Barra Superior: Inclui botões para girar a roleta e selecionar o valor da aposta.
    Tela da Roleta: Mostra o resultado da roleta com a opção de destacar os slots vencedores.
    Seção Lateral: Exibe os resultados das apostas.

3. Arquivos de Estilo e Scripts

    tabuleiro.css: Define o estilo visual da roleta e outros elementos da interface.
    tabuleiro.js: Contém a lógica para girar a roleta, atualizar a interface e lidar com o estado automático.

Exemplo de Uso

    Escolha o valor da aposta no menu suspenso.
    Clique em "Girar Roleta" para iniciar o jogo.
    Veja os resultados e o saldo atualizado.

Rotas da API

    /: Página principal que carrega o jogo.
    /play_game: Rota POST que gira a roleta e retorna o resultado.
    /toggle-button: Rota POST que alterna o estado do botão AUTO.
    /play_game_auto: Rota POST que gira a roleta automaticamente se o estado do botão AUTO estiver ativado.

Exemplo de Resposta da API

{
    "slots": [
        [{"display": "A", "fill": true}, {"display": "B", "fill": false}, {"display": "C", "fill": false}],
        [{"display": "A", "fill": true}, {"display": "B", "fill": false}, {"display": "C", "fill": false}],
        [{"display": "A", "fill": true}, {"display": "B", "fill": false}, {"display": "C", "fill": false}]
    ],
    "verificacao": [{"display": "A", "value": "A"}],
    "ganhou": true,
    "saldo": 1010
}
Contribuindo

Se você quiser contribuir para este projeto, por favor, siga estas etapas:

    Faça um fork deste repositório.
    Crie uma branch para sua feature (git checkout -b minha-feature).
    Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
    Envie sua branch para o repositório (git push origin minha-feature).
    Crie um Pull Request.


  muito obrigado por ler <3
