from tkinter import Tk, ttk, constants


class GUI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label_from_file = ttk.Label(master=self._root, text='Process this file:')
        entry_from_file = ttk.Entry(master=self._root)
        button_from_file = ttk.Button(master=self._root, text='Browse')

        label_to_file = ttk.Label(master=self._root, text='Save result to:')
        entry_to_file = ttk.Entry(master=self._root)
        button_to_file = ttk.Button(master=self._root, text='Browse')

        label_compr_method = ttk.Label(master=self._root, text='Compression method')
        radio_huffman = ttk.Radiobutton(master=self._root, text='Huffman coding')
        radio_lzw = ttk.Radiobutton(master=self._root, text='Lempel-Ziv-Welch')

        button_compress = ttk.Button(master=self._root, text='Compress')
        button_decompress = ttk.Button(master=self._root, text='Decompress')

        label_from_file.grid(row=0, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        entry_from_file.grid(row=1, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        button_from_file.grid(row=1, column=2, sticky=(constants.W, constants.E), padx=5, pady=5)

        label_to_file.grid(row=2, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        entry_to_file.grid(row=3, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        button_to_file.grid(row=3, column=2, sticky=(constants.W, constants.E), padx=5, pady=5)

        label_compr_method.grid(row=4, column=0, padx=5, pady=5)
        radio_huffman.grid(row=5, column=0, padx=5, pady=5)
        radio_lzw.grid(row=5, column=1, padx=5, pady=5)

        button_compress.grid(row=6, column=0, padx=5, pady=5)
        button_decompress.grid(row=6, column=2, padx=5, pady=5)


window = Tk()
window.title('Text Compressor')
window.resizable(False, False)
window.geometry('420x240')

gui = GUI(window)
gui.start()

window.mainloop()
