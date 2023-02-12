import json
import tkinter as tk
from tkinter import filedialog
import random

# Load the JSON file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Save the JSON file
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Update the JSON data
def update_json(data, attribute, factor, filter=False, max=0, min=0, factorrandom=False):
    for item in data['Items']:
        value_type = type(item[attribute])
        if filter:
            if value_type == int or value_type == float:
                if item[attribute] <= max and item[attribute] >= min:
                    if factorrandom:
                        item[attribute] = value_type(item[attribute] * random.uniform(factor - 0.5, factor + 1.5))
                    else:                       
                        item[attribute] = value_type(item[attribute] * factor)
                else:
                    pass
            else:
                pass
        else:
            if value_type == int or value_type == float:
                if factorrandom:
                    item[attribute] = value_type(item[attribute] * random.uniform(factor - 0.5, factor + 1.5))
                else:
                    item[attribute] = value_type(item[attribute] * factor)
            else:
                pass
    return data

# Main GUI
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("JSON Updater")
        self.filename = tk.StringVar()
        self.attribute = tk.StringVar()
        self.factor = tk.DoubleVar()
        self.max = tk.DoubleVar()
        self.min = tk.DoubleVar()
        self.filter = tk.BooleanVar()
        self.factorrandom = tk.BooleanVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="JSON File:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.filename).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self, text="Browse", command=self.load_file).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self, text="Attribute:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.attribute).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Factor:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.factor).grid(row=2, column=1, padx=5, pady=5)
        tk.Checkbutton(self, text="Random", variable=self.factorrandom).grid(row=2, column=2, padx=5, pady=5)
        #add a checkbox if you want to use the max and min values
        tk.Checkbutton(self, text="Filter", variable=self.filter).grid(row=3, column=0, padx=5, pady=5)
        tk.Label(self, text="Max:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.max).grid(row=4, column=1, padx=5, pady=5)
        tk.Label(self, text="Min:").grid(row=5, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.min).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self, text="Update", command=self.update_file).grid(row=6, column=1, padx=5, pady=5)

    def load_file(self):
        self.filename.set(filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")]))

    def update_file(self):
        data = load_json(self.filename.get())
        data = update_json(data, self.attribute.get(), self.factor.get(), self.filter.get(), self.max.get(), self.min.get(), self.factorrandom.get())
        save_json(data, self.filename.get())
        return "break"

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
