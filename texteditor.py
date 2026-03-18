import flet as ft

def main(page: ft.Page):
    def changeText(e):
        countWords()
        countCharacters()

    def countWords():
        words_text.value = f"Word count: {len(text_box.value.strip().split())}"

    def countCharacters():
        characters_text.value = f"Character Count: {len(text_box.value.strip())}"

    text_box = ft.TextField(
        multiline=True,
        hint_text="Write watever you want",
        on_change=changeText
    )

    words_text = ft.Text(
        value="",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PINK_400,
        size=55
    )

    characters_text = ft.Text(
        value="",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PINK_400,
        size=55
    )

    page.add(words_text, characters_text, text_box)

ft.run(main)
