import flet as ft
import time

# def main(page: ft.Page):
#   # Basic text usage
#   t = ft.Text(value="Hello, world!", color="green")
#   page.controls.append(t)
#   page.update()

# def main(page: ft.Page):
#   # Add is a shortcut to append() and update()
#   t = ft.Text()
#   page.add(t)

#   for i in range(10):
#     t.value = f"Step {i}"
#     page.update()
#     time.sleep(1)

# Example of simple controls
# def main(page: ft.Page):
#   page.add(
#     ft.Row(
#       controls=[
#         ft.Text("A"),
#         ft.Text("B"),
#         ft.Text("C"),
#       ]
#     )
#   )

#   page.add(
#     ft.Row(
#       controls=[
#         ft.TextField(label="Your Name"),
#         ft.ElevatedButton(text="Say my name!")
#       ]
#     )
#   )

#   # update() is smart enough to know what to update in the UI
#   # for i in range(10):
#   #   page.controls.append(ft.Text(f"Line {i}"))
#   #   if i > 4:
#   #     page.controls.pop(0)
#   #   page.update()
#   #   time.sleep(0.3)

#   def button_clicked(e):
#     page.add(ft.Text("Clicked!"))

#   page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


# Simple tasks app
# def main(page: ft.Page):
#   def add_clicked(e):
#     page.add(ft.Checkbox(label=new_task.value))
#     new_task.value = ""
#     new_task.focus()
#     new_task.update()

#   new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
#   page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

# Flet can use refs just as React does, this keeps a track on the elements, can be more verbose
def main(page: ft.Page):
  first_name = ft.Ref[ft.TextField]()
  last_name = ft.Ref[ft.TextField]()
  greetings = ft.Ref[ft.Column]()

  def bttn_click(e):
    greetings.current.controls.append(
      ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}")
    )
    first_name.current.value = ""
    last_name.current.value = ""
    page.update()
    first_name.current.focus()

  page.add(
    ft.TextField(ref=first_name, label="First name", autofocus=True),
    ft.TextField(ref=last_name, label="Last name"),
    ft.ElevatedButton("Say hello!", on_click=bttn_click),
    ft.Column(ref=greetings)
  )


ft.app(target=main)