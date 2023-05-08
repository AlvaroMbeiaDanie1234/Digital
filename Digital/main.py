from time import sleep
import pymysql
import sqlite3
import flet as ft 
from flet import(Page, TextField, AppBar, Text, Icon, icons, IconButton, colors, ElevatedButton, TextButton, Row,
	Container, Card, ListTile, Image, PopupMenuButton, PopupMenuItem, ButtonStyle, AlertDialog, ResponsiveRow,
	ProgressBar, alignment, Divider, OutlinedButton, LinearGradient, SnackBar, Dropdown, dropdown,
	FloatingActionButton,
	AlertDialog,
	Column,
	BottomSheet,
	Banner,
	)


def main(page: ft.Page):
	page.title = "AMDM"
	page.scroll = True
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER



	def white_dark_mode(e):
		e.control.selected = not e.control.selected
		e.control.update()
		if(e.control.selected == True):
			page.theme_mode = "LIGHT"
			page.update()
		else:
			page.theme_mode = "DARK"
			page.update()


	menu =AppBar(
		#title=Text("All Digital", size=30,),
		leading=Image(src="assets/logoAluy.png"),
		leading_width=200,
		bgcolor=colors.BLUE_300,
		actions=[
		IconButton(icons.DARK_MODE,
			selected=False,
			selected_icon=icons.LIGHT_MODE,
			tooltip="Mudar tema",
			on_click=white_dark_mode,
			style=ButtonStyle(color={"selected": colors.BLACK, "":colors.WHITE})
			),
		PopupMenuButton(
			items=[
			PopupMenuItem(text="Sign", icon=icons.PERSON),
			PopupMenuItem(text="Mensagem", icon=icons.CHAT),
			PopupMenuItem(), #DIvider
			PopupMenuItem(text="FeedBack", icon=icons.FEEDBACK)
			],
			)
		],

		)
	page.add(menu)

	a = Card(
		content=ft.Container(
			content=Column(
				[
				ListTile(
					title=Text("Olá, seja bem-vindo a All Digital!"),
					subtitle=Text(" A amdm, vai garantir uma vida agradavél da sua grande ou pequena empressa no mundo digital..."),
					tooltip="Equipa amdm",
					leading=Image(src="assets/team.png", border_radius=90),),
				Row([TextField(hint_text="Tem uma duvida? pesquise aqui", border="underline",  width=300, height=40, prefix_icon=icons.SEARCH), 
					],
					alignment="center")
				]
				)
			)
		)
	page.add(a)


	#====================Vantagens=======================#
	a = Text("All Digital é uma super e pequena empressa de técnologias\nem online que presta diferentes tipos de serviços\ncomo desenvolvimento de softwares para\npequena e grandes empressas e outros...", weight="bold")
	baixar = OutlinedButton("baixar", width=50)

	a1 = Column(
		[
		Text("Quem somo nós?", size=17, weight="bold"),
		Text("All Digital é uma super e pequena empressa de técnologias\nem online que presta diferentes tipos de serviços\ncomo desenvolmineto de softwares para\npequena e grandes empressas e outros..."),
		Text("Baixar o App!", weight="bold"),
		Row([
			OutlinedButton(text="Android", icon=icons.ANDROID, tooltip="Baixar para android"),
			ElevatedButton(text="Computador", icon=icons.COMPUTER, bgcolor=colors.RED_400, color=colors.BLACK, tooltip="Baixar para computador")
			]),
		Image(src="assets/logoAluy.png"),
		]
		)
	amdm = ft.Container(
		content=ResponsiveRow([a1
			],
		
		height=200,
		width=700,
			),
		#bgcolor=ft.colors.BLUE_200,
		padding=10
		)
	page.add(amdm)

	vantagem = Container(
		content=Column(
			[
			Text("Vantagens de escolher á All Digital", weight="bold", size=22),
			],
		height=50,
			)
		)
	page.add(vantagem)


	#==========================cadastrar Cliente ===================================#
	def cliente(e):
		Nome = TextField(hint_text="Nome completo", prefix_icon=icons.PERSON)
		Empressa = TextField(hint_text="Nome da empressa", prefix_icon=icons.STORE)
		Email = TextField(hint_text="E-mail", prefix_icon=icons.EMAIL)
		Telefone = TextField(hint_text="Contacto", prefix_icon=icons.PHONE, prefix_text="+244 ")
		tipo = Dropdown(
        hint_text="O que Você deseja?",
        options=[
            dropdown.Option("Sistema Escolar"),
            dropdown.Option("Blogge"),
            dropdown.Option("Portfolio"),
            dropdown.Option("E-commerce"),
            dropdown.Option("Um site pessoal"),
            dropdown.Option("Site para minha empressa"),
            dropdown.Option("Outros"),
        ],
    )

		dlg_perfil = ft.AlertDialog(
			title=ft.TextButton("É simples e rápido", icon=icons.PERSON, disabled=True),
			content=ft.Column([Nome, Empressa, Email, Telefone, tipo, ElevatedButton(text="Submeter", width=500)], width=400, height=390, tight=True, scroll=True),
			)
		page.dialog = dlg_perfil
		dlg_perfil.open = True
		page.update()





	page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column([
                    	Image(src="assets/1.png"),
                    	Text("Software modernos", weight="bold")
                    	]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_200,
                    width=160,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Column(
                    	[
                    	Image(src="assets/2.png"),
                    	Text("Rapidez na entrega", weight="bold")
                    	]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_200,
                    width=160,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Inovação!"),
                ),
                ft.Container(
                    content=ft.Column([
                    	Image(src="assets/3.png"),
                    	Text("Profissionalismo", weight="bold")
                    	]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_200,
                    width=160,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Column([
                    	Image(src="assets/4.png"),
                    	Text(" Divulgação", weight="bold")
                    	]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            wrap = True
        ),

         ft.Container(
         	content=ft.Row([
         		Image(src="assets/pessoas.png", width=180),
         		Text("Deixe-nos conectar a sua empressa ao mundo digital\n aondo tudo e todos podem ver... ", weight="bold", size=17),
         		],
         		wrap=True
         		),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=1000,
                    height=454,
                    border_radius=5,
                    ink=True,
                ),
        Divider(),
        Text("Com técnologias de ultima geração", weight="bold"),

        ft.Container(
         	content=ft.Row([
         		Image(src="assets/python.png", width=180),
         		Image(src="assets/mysql.png", width=180),
         		Image(src="assets/sqlite.png", width=100),
         		Image(src="assets/github.png", width=100),
         		
         		],
         		wrap=True
         		),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=1000,
                    height=404,
                    border_radius=5,
                    ink=True,
                ),


        #===================================Serviços================================#

        ft.Container(
         	content=ft.Row([
         		ft.Container( width=160, height=170, border_radius=10, alignment=alignment.center,
         			content=Column([
         				Image(src="assets/a.png"),
         				Text("Sistema Escolar", weight="bold"),
         				ElevatedButton("Saber mais", icon=icons.MORE)
         				
         				]),
         			gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=[colors.RED, colors.ORANGE, colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode="mirror",
                        ),
         			),

         		#===============================================Blogger=============================#
         		ft.Container( width=160, height=170, border_radius=10, alignment=alignment.center,
         			content=Column([
         				Image(src="assets/a.png"),
         				Text("Blogger Pessoal", weight="bold"),
         				ElevatedButton("Saber mais", icon=icons.MORE)
         				
         				]),
         			gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=[colors.RED, colors.ORANGE, colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode="mirror",
                        ),
         			),
                
                #===========================================Web Site===============================#
         		ft.Container( width=160, height=170, border_radius=10, alignment=alignment.center,
         			content=Column([
         				Image(src="assets/a.png"),
         				Text("Web Site", weight="bold"),
         				ElevatedButton("Saber mais", icon=icons.MORE)
         				
         				]),
         			gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=[colors.RED, colors.ORANGE, colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode="mirror",
                        ),
         			),


         		ft.Container( width=160, height=170, border_radius=10, alignment=alignment.center,
         			content=Column([
         				Image(src="assets/a.png"),
         				Text("E outros", weight="bold"),
         				ElevatedButton("Saber mais", icon=icons.MORE)
         				
         				]),
         			gradient=LinearGradient(
                        begin=alignment.center_left,
                        end=alignment.center_right,
                        colors=[colors.RED, colors.ORANGE, colors.BLUE],
                        stops=[0.1, 0.2, 1.0],
                        tile_mode="mirror",
                        ),
         			),


         		],
         		wrap=True
         		),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=1000,
                    height=350,
                    border_radius=5,
                    ink=True,
                    ),

        ft.FloatingActionButton(
        icon=ft.icons.FACEBOOK),

        TextButton("Inscrever-se", icon=icons.PERSON, on_click=cliente),
        Text(""),

        SnackBar(
        	ft.Text("A equipa de programadores foi notificado"), 
        	open=True,
        	)




    )





#=======================================Aviso de verificação==========================#

	sleep(6)
	mensagem = TextButton(text="A equipa amdm trabalha com rapidez e profissionalismo para dar aos seus clientes o que realmente querem", disabled=True)
	img = Image(src="assets/team.png")
	dlg_perfil = ft.AlertDialog(
		title=ft.TextButton("Somos verificado pela AGT", icon=icons.VERIFIED, disabled=True),
		content=ft.Column([img, mensagem], width=370, height=250, tight=True, scroll=True),
		)
	page.dialog = dlg_perfil
	dlg_perfil.open = True
	page.update()

	        

ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)