import time
from tkinter import ttk, constants, StringVar, filedialog, messagebox

from services.text_compressor_service import TextCompressorService


class GUI:
    def __init__(self, root, service: TextCompressorService):
        self._root = root
        self.service = service

    def _select_from_file(self):
        filetypes = (
            ('All files', '*'),
            ('Text files', '*.txt'),
            ('Huffman coded files', '*.hc'),
            ('LZW compressed files', '*.lzw'),
            ('HC and LZW compressed files', '*.tczip')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            filetypes=filetypes
        )
        self._from_file_var.set(filename)

    def _select_to_file(self):
        filetypes = (
            ('All files', '*'),
            ('Text files', '*.txt'),
            ('Huffman coded files', '*.hc'),
            ('LZW compressed files', '*.lzw'),
            ('HC and LZW compressed files', '*.tczip')
        )
        filename = filedialog.asksaveasfilename(
            title='Save to file...',
            filetypes=filetypes,
            confirmoverwrite=True
        )
        self._to_file_var.set(filename)

    def _handle_button_compress_click(self, method: str):
        from_value = self._from_file_var.get()
        to_value = self._to_file_var.get()
        method_value = self._method_var.get()

        if not from_value or not to_value:
            messagebox.showerror(
                title='Error',
                message='Both files must be defined'
            )
        else:
            match method:
                case 'compress':
                    try:
                        start_time = time.time()
                        encoding_successful = self.service.encode_file(
                            from_value, to_value, method_value
                        )
                        end_time = time.time()
                        elapsed_time = end_time-start_time
                        if encoding_successful:
                            messagebox.showinfo(
                                title='Compression result',
                                message=f"FILE\n\n{from_value}\n\nCOMPRESSED TO FILE\n\n{to_value}\n\nUSING: {method_value}\nELAPSED TIME: {elapsed_time:.2f} seconds"
                            )
                        else:
                            messagebox.showerror(
                                title='Error',
                                message=f"\nFile {from_value} couldn't be compressed"
                            )
                    except (ValueError) as error:
                        messagebox.showerror(
                            title='Error',
                            message=f"Error: {error}"
                        )
                case 'decompress':
                    try:
                        start_time = time.time()
                        encoding_successful = self.service.decode_file(
                            from_value, to_value, method_value
                        )
                        end_time = time.time()
                        elapsed_time = end_time-start_time
                        if encoding_successful:
                            messagebox.showinfo(
                                title='Decompression result',
                                message=f"FILE\n\n{from_value}\n\nDECOMPRESSED TO FILE\n\n{to_value}\n\nUSING: {method_value}\nELAPSED TIME: {elapsed_time:.2f} seconds"
                            )
                        else:
                            messagebox.showerror(
                                title='Error',
                                message=f"\nFile {from_value} couldn't be decompressed"
                            )
                    except (ValueError) as error:
                        messagebox.showerror(
                            title='Error',
                            message=f"Error: {error}"
                        )
                case _default:
                    messagebox.showerror(
                        title='Error',
                        message='something went wrong!'
                    )

    def start(self):
        self._method_var = StringVar()
        self._method_var.set('huffman coding')
        self._from_file_var = StringVar()
        self._to_file_var = StringVar()

        lbl_from_file = ttk.Label(master=self._root, text='Process this file:')
        ent_from_file = ttk.Entry(
            master=self._root, textvariable=self._from_file_var)
        btn_from_file = ttk.Button(
            master=self._root,
            text='Browse',
            command=self._select_from_file
        )

        lbl_to_file = ttk.Label(master=self._root, text='Save result to:')
        ent_to_file = ttk.Entry(
            master=self._root, textvariable=self._to_file_var)
        btn_to_file = ttk.Button(
            master=self._root,
            text='Browse',
            command=self._select_to_file
        )

        lbl_compr_method = ttk.Label(
            master=self._root, text='Compression method')
        rad_huffman = ttk.Radiobutton(
            master=self._root,
            text='Huffman coding',
            variable=self._method_var,
            value='huffman coding',
            state='ACTIVE'
        )
        rad_lzw = ttk.Radiobutton(
            master=self._root,
            text='Lempel-Ziv-Welch',
            variable=self._method_var,
            value='lzw'
        )
        rad_both = ttk.Radiobutton(
            master=self._root,
            text='Both',
            variable=self._method_var,
            value='both'
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

        lbl_from_file.grid(row=0, column=0, columnspan=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        ent_from_file.grid(row=1, column=0, columnspan=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        btn_from_file.grid(row=1, column=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)

        lbl_to_file.grid(row=2, column=0, columnspan=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        ent_to_file.grid(row=3, column=0, columnspan=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        btn_to_file.grid(row=3, column=2, sticky=(
            constants.W, constants.E), padx=5, pady=5)

        lbl_compr_method.grid(row=4, column=0, padx=5, pady=5)
        rad_huffman.grid(row=5, column=0, padx=5, pady=5)
        rad_lzw.grid(row=5, column=1, padx=5, pady=5)
        rad_both.grid(row=5, column=2, padx=5, pady=5)

        btn_compress.grid(row=6, column=0, padx=5, pady=5)
        btn_decompress.grid(row=6, column=2, padx=5, pady=5)
