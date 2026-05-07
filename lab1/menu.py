from tkinter import *
from tkinter.ttk import *
from functions import *
from variable_upload import *

def get_set(set_var):
    try:
        return list([int(i) for i in set_var.get().split(', ')])
    except ValueError:
        set_var.set("")

if __name__ == '__main__':
    root = Tk()
    root.title("Window 1")

    def exec_linear():
        a_linear = a.get()
        c_linear_here = c_linear.get()
        linear_result.set(f"{linear((a_linear), c_linear_here):.2f}")
        return

    def exec_branched():
        x_branched = x.get()
        k_branched = k.get()
        c_branched_here = c_branched.get()
        b_branched = b.get()
        branched_result.set(f"{branched(x_branched, k_branched,c_branched_here, b_branched):.2f}")
        return

    def exec_cyclical():
        a_cyclical = get_set(a_set)
        n_cyclical = n.get()
        cyclical_result.set(f"{cyclical(a_cyclical, n_cyclical):.2f}")
        return

    def upload_values():
        for i in range(len(var_list)):
            var_list[i].set(var_search(file_name.get(), var_name_list[i]))

    a = IntVar()
    c_linear = IntVar()

    x = IntVar()
    k = IntVar()
    c_branched = IntVar()
    b = IntVar()

    a_set = StringVar()
    n = IntVar()

    linear_result = StringVar()
    branched_result = StringVar()
    cyclical_result = StringVar()

    file_name = StringVar()
    var_list = [a, c_linear, x, k, c_branched, b, a_set, n]
    var_name_list = ['a', 'c_linear', 'x', 'k', 'c_branched', 'b', 'a_set', 'n']

    Label(root, text="Значення змінних").grid(row=0, column=3)

    Label(root, text="a:").grid(row=1, column=0)
    Label(root, text="c:").grid(row=2, column=0)
    Entry(root, textvariable=a).grid(row=1, column=1)
    Entry(root, textvariable=c_linear).grid(row=2, column=1)

    Label(root, text="x:").grid(row=1, column=2)
    Label(root, text="k:").grid(row=2, column=2)
    Label(root, text="c:").grid(row=1, column=4)
    Label(root, text="b:").grid(row=2, column=4)
    Entry(root, textvariable=x).grid(row=1, column=3)
    Entry(root, textvariable=k).grid(row=2, column=3)
    Entry(root, textvariable=c_branched).grid(row=1, column=5)
    Entry(root, textvariable=b).grid(row=2, column=5)

    Label(root, text="a:").grid(row=1, column=6)
    Label(root, text="n:").grid(row=2, column=6)
    Entry(root, textvariable=a_set).grid(row=1, column=7)
    Entry(root, textvariable=n).grid(row=2, column=7)

    Button(root, text="Linear", command=exec_linear).grid(row=3, column=1)
    Button(root, text="Branched", command=exec_branched).grid(row=3, column=3)
    Button(root, text="Cyclical", command=exec_cyclical).grid(row=3, column=7)

    Entry(root, textvariable=linear_result).grid(row=4, column=1)
    Entry(root, textvariable=branched_result).grid(row=4, column=3)
    Entry(root, textvariable=cyclical_result).grid(row=4, column=7)

    Label(root, text="Файл:").grid(row=5, column=0)
    Entry(root, textvariable=file_name).grid(row=5, column=1)
    Button(root, text="Upload", command=upload_values).grid(row=5, column=3)

    root.mainloop()
