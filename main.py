from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)
    print(quote)


window = Tk()
window.title("YE says:")
window.config(padx=30, pady=30)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click me, so I can start with quotes!", width=250, font=("Arial", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
