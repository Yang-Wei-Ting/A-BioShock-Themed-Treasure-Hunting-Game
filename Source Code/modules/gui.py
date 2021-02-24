import random, tkinter as tk


def add_landscape(image, row, column, rowspan=1, columnspan=1):
    "Adds the image to the window."
    tk.Label(
        master=window,
        image=image,
        borderwidth=0,
    ).grid(
        row=row,
        column=column,
        rowspan=rowspan,
        columnspan=columnspan,
    )


def update_label(instance):
    "Updates the instance's label."
    if hasattr(instance, "label"):
        instance.label.grid_remove()
    try:
        instance.label = tk.Label(
            master=window,
            width=2,
            height=1,
            bg=instance.color,
            relief=tk.RAISED,
            borderwidth=5
        )
        instance.label.grid(row=-instance.y + 6, column=instance.x + 6)
    except tk.TclError:
        pass


def add_bad_guy_boat():
    "Adds the image water_ne_arrival to the window."
    add_landscape(water_ne_arrival, 0, 12)


def remove_label(instance):
    "Removes the instance's label."
    instance.label.grid_remove()


window = tk.Tk()
window.title("Map")
window.resizable(width=False, height=False)


land_tuple = tuple(tk.PhotoImage(file=f"landscape/land_{i}.gif") for i in range(1, 15))
mountain_tuple = tuple(tk.PhotoImage(file=f"landscape/mountain_{i}.gif") for i in (1, 2, 3))
water_n = tk.PhotoImage(file="landscape/water_n.gif")
water_s = tk.PhotoImage(file="landscape/water_s.gif")
water_w = tk.PhotoImage(file="landscape/water_w.gif")
water_e = tk.PhotoImage(file="landscape/water_e.gif")
water_nw = tk.PhotoImage(file="landscape/water_nw.gif")
water_ne = tk.PhotoImage(file="landscape/water_ne.gif")
water_sw = tk.PhotoImage(file="landscape/water_sw.gif")
water_se = tk.PhotoImage(file="landscape/water_se.gif")
water_ne_arrival = tk.PhotoImage(file="landscape/water_ne_arrival.gif")


for row in range(1, 12):
    for column in range(1, 12):
        add_landscape(random.choices(land_tuple, weights=[2, 2, 3, 3, 4, 4, 5, 4, 4, 3, 3, 2, 2, 3], k=1), row, column)

add_landscape(mountain_tuple[0], random.randint(1, 5), random.randint(1, 3), 3, 3)
add_landscape(mountain_tuple[1], random.randint(6, 9), random.randint(6, 9), 3, 3)
add_landscape(mountain_tuple[2], random.randint(1, 3), random.randint(6, 9), 3, 3)

for column in range(1, 12):
    add_landscape(water_n, 0, column)
    add_landscape(water_s, 12, column)

for row in range(1, 12):
    add_landscape(water_w, row, 0)
    add_landscape(water_e, row, 12)

add_landscape(water_nw, 0, 0)
add_landscape(water_ne, 0, 12)
add_landscape(water_sw, 12, 0)
add_landscape(water_se, 12, 12)
