def oled_line_print(text: str, oled) -> None:
    oled.scroll(0, -oled.pages)
    oled.fill_rect(0, oled.height - oled.pages, oled.width, oled.height, 0)
    oled.text(text, 0, oled.height - oled.pages, 1)
    oled.show()
