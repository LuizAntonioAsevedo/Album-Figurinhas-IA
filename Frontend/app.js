const API_URL = "http://127.0.0.1:8001";

let figurinhas = [];

let paginaAtual = 1;

const figurinhasPorPagina = 5;

const totalPaginas = 7;

let animando = false;


/* ============================================================
   ELEMENTOS
   ============================================================ */

const capa =
    document.getElementById("capa");

const albumContainer =
    document.getElementById("album-container");

const album =
    document.getElementById("album");

const paginaEsquerda =
    document.getElementById("pagina-esquerda");

const paginaDireita =
    document.getElementById("pagina-direita");

const btnAnterior =
    document.getElementById("btn-anterior");

const btnProxima =
    document.getElementById("btn-proxima");

const indicador =
    document.getElementById("pagina-atual");


/* ============================================================
   CARREGAR FIGURINHAS
   ============================================================ */

async function carregarFigurinhas() {

    try {

        const resposta =
            await fetch(
                `${API_URL}/figurinhas`
            );

        if (!resposta.ok) {

            throw new Error(
                "Não foi possível carregar as figurinhas."
            );

        }

        figurinhas =
            await resposta.json();

        console.log(
            "Figurinhas carregadas:",
            figurinhas
        );

    } catch (erro) {

        console.error(
            "Erro:",
            erro
        );

    }

}


/* ============================================================
   CRIAR CARD DA FIGURINHA
   ============================================================ */

function criarFigurinha(figurinha) {

    const card =
        document.createElement(
            "div"
        );

    card.className =
        "figurinha";


    /* --------------------------------------------------------
       NÚMERO
       -------------------------------------------------------- */

    const numero =
        document.createElement(
            "div"
        );

    numero.className =
        "numero-figurinha";

    numero.textContent =
        String(
            figurinha.id
        ).padStart(
            2,
            "0"
        );


    /* --------------------------------------------------------
       IMAGEM
       -------------------------------------------------------- */

    const imagem =
        document.createElement(
            "img"
        );

    imagem.src =
        `${API_URL}/figurinhas/${figurinha.id}/imagem`;

    imagem.alt =
        figurinha.nome;

    imagem.onerror =
        function () {

            this.style.display =
                "none";

            card.classList.add(
                "sem-imagem"
            );

        };


    /* --------------------------------------------------------
       NOME
       -------------------------------------------------------- */

    const nome =
        document.createElement(
            "h3"
        );

    nome.textContent =
        figurinha.nome;


    /* --------------------------------------------------------
       CATEGORIA
       -------------------------------------------------------- */

    const categoria =
        document.createElement(
            "p"
        );

    categoria.textContent =
        figurinha.categoria;


    /* --------------------------------------------------------
       MONTAR CARD
       -------------------------------------------------------- */

    card.appendChild(
        numero
    );

    card.appendChild(
        imagem
    );

    card.appendChild(
        nome
    );

    card.appendChild(
        categoria
    );

    return card;

}


/* ============================================================
   CRIAR ESPAÇO DE FIGURINHA
   ============================================================ */

function criarEspacoVazio(numero) {

    const card =
        document.createElement(
            "div"
        );

    card.className =
        "figurinha sem-imagem";


    const numeroElemento =
        document.createElement(
            "div"
        );

    numeroElemento.className =
        "numero-figurinha";

    numeroElemento.textContent =
        String(
            numero
        ).padStart(
            2,
            "0"
        );


    const nome =
        document.createElement(
            "h3"
        );

    nome.textContent =
        "Aguardando figurinha";


    const categoria =
        document.createElement(
            "p"
        );

    categoria.textContent =
        "Espaço disponível";


    card.appendChild(
        numeroElemento
    );

    card.appendChild(
        nome
    );

    card.appendChild(
        categoria
    );

    return card;

}


/* ============================================================
   CRIAR PÁGINA
   ============================================================ */

function criarPagina(numeroPagina) {

    const pagina =
        document.createElement(
            "div"
        );

    pagina.className =
        "pagina";


    /* --------------------------------------------------------
       PÁGINA FINAL
       -------------------------------------------------------- */

    if (
        numeroPagina === totalPaginas
    ) {

        pagina.innerHTML = `

            <div class="pagina-vazia">

                <div class="estrela">
                    ★
                </div>

                <h3>
                    Página Final
                </h3>

                <p>
                    Espaço reservado para futuras figurinhas.
                </p>

            </div>

        `;

        return pagina;

    }


    /* --------------------------------------------------------
       TÍTULO
       -------------------------------------------------------- */

    const titulo =
        document.createElement(
            "div"
        );

    titulo.className =
        "titulo-pagina";

    titulo.textContent =
        `Página ${numeroPagina}`;

    pagina.appendChild(
        titulo
    );


    /* --------------------------------------------------------
       ÍNDICES
       -------------------------------------------------------- */

    const inicio =
        (numeroPagina - 1)
        * figurinhasPorPagina;

    const fim =
        inicio
        + figurinhasPorPagina;


    /* --------------------------------------------------------
       FIGURINHAS
       -------------------------------------------------------- */

    for (
        let i = inicio;
        i < fim;
        i++
    ) {

        const figurinha =
            figurinhas[i];

        if (figurinha) {

            pagina.appendChild(
                criarFigurinha(
                    figurinha
                )
            );

        } else {

            /*
             * Mantém o espaço reservado
             * para uma futura figurinha.
             */

            pagina.appendChild(
                criarEspacoVazio(
                    i + 1
                )
            );

        }

    }

    return pagina;

}


