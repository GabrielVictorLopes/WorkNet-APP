import flet as ft
from datetime import datetime, timedelta
from flet import (
    Page,
    ElevatedButton,
    Column,
    Row,
    Container,
    Image,
    Text,
    IconButton,
    TextField,
    colors,
    icons,
)


def tela_login(page, navegar_para_home):
    # Cabeçalho 
    header = Container(
        bgcolor=ft.colors.BLUE,
        height=66,
        content=Row(
            [
                Image(
                    src="img/logo_worknet.png",  # URL da imagem
                    width=140,  # Largura da imagem
                    height=140,  # Altura da imagem
                    fit=ft.ImageFit.CONTAIN,  # Ajusta o tamanho da imagem
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    botao_usu = ElevatedButton(
        height=115,
        width=115,
        bgcolor="#00b5ff",
        content=Container(
            content=Image(
                src="img/icone_usuario.png",
                width=87,
                height=87,
                fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.center,
        ),
        on_click=lambda e: print("Você é um usuário!"),
    )
    botao_prof = ElevatedButton(
        height=115,
        width=115,
        bgcolor="#00b5ff",
        content=Container(
            content=Image(
                src="img/icone_prof.png",
                width=87,
                height=87,
                fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.center,
        ),
        on_click=lambda e: print("Você é um profissional!"),
    )

    # Botão de login
    botao_login = ElevatedButton(
        height=55,
        width=130,
        bgcolor="#00b5ff",
        style=ft.ButtonStyle(
            side=ft.BorderSide(color="black", width=3),
        ),
        content=Text(
            "LOGIN",
            font_family="Quicksand",
            color="black",
            size=17,
        ),
        on_click=lambda e: navegar_para_home(),  # Chama a função para ir à tela Home
    )

    # Campos de texto login
    campos_texto = Column(
        [
            TextField(label="NOME", border="underline",color=ft.colors.BLACK),
            TextField(label="E-MAIL", border="underline",color=ft.colors.BLACK),
            TextField(label="TELEFONE", border="underline",color=ft.colors.BLACK),
            TextField(label="CPF", border="underline",color=ft.colors.BLACK),
            TextField(
                label="CRIE SUA SENHA",
                border="underline",
                password=True,
                can_reveal_password=True,
                color=ft.colors.BLACK,
            ),
        ],
        spacing=10,
    )

    # Layout da tela 
    return Column(
        [
            header,
            Row([botao_usu, botao_prof], alignment=ft.MainAxisAlignment.CENTER, spacing=40),
            campos_texto,
            Row([botao_login], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )


def tela_home(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens):
    # Cabeçalho 
    header = Container(
        bgcolor=ft.colors.BLUE,
        height=66,
        content=Row(
            [
                Image(
                    src="img/logo_worknet.png",
                    width=140,
                    height=140,
                    fit=ft.ImageFit.CONTAIN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
#carrossel
    destaques_conteudos = [
        {
            "imagem": "img/Flavin.jpeg",
            "texto": "Hoje finalizamos a realização de um trabalho feito com muita dedicação e esforço.",
        },
        {
            "imagem": "img/Costureira.jpeg",
            "texto": "Terminei um grande trabalho hoje, após 10 dias de luta. O cliente ficou satisfeito.",
        },
        {
            "imagem": "img/homem.jpeg",
            "texto": "Realizei a criação de um site para o nosso querido cliente.",
        },
    ]

    carrossel_index = 0

    #  atualizar o carrossel
    def atualizar_carrossel():
        img_container.content = Image(
            src=destaques_conteudos[carrossel_index]["imagem"],
            width=150,
            height=150,
            fit="cover",
        )
        texto_container.content = Text(
            destaques_conteudos[carrossel_index]["texto"],
            size=15,
            color=colors.BLACK87,
            weight="bold",
            max_lines=3,
            overflow=ft.TextOverflow.ELLIPSIS,
        )
        page.update()

    #  alterar o índice do carrossel
    def alterar_indice(e):
        nonlocal carrossel_index
        if e.control.icon == icons.CHEVRON_LEFT:
            carrossel_index = (carrossel_index - 1) % len(destaques_conteudos)
        elif e.control.icon == icons.CHEVRON_RIGHT:
            carrossel_index = (carrossel_index + 1) % len(destaques_conteudos)
        atualizar_carrossel()

    # Containers para imagem e texto do carrossel
    img_container = Container(
        content=Image(
            src=destaques_conteudos[0]["imagem"],
            width=150,
            height=150,
            fit="cover",
        ),
        width=100,
        height=100,
        border_radius=100,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=colors.BLACK26),
    )

    texto_container = Container(
        content=Text(
            destaques_conteudos[0]["texto"],
            size=15,
            color=colors.BLACK87,
            weight="bold",
            max_lines=3,
            overflow=ft.TextOverflow.ELLIPSIS,
        ),
        width=250,
    )

    # Sessão "Destaques"
    destaques = Column(
        [
            Row(
                [Text("DESTAQUES", size=21, weight="bold", color=colors.BLACK)],
                alignment="center",
            ),
            Column(
                [
                    Row(
                        [img_container, texto_container],
                        alignment="start",
                        spacing=10,
                    ),
                    Row(
                        [
                            IconButton(
                                icon=icons.CHEVRON_LEFT,
                                icon_color=colors.BLACK,
                                on_click=alterar_indice,
                            ),
                            IconButton(
                                icon=icons.CHEVRON_RIGHT,
                                icon_color=colors.BLACK,
                                on_click=alterar_indice,
                            ),
                        ],
                        alignment="center",
                    ),
                ],
                alignment="center",
            ),
        ],
        spacing=20,
    )

    # Função para criar os "Melhores Avaliados"
    def criar_box(nome, subtitulo, avatar_caminho, estrelas):
        return Container(
            margin=ft.margin.symmetric(vertical=10),
            padding=5,
            bgcolor=colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=colors.BLACK),
            content=Row(
                [
                    Container(
                        content=Image(
                            src=avatar_caminho,
                            width=40,
                            height=40,
                            fit="cover",
                        ),
                        border_radius=25,
                        width=50,
                        height=50,
                        clip_behavior="antiAliasWithSaveLayer",
                    ),
                    Column(
                        [
                            Text(nome, size=13, weight="bold", color=colors.BLACK87),
                            Text(subtitulo, size=10, color=colors.BLACK87),
                        ],
                        alignment="start",
                        spacing=2,
                    ),
                    Text(f"⭐ {estrelas}", size=12, weight="bold", color=colors.BLACK87),
                ],
                alignment="spaceBetween",
            ),
        )

    # Sessão "Melhores Avaliados"
    melhores_avaliados = Column(
        [
            Row(
                [Text("MELHORES AVALIADOS", size=18, weight="bold", color=colors.BLACK)],
                alignment="center",
            ),
            criar_box("PRISCILLA SOARES", "- COSTUREIRA", "img/Costureira2.jpeg", "5"),
            criar_box("GÉRSON FABIANO", "- PEDREIRO", "img/Predeiro.jpeg", "4.8"),
        ],
        alignment="center",
    )

    # Rodapé 
    rodape = Container(
        bgcolor=colors.WHITE,
        height=60,
        content=Row(
            [
                IconButton(icon=icons.HOME, icon_color=colors.BLACK,on_click=lambda _: navegar_para_home()),
                IconButton(icon=icons.SEARCH, icon_color=colors.BLACK,on_click=lambda _: mudar_para_search()),
                IconButton(icon=icons.ADD,icon_color=colors.BLACK,on_click=lambda _: mudar_para_criar_demanda()),
                IconButton(icon=icons.PERSON, icon_color=colors.BLACK,on_click=lambda _: mudar_para_user()),
                IconButton(icon=icons.CHAT, icon_color=colors.BLACK,on_click=lambda _: mudar_para_mensagens()),
            ],
            alignment="spaceAround",
        ),
    )

    # Layout da tela Home
    return Column(
        [
            header,
            Container(content=destaques, margin=10),
            Container(content=melhores_avaliados, margin=10),
            ft.Container(expand=True),
            Container(content=rodape, margin=10),
        ],
    )


def criar_tela_demanda(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens):
    page.title = "Adicione Sua Urgência"
    page.bgcolor = "white"
    page.window.width = 380
    page.window.height = 710
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 5
    page.scroll = ft.ScrollMode.AUTO

    # Variáveis para armazenar os dados
    ramo_profissional = ft.TextField(hint_text="ESCREVA AQUI...", border_color="black", border="underline",color=ft.colors.BLACK)
    especialidade = ft.TextField(hint_text="ESCREVA AQUI...", border_color="black", border="underline",color=ft.colors.BLACK)
    descricao = ft.TextField(hint_text="ESCREVA AQUI...", border_color="black", border="underline",color=ft.colors.BLACK)
    min_price = ft.TextField(hint_text="MÍN...", width=80, bgcolor="white",color=ft.colors.BLACK)
    max_price = ft.TextField(hint_text="MÁX...", width=80, bgcolor="white",color=ft.colors.BLACK)

    # Data inicial
    today = datetime.today()
    selected_date = today
    current_year = today.year
    current_month = today.month
    

    # Função para gerar os dias do calendário
    def generate_calendar(year, month):
        first_day = datetime(year, month, 1)
        start_day = first_day - timedelta(days=first_day.weekday() + 1)
        days = []
        for i in range(42):
            day = start_day + timedelta(days=i)
            days.append(day)
        return days

    # Função para atualizar o calendário
    def update_calendar(year, month):
        nonlocal current_year, current_month
        current_year, current_month = year, month
        days = generate_calendar(year, month)
        calendar_days.controls.clear()
        for day in days:
            is_selected = day == selected_date
            day_container = ft.Container(
                content=ft.Text(
                    str(day.day),
                    color="gray" if day.month != month else "black",
                    weight=ft.FontWeight.BOLD if is_selected else ft.FontWeight.NORMAL,
                ),
                bgcolor="blue" if is_selected else None,
                border_radius=50 if is_selected else None,
                alignment=ft.alignment.center,
                padding=5,
                on_click=lambda e, day=day: select_date(day)
            )
            calendar_days.controls.append(day_container)
        calendar_title.value = f"{datetime(year, month, 1):%B %Y}"
        page.update()

    # Função para selecionar uma data
    def select_date(day):
        nonlocal selected_date
        selected_date = day
        update_calendar(current_year, current_month)

    def enviar_dados(e):
        dados = {
            "Ramo Profissional": ramo_profissional.value,
            "Especialidade": especialidade.value,
            "Prazo para Entrega": selected_date.strftime("%d/%m/%Y"),
            "Margem de Preço": f"{min_price.value} - {max_price.value}",
            "Descrição": descricao.value
        }

        # Exibir os dados no console (ou realizar outro processamento)
        print("Dados do Formulário:")
        for campo, valor in dados.items():
            print(f"{campo}: {valor}")

        # Mostrar uma mensagem na interface
        resultado.value = "Formulário enviado com sucesso!"
        resultado.color = "green"

        page.update()

    # Controles do calendário
    calendar_title = ft.Text(f"{today:%B %Y}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
    calendar_days = ft.GridView(expand=1, max_extent=45, child_aspect_ratio=1)

    # Gerar o calendário inicial
    update_calendar(current_year, current_month)

    # Mensagem de resultado
    resultado = ft.Text("", size=16)

    header = Container(
        bgcolor=ft.colors.BLUE,
        height=66,
        content=Row(
            [
                Image(
                    src="img/logo_worknet.png",
                    width=140,
                    height=140,
                    fit=ft.ImageFit.CONTAIN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Contêiner para o calendário com fundo branco
    calendario_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CHEVRON_LEFT,
                            on_click=lambda _: update_calendar(current_year, current_month - 1 if current_month > 1 else 12),
                        ),
                        calendar_title,
                        ft.IconButton(
                            icon=ft.icons.CHEVRON_RIGHT,
                            on_click=lambda _: update_calendar(current_year, current_month + 1 if current_month < 12 else 1),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                calendar_days,
            ],
            spacing=5,
        ),
        padding=10,
        border_radius=10,
        bgcolor="white",  # Fundo branco do calendário
        shadow=ft.BoxShadow(blur_radius=5, spread_radius=2, color="gray"),
    )

    # Campos do formulário
    form_fields = ft.Column(
        controls=[
            ft.Text("ADICIONE SUA URGÊNCIA", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.Text("RAMO PROFISSIONAL", size=16, weight=ft.FontWeight.BOLD, color="black"),
            ramo_profissional,
            ft.Text("ESPECIALIDADE", size=16, weight=ft.FontWeight.BOLD, color="black"),
            especialidade,
            ft.Text("PRAZO PARA ENTREGA", size=16, weight=ft.FontWeight.BOLD, color="black"),
            calendario_container,  # Adicionando o calendário com o fundo branco
            ft.Text("MARGEM DE PREÇO", size=16, weight=ft.FontWeight.BOLD, color="black"),
            ft.Row(
                controls=[
                    min_price,
                    ft.Text("À", size=16),
                    max_price,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("DESCRIÇÃO", size=16, weight=ft.FontWeight.BOLD, color="black"),
            descricao,
            ft.ElevatedButton("Enviar", on_click=enviar_dados), 
             # Botão de envio
            resultado,  # Mensagem de resultado
        ],
        spacing=8,
    )
    # Rodapé 
    rodape = Container(
        bgcolor=colors.WHITE,
        height=60,
        content=Row(
            [
                IconButton(icon=icons.HOME, icon_color=colors.BLACK,on_click=lambda _: navegar_para_home()),
                IconButton(icon=icons.SEARCH, icon_color=colors.BLACK,on_click=lambda _: mudar_para_search()),
                IconButton(icon=icons.ADD,icon_color=colors.BLACK,on_click=lambda _: mudar_para_criar_demanda()),
                IconButton(icon=icons.PERSON, icon_color=colors.BLACK,on_click=lambda _: mudar_para_user()),
                IconButton(icon=icons.CHAT, icon_color=colors.BLACK,on_click=lambda _: mudar_para_mensagens()),
            ],
            alignment="spaceAround",
        ),
    )

    # Layout da tela Home
    return Column(
        [
            Container(content=header, margin=10),
            Container(content=form_fields, margin=10),
            Container(content=rodape),

        ],
    )


def user(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens):
    page.title = "Interface com Flet"
    page.padding = 0
    page.bgcolor = colors.WHITE

    # Configuração do tamanho da página
    page.window.width = 380
    page.window.height = 710

    # Variável para rastrear aba ativa
    aba_ativa = "HOME"  # Aba inicial

    # Função para alterar aba ativa
    def atualizar_aba_ativa(e):
        nonlocal aba_ativa
        aba_ativa = e.control.icon
        rodape.update()

    # Cabeçalho azul com o "W"
    header = Container(
        bgcolor=colors.BLUE,
        height=60,
        content=Row(
            [
                Text("W", size=32, weight="bold", color=colors.BLACK),
            ],
            alignment="center",
        ),
    )
    
    # Novo contêiner com o texto "PERFIL"
    perfil_texto = Container(
        content=Text("PERFIL", size=24, weight="bold", color=colors.BLACK),
        alignment=ft.alignment.top_left,
        padding=ft.padding.only(top=6, left=12, bottom=6),
    )
    
    # Imagem de perfil redonda
    imagem_perfil = Container(
        content=Image(
            src="img/perfil.png",
            width=100,
            height=100,
            fit=ft.ImageFit.COVER,
            border_radius=(50),
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=12),
    )

    texto_usuario = Container(
        content=Text("usuário 1", size=16, color=colors.BLACK),
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=6),
    )
    
    # Texto "@USUÁRIO01" abaixo de "usuário 1"
    texto_usuario_handle = Container(
        content=Text("@USUÁRIO01", size=14, color=colors.GREY),
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=4),
    )

    # Novo conteúdo adicionado (navegação e cartão)
    nav = Row(
        controls=[
            Text("URGENCIAS", size=16, weight="bold", color=colors.BLACK),
            Text("AVALIAÇÕES", size=16, weight="bold", color=colors.GREY),
        ],
        alignment="spaceBetween",
        spacing=20,
    )

    card = Container(
        content=Row(
            controls=[
                # Imagem do perfil
                Container(
                    content=Image(
                        src="img/perfil.png",
                        width=50,
                        height=50,
                        border_radius=(25),
                    ),
                    padding=ft.padding.only(right=20),
                ),
                # Conteúdo do cartão
                Column(
                    controls=[
                        Text("@USUARIO1", size=14, weight="bold", color=colors.BLACK),
                        Text(
                            "- Preciso de um designer especializado em camisa de esporte, "
                            "tenho uma escolinha de futebol, e gostaria de um profissional "
                            "que seja rápido e que faça desenhos bonitos.",
                            size=14,
                            color=colors.BLACK,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ],
                    expand=True,
                    spacing=5,
                ),
                # Footer do cartão
                Text("Respondida ✔", size=14, weight="bold", color=colors.BLACK),
            ],
            alignment="start",
        ),
        padding=20,
        bgcolor=colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=colors.BLACK12,
            offset=ft.Offset(0, 4),
        ),
    )

    # Rodapé com abas clicáveis
    rodape = Container(
        bgcolor=colors.WHITE,
        height=60,
        content=Row(
            [
                IconButton(icon=icons.HOME, icon_color=colors.BLACK,on_click=lambda _: navegar_para_home()),
                IconButton(icon=icons.SEARCH, icon_color=colors.BLACK,on_click=lambda _: mudar_para_search()),
                IconButton(icon=icons.ADD,icon_color=colors.BLACK,on_click=lambda _: mudar_para_criar_demanda()),
                IconButton(icon=icons.PERSON, icon_color=colors.BLACK,on_click=lambda _: mudar_para_user()),
                IconButton(icon=icons.CHAT, icon_color=colors.BLACK,on_click=lambda _: mudar_para_mensagens()),
            ],
            alignment="spaceAround",
        ),
    )

    # Adicionando todos os elementos na página usando Column

    return Column(
        [
            Container(content=header, margin=10),
            Container(content=perfil_texto, margin=10),
            Container(content=imagem_perfil, margin=10),
            Container(content=texto_usuario, margin=10),
            Container(content=texto_usuario_handle, margin=10),
            Container(content=nav, margin=10),
            Container(content=card, margin=10),  
            Container(content=rodape, margin=10),

        ],
        spacing=30,
    )

def search(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens):
    page.title = "Tela de Pesquisa"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0
    page.bgcolor = "white"
    page.window.width = 380  # Largura máxima definida
    page.window.height = 710

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("W", size=32, weight=ft.FontWeight.BOLD, color="black"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor="#00ADEF",
        height=50,
        padding=ft.padding.only(left=10, right=10),
    )

    search_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextField(
                    hint_text="Buscar...",
                    expand=True,
                    border=ft.InputBorder.UNDERLINE,
                    text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color="black"),  # Texto digitado preto e negrito
                ),
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                    icon_color="black",
                    tooltip="Buscar",
                ),
                ft.IconButton(
                    icon=ft.icons.FILTER_LIST,
                    icon_color="black",
                    tooltip="Filtrar",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=10, vertical=5),
    )
    teste = Container(
        expand=True
    )


    # Rodapé com abas clicáveis
    rodape = Container(
        bgcolor=colors.WHITE,
        height=60,
        content=Row(
            [
                IconButton(icon=icons.HOME, icon_color=colors.BLACK,on_click=lambda _: navegar_para_home()),
                IconButton(icon=icons.SEARCH, icon_color=colors.BLACK,on_click=lambda _: mudar_para_search()),
                IconButton(icon=icons.ADD,icon_color=colors.BLACK,on_click=lambda _: mudar_para_criar_demanda()),
                IconButton(icon=icons.PERSON, icon_color=colors.BLACK,on_click=lambda _: mudar_para_user()),
                IconButton(icon=icons.CHAT, icon_color=colors.BLACK,on_click=lambda _: mudar_para_mensagens()),
            ],
            alignment="spaceAround",
        ),
    )
    return Column(
        [
            Container(content=header, margin=10),
            Container(content=search_row, margin=10),
            Container(content=teste, expand=True),
            Container(content=rodape, margin=10),
        ],
        spacing=30,
    )

def mensagens(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens):
    page.title = "Tela de Conversas"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0
    page.bgcolor = "#ffffff"
    page.window_width = 380  # Largura máxima definida
    page.window_height = 710
    page.horizontal_alignment = "center"  # Centraliza horizontalmente o conteúdo
    page.vertical_alignment = "start"  # Começa do topo da telae

    # Cabeçalho
    header = Container(
        bgcolor=ft.colors.BLUE,
        height=66,
        content=Row(
            [
                Image(
                    src="img/logo_worknet.png",  # URL da imagem
                    width=140,  # Largura da imagem
                    height=140,  # Altura da imagem
                    fit=ft.ImageFit.CONTAIN,  # Ajusta o tamanho da imagem
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Lista de conversas
    def conversation_item(photo, name, message, time, is_unread=False):
        return ft.Container(
            content=ft.Row(
                [
                    ft.CircleAvatar(
                        content=ft.Image(src=photo, fit=ft.ImageFit.COVER),
                        radius=25,
                    ),
                    ft.Column(
                        [
                            ft.Text(name, weight=ft.FontWeight.BOLD, size=14, color=ft.colors.BLACK),
                            ft.Text(message, size=12, color="#666666"),
                        ],
                        spacing=5,
                    ),
                    ft.Column(
                        [
                            ft.Text(time, size=10, color="#666666"),
                            ft.Container(
                                content=ft.Text("1", size=10, color="#ffffff"),
                                bgcolor="#00b5e2",
                                border_radius=10,
                                padding=5,
                                visible=is_unread,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=10,
            border=ft.Border(bottom=ft.BorderSide(1, "#dddddd")),
        )

    chat = Container(
        conversation_item(
            photo="img/predeiro.jpeg",
            name="PEDRO CAMPOS",
            message="Olá, boa tarde!",
            time="10:44",
            is_unread=True,
        ),
    )
    chat2 = Container(
        conversation_item(
            photo="img/Flavin.jpeg",
            name="AYRTON CARVALHO",
            message="Ok, sem problemas!",
            time="08:55",
        ),
    )
    chat3 = Container(
        conversation_item(
            photo="img/costureira.jpeg",
            name="FLAVIA MARIA",
            message="Consegue fazer assim?",
            time="07:51",
        ),
    )
    chat4 = Container(
        conversation_item(
            photo="img/homem.jpeg",
            name="EDUARDO COSTA",
            message="Desculpe, não vai acontecer novamente!",
            time="23 de abr.",
        ),
    )



    # Rodapé com abas clicáveis
    rodape = Container(
        bgcolor=colors.WHITE,
        height=60,
        content=Row(
            [
                IconButton(icon=icons.HOME, icon_color=colors.BLACK,on_click=lambda _: navegar_para_home()),
                IconButton(icon=icons.SEARCH, icon_color=colors.BLACK,on_click=lambda _: mudar_para_search()),
                IconButton(icon=icons.ADD,icon_color=colors.BLACK,on_click=lambda _: mudar_para_criar_demanda()),
                IconButton(icon=icons.PERSON, icon_color=colors.BLACK,on_click=lambda _: mudar_para_user()),
                IconButton(icon=icons.CHAT, icon_color=colors.BLACK,on_click=lambda _: mudar_para_mensagens()),
            ],
            alignment="spaceAround",
        ),
    )
    return Column(
        [
            Container(content=header, margin=10),
            Container(content=chat, margin=10),
            Container(content=chat2, margin=10),
            Container(content=chat3, margin=10),
            Container(content=chat4, margin=10),
            Container(content=rodape, margin=10),
        ],
        spacing=30,
    )

def main(page: Page):
    page.title = "WorkNet"
    page.bgcolor = colors.WHITE
    page.window.width = 380
    page.window.height = 710
    page.scroll = ft.ScrollMode.AUTO

    # Função para mudar para a tela Home
    def navegar_para_home():
        page.clean()
        page.add(tela_home(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens))
        page.update()

    # Função para mudar para a tela "Criar Demanda"
    def mudar_para_criar_demanda():
        page.clean()
        page.add(criar_tela_demanda(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens))
        page.update()

    def mudar_para_user():
        page.clean()
        page.add(user(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens))
        page.update()

    def mudar_para_search():
        page.clean()
        page.add(search(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens))
        page.update()
    
    def mudar_para_mensagens():
        page.clean()
        page.add(mensagens(page, navegar_para_home, mudar_para_criar_demanda, mudar_para_user,mudar_para_search,mudar_para_mensagens))
        page.update()

    # Mostrando a tela inicial
    page.add(tela_login(page, navegar_para_home))


ft.app(target=main)