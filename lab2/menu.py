from tkinter import *
from tkinter.ttk import *
from set_upload import get_sets
from quicksort import quicksort
from algorythm_timing import run_sorting_algorithm

if __name__ == '__main__':
    root = Tk()
    root.title("Quicksort")

    saved_sets = []

    values_set = StringVar()
    set_count = IntVar()
    message = StringVar()
    file_name = StringVar()

    def save_set():
        global saved_sets
        if set_count.get() == 10:
            message.set("Set list is full.")
            Label(root, text=f"{message.get()}").grid(row=0, column=2)
            return

        saved_sets.append(values_set.get().split(', '))
        set_count.set(set_count.get() + 1)
        Label(root, text=f"{set_count.get()}/10").grid(row=0, column=1)
        values_set.set("")
        return

    def upload_sets():
        global saved_sets
        saved_sets = get_sets(file_name.get())
        set_count.set(len(saved_sets))
        Label(root, text=f"{set_count.get()}/10").grid(row=0, column=1)
        return saved_sets

    def clean_sets():
        global saved_sets
        saved_sets = []
        set_count.set(0)
        Label(root, text=f"{set_count.get()}/10").grid(row=0, column=1)
        return

    def run_sorting():
        time_measures = Toplevel(root)
        time_measures.title("Time Measures")
        row_count = 0

        for i in saved_sets:
            Label(time_measures, text=str(row_count)).grid(row=row_count, column=0)
            Label(time_measures, text=run_sorting_algorithm(quicksort, i)).grid(row=row_count, column=1)

            row_count += 1

    Label(root, text="Введіть масиви:").grid(row=0, column=0)
    Label(root, text=f"{set_count.get()}/10").grid(row=0, column=1)
    Label(root, text=f"{message.get()}").grid(row=0, column=2)

    Entry(root, textvariable=values_set).grid(row=1, column=0)
    Button(root, text="Зберегти масив", command=save_set).grid(row=1, column=1)
    Button(root, text="Очистити масиви", command=clean_sets).grid(row=1, column=2)

    Label(root, text="Назва файлу:").grid(row=2, column=0)
    Entry(root, textvariable=file_name).grid(row=2, column=1)
    Button(root, text="Завантажити масиви", command=upload_sets).grid(row=2, column=2)

    Button(root, text="Сортувати", command=run_sorting).grid(row=3, column=0)

    root.mainloop()
