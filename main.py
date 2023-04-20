import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile


class SimpleData(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dataset Shortcuts")
        self.geometry("600x700")

        self.notebook = ttk.Notebook(self)

        getdata_tab = ttk.Frame(self.notebook)
        showdata_tab = ttk.Frame(self.notebook)
        data_choices_tab = ttk.Frame(self.notebook)

        self.getdata_button = tk.Button(getdata_tab, text="Upload Dataset", command=self.uploaddata
                                        , bg="lightblue", fg="white")
        self.getdata_button.pack(side=tk.BOTTOM, fill=tk.X)
        self.get_data_label = ttk.Label(getdata_tab, text="Code to upload a dataset here", background="white"
                                        , foreground="black", justify="center")
        self.get_data_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.download_data_button = tk.Button(showdata_tab, text="Save Dataset", command=self.savedata
                                               , bg="red", fg="black")
        self.download_data_button.pack(side=tk.BOTTOM)
        self.show_data_label = ttk.Label(showdata_tab, text="Dataset Stats here", background="white"
                                        , foreground="black", justify="center")
        self.show_data_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.commit_change_button = tk.Button(data_choices_tab, text="Commit Changes", command=self.commitchange
                                              , bg="lightblue", fg="white")
        self.commit_change_button.pack(side=tk.BOTTOM, fill=tk.X)
        self.change_label = ttk.Label(data_choices_tab, text="Ability to adjust dataset here i.e. Remove duplicates"
                                      , background="white", foreground="black", justify="center")
        self.change_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(getdata_tab, text="Get Dataset")
        self.notebook.add(showdata_tab, text="Discovery")
        self.notebook.add(data_choices_tab, text="Possible Changes")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    def uploaddata(self, path=None):
        pass

    def savedata(self):
        pass

    def commitchange(self):
        pass


if __name__ == "__main__":
    simpledata = SimpleData()
    simpledata.mainloop()
