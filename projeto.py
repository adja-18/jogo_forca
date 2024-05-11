import flet as ft
import string
import random


def main(page: ft.Page):
    # colocar fundo na página
    page.bgcolor = ft.colors.BROWN_600
    
# criar fução

    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter=letter)
                word.update()
        if all(word_control.content.value != '_' for word_control in word.controls):
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value='Você ganhou! :)'),
                    open=True,
                )
                page.update()

        if e.control.content.value not in choiced:
            victim.data += 1
            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value='Você perdeu! :('),
                    open=True,
                )
                
                page.update()
            errors = victim.data
            victim.src = f'images/hangman_{errors}.png'
            victim.update()
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()

    def letter_to_guess(letter):
        return ft.Container(
            bgcolor=ft.colors.AMBER_500,
            height=50,
            width=50,
            border_radius=ft.border_radius.all(5),
            content=ft.Text(
                value=letter,
                color=ft.colors.BLACK,
                size=30,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
            )
        )

    palavra_filosofia = ["Verdade", "Conhecimento", "Razão", "Pensamento", "Logica",
                         "etica", "Moral", "Liberdade", "Justiça", "Bem",
                         "Mal", "Beleza", "Bom", "Feliz", "Realidade",
                         "Existência", "Dever", "Certo", "Errado", "Alma"]
    choiced = random.choice(palavra_filosofia).upper()
    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[

            letter_to_guess('_') for letter in choiced
        ]
    )
    victim = ft.Image(
        # Data parametro para fazer a troca de imagem
        data=0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        # Definir altura da imagem
        height=300,
    )
    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        # Distanciar todas as laterais
        padding=ft.padding.all(50),
        # criar conteúdo do content
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # criar a vítima
                victim,
                # criar a palavra para advinhar
                word
            ]
        )
    )
    # criar teclado
    Keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        # criar teclado com ROW
        content=ft.Row(
            # Estabelecer o tamanho limite da Row para que quebre a linha
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.BLACK,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        
                    ),
                    # adiconar cor de fundo do container
                    # bgcolor=ft.colors.ORANGE,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE],
                    ),
                    on_click=validate_letter
                  # criarloop list compreesion para as letras do alfabeto
                )for letter in string.ascii_uppercase
            ]
        )

    )
    # criar cena com caminho relativo
    scene = ft.Image(col=12, src='images/filosofia.jpg')

    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            # inserir cenários superior
            scene,
            # criar o jogo
            game,
            # criar o teclado
            Keyboard,
            # inserir cena inferior
            scene,

        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.update()
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main,view = ft.AppView.FLET_APP, assets_dir='assets')
