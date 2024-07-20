document.addEventListener('DOMContentLoaded', () => {
    const botaoRodar = document.getElementById('botao-container');
    const botaoAuto = document.getElementById('auto');
    const telaRoleta = document.getElementById('tela-roleta');
    const slots = Array.from(telaRoleta.getElementsByClassName('slot'));
    const saldoElement = document.querySelector('.saldo span');
    const valorApostaElement = document.getElementById('valor-aposta');
    const resultadosElement = document.getElementById('resultados');
    const audioElement = document.getElementById('audio');

    let saldo = parseInt(saldoElement.textContent);
    let autoPlay = false;
    let autoPlayInterval = null;

    botaoRodar.addEventListener('click', () => {
        rodarRoleta();
    });

    botaoAuto.addEventListener('click', () => {
        autoPlay = !autoPlay;
        botaoAuto.textContent = autoPlay ? "STOP" : "AUTO";
        if (autoPlay) {
            autoPlayInterval = setInterval(rodarRoleta, 1000);
        } else {
            clearInterval(autoPlayInterval);
        }
    });

    function rodarRoleta() {
        const valorAposta = parseInt(valorApostaElement.value);
        if (isNaN(valorAposta) || valorAposta <= 0 || valorAposta > saldo) {
            alert('Valor de aposta inválido.');
            return;
        }

        fetch('/play_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ valorAposta: valorAposta })
        })
        .then(response => response.json())
        .then(data => {
            saldo -= valorAposta;
            updateSaldo();
            atualizarRoleta(data.slots);
            exibirResultados(data.verificacao);
            if (data.ganhou) {
                saldo += valorAposta * 10; // Multiplicador de ganho
                updateSaldo();
            }
            audioElement.play();
        })
        .catch(error => console.error('Erro:', error));
    }

    function atualizarRoleta(slotsData) {
        slots.forEach((slot, index) => {
            const rowIndex = Math.floor(index / 3);
            const colIndex = index % 3;
            slot.textContent = slotsData[rowIndex][colIndex];
            slot.classList.remove('win');
        });
    }

    function exibirResultados(verificacaoData) {
        resultadosElement.innerHTML = '';
        verificacaoData.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.display} ${item.value}`;
            resultadosElement.appendChild(li);
        });
    }

    function updateSaldo() {
        saldoElement.textContent = saldo;
        saldoElement.className = saldo >= 10 ? 'com_saldo' : 'sem_saldo';
    }
});
