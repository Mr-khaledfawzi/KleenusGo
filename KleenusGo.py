import flet as ft

def main(page: ft.Page):
    page.title = "Kleenus Go"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 380
    page.window_height = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#121212"

    # العناصر الرسومية
    header = ft.Text("KLEENUS GO", size=35, weight="bold", color="#3b8ed0")
    author = ft.Text("By Khaled", size=14, italic=True, color="grey")

    # بطاقة معلومات
    info_card = ft.Container(
        content=ft.Column([
            ft.Text("System Status", weight="bold"),
            ft.Text("Safe & Optimized", color="green"),
        ]),
        padding=20, bgcolor="#1e1e1e", border_radius=15, width=320
    )

    progress_bar = ft.ProgressBar(width=300, color="blue", visible=False)
    status_msg = ft.Text("", size=12, color="#aaaaaa")

    # دالة الضغط
    def start_process(e):
        progress_bar.visible = True
        status_msg.value = "Kleenus Go is working..."
        page.update()

    # استخدام ElevatedButton بأبسط صورة ممكنة لتجنب الخطأ
    btn = ft.ElevatedButton(
        content=ft.Text("BOOST MOBILE", weight="bold"), # وضعنا النص داخل content
        on_click=start_process,
        width=250,
        height=50
    )

    # وضع كل شيء داخل عمود مركزي
    content_view = ft.Column(
        [
            ft.Divider(height=40, color="transparent"),
            header,
            author,
            ft.Divider(height=20, color="transparent"),
            info_card,
            ft.Divider(height=30, color="transparent"),
            btn,
            ft.Divider(height=20, color="transparent"),
            progress_bar,
            status_msg,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(content_view)

ft.app(target=main)