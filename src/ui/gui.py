from tkinter import Tk, ttk, constants, StringVar, filedialog, messagebox


class GUI:
    def __init__(self, root):
        self._root = root

    def _select_from_file(self):
        filetypes = (
            ('Text files', '*.txt'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            filetypes=filetypes
        )
        self._from_file_var.set(filename)

    def _select_to_file(self):
        filename = filedialog.asksaveasfilename(
            title='Save to file...',
            confirmoverwrite=True
        )
        self._to_file_var.set(filename)

    def _handle_button_compress_click(self, method:str):
        from_value = self._from_file_var.get()
        to_value = self._to_file_var.get()
        method_value = self._method_var.get()
        match method:
            case 'compress':
                messagebox.showinfo(
                    title='Compression result',
                    message=f"{method_value} compressing\n{from_value}\nto\n{to_value}!"
                )
            case 'decompress':
                messagebox.showinfo(
                    title='Compression result',
                    message=f"{method_value} decompressing\n{from_value}\nto\n{to_value}!"
                )
            case _default:
                messagebox.showerror(
                    title='Error',
                    message='something went wrong!'
                )

    def start(self):
        self._method_var = StringVar()
        self._method_var.set('Huffman coding')
        self._from_file_var = StringVar()
        self._to_file_var = StringVar()
    
        lbl_from_file = ttk.Label(master=self._root, text='Process this file:')
        ent_from_file = ttk.Entry(master=self._root, textvariable=self._from_file_var)
        btn_from_file = ttk.Button(
            master=self._root,
            text='Browse',
            command=self._select_from_file
        )

        lbl_to_file = ttk.Label(master=self._root, text='Save result to:')
        ent_to_file = ttk.Entry(master=self._root, textvariable=self._to_file_var)
        btn_to_file = ttk.Button(
            master=self._root,
            text='Browse',
            command=self._select_to_file
        )

        lbl_compr_method = ttk.Label(master=self._root, text='Compression method')
        rad_huffman = ttk.Radiobutton(
            master=self._root,
            text='Huffman coding',
            variable=self._method_var,
            value='Huffman coding',
            state='ACTIVE'
        )
        rad_lzw = ttk.Radiobutton(
            master=self._root,
            text='Lempel-Ziv-Welch',
            variable=self._method_var,
            value='LZW'
        )

        btn_compress = ttk.Button(
            master=self._root,
            text='Compress',
            command=lambda: self._handle_button_compress_click('compress')
        )
        btn_decompress = ttk.Button(
            master=self._root,
            text='Decompress',
            command=lambda: self._handle_button_compress_click('decompress')
        )

        lbl_from_file.grid(row=0, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        ent_from_file.grid(row=1, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        btn_from_file.grid(row=1, column=2, sticky=(constants.W, constants.E), padx=5, pady=5)

        lbl_to_file.grid(row=2, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        ent_to_file.grid(row=3, column=0, columnspan=2, sticky=(constants.W, constants.E), padx=5, pady=5)
        btn_to_file.grid(row=3, column=2, sticky=(constants.W, constants.E), padx=5, pady=5)

        lbl_compr_method.grid(row=4, column=0, padx=5, pady=5)
        rad_huffman.grid(row=5, column=0, padx=5, pady=5)
        rad_lzw.grid(row=5, column=1, padx=5, pady=5)

        btn_compress.grid(row=6, column=0, padx=5, pady=5)
        btn_decompress.grid(row=6, column=2, padx=5, pady=5)


window = Tk()
window.title('Text Compressor')
window.resizable(False, False)
window.geometry('420x240')

gui = GUI(window)
gui.start()

window.mainloop()