/* ============================================================
   RENDERIZAR ÁLBUM
   ============================================================ */

function renderizarAlbum() {

    paginaEsquerda.innerHTML = "";

    paginaDireita.innerHTML = "";


    const esquerda =
        criarPagina(
            paginaAtual
        );

    const direita =
        criarPagina(
            paginaAtual + 1
        );


    paginaEsquerda.innerHTML =
        esquerda.innerHTML;

    paginaDireita.innerHTML =
        direita.innerHTML;


    atualizarControles();

}


/* ============================================================
   ATUALIZAR CONTROLES
   ============================================================ */

function atualizarControles() {

    const paginaFinal =
        Math.min(
            paginaAtual + 1,
            totalPaginas
        );


    indicador.textContent =
        `Páginas ${paginaAtual}–${paginaFinal} de ${totalPaginas}`;


    btnAnterior.disabled =
        paginaAtual === 1;


    if (
        paginaAtual === totalPaginas
    ) {

        btnProxima.textContent =
            "Fechar álbum";

        btnProxima.disabled =
            false;

    } else {

        btnProxima.textContent =
            "Próxima ▶";

        btnProxima.disabled =
            false;

    }

}


/* ============================================================
   CENTRALIZAR ÁLBUM
   ============================================================ */

function centralizarAlbum() {

    setTimeout(
        () => {

            albumContainer.scrollIntoView({
                behavior: "smooth",
                block: "center",
                inline: "center"
            });

        },
        500
    );

}


/* ============================================================
   ABRIR ÁLBUM
   ============================================================ */

async function abrirAlbum() {

    if (
        capa.classList.contains("abrindo")
    ) {

        return;

    }


    await carregarFigurinhas();


    paginaAtual = 1;


    renderizarAlbum();


    capa.classList.remove(
        "fechando"
    );

    capa.classList.add(
        "abrindo"
    );


    setTimeout(
        () => {

            albumContainer.classList.remove(
                "fechado",
                "fechando"
            );

            albumContainer.classList.add(
                "aberto"
            );


            centralizarAlbum();

        },
        350
    );

}


/* ============================================================
   FECHAR ÁLBUM
   ============================================================ */

function fecharAlbum() {

    if (animando) {
        return;
    }


    animando = true;


    albumContainer.classList.remove(
        "aberto"
    );

    albumContainer.classList.add(
        "fechando"
    );


    setTimeout(
        () => {

            albumContainer.classList.remove(
                "fechando"
            );

            albumContainer.classList.add(
                "fechado"
            );


            paginaAtual = 1;


            capa.classList.remove(
                "abrindo"
            );

            capa.classList.add(
                "fechando"
            );


            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });


            setTimeout(
                () => {

                    capa.classList.remove(
                        "fechando"
                    );

                    animando = false;

                },
                100
            );

        },
        700
    );

}


/* ============================================================
   TROCAR PÁGINAS
   ============================================================ */

function trocarAbertura(direcao) {

    if (animando) {
        return;
    }


    /* --------------------------------------------------------
       FECHAR ÁLBUM
       -------------------------------------------------------- */

    if (
        direcao === "proxima" &&
        paginaAtual === totalPaginas
    ) {

        fecharAlbum();

        return;

    }


    /* --------------------------------------------------------
       PRÓXIMA
       -------------------------------------------------------- */

    if (
        direcao === "proxima"
    ) {

        if (
            paginaAtual + 2 >
            totalPaginas
        ) {

            return;

        }

    }


    /* --------------------------------------------------------
       ANTERIOR
       -------------------------------------------------------- */

    if (
        direcao === "anterior"
    ) {

        if (
            paginaAtual - 2 <
            1
        ) {

            return;

        }

    }


    animando = true;


    const classe =
        direcao === "proxima"
            ? "virando-proxima"
            : "virando-anterior";


    album.classList.remove(
        "virando-proxima",
        "virando-anterior"
    );


    void album.offsetWidth;


    album.classList.add(
        classe
    );


    setTimeout(
        () => {

            if (
                direcao === "proxima"
            ) {

                paginaAtual += 2;

            } else {

                paginaAtual -= 2;

            }


            renderizarAlbum();

        },
        425
    );


    setTimeout(
        () => {

            album.classList.remove(
                "virando-proxima",
                "virando-anterior"
            );

            animando = false;

        },
        850
    );

}


/* ============================================================
   EVENTOS
   ============================================================ */

capa.addEventListener(
    "click",
    abrirAlbum
);


btnProxima.addEventListener(
    "click",
    () => {

        trocarAbertura(
            "proxima"
        );

    }
);


btnAnterior.addEventListener(
    "click",
    () => {

        trocarAbertura(
            "anterior"
        );

    }
);


/* ============================================================
   INICIALIZAÇÃO
   ============================================================ */

renderizarAlbum();