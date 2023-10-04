# instalar 
# pip install flet

# Passo a passo
# Passo 1: Botao de iniciar chat
# PAsso 2: Popup para entrar no char
    # quando entrar no chat a mensagem que voce entrou 
    # e o botão de enviar mensagem
# a cada mensagem que voce envia aparece para todo mundo
    # Nome: Texto da mensagem

# flet -> backend/frontend
import flet as ft

def main(pagina): # criar funcao da pagina principal
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(Label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem"!
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar mensagem no chat
            chat.controls.append(ft.Text(f"usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"usuario_mensagem}: entrou no chat",
            size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # comunicacao entre usuarios

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto"! campo_mensagem.value, "usuario"! nome_usuario.value,
        "tipo": "mensagem" })
        # limpar o campo de mensagens
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(Label="Digite uma mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        pagina.add(chat)

        # Fechar o popup
        popup.open = false

        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        # criar campo de mensagem usuario
        # criar o botão de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
         pagina.update()         

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Benvindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.TextButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.TextButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto) 
    pagina.add(botao_iniciar) 

ft.app(target=main, view=ft.WEB_BROWSER, port=8000) # funcao que vai executar o site
