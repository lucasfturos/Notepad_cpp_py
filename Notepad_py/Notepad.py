import os
from tkinter import Tk, Text, Menu, Scrollbar, E, N, S, W, Y, END, RIGHT
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Notepad:
    """Class Notepad"""

    __root = Tk()
    __this_width = 680
    __this_height = 480
    __this_text_area = Text(__root)
    __this_menu_bar = Menu(__root)
    __this_file_menu = Menu(__this_menu_bar, tearoff=0)
    __this_edit_menu = Menu(__this_menu_bar, tearoff=0)
    __this_about_menu = Menu(__this_menu_bar, tearoff=0)
    __this_scroll_bar = Scrollbar(__this_text_area)
    __file = None

    def __init__(self, **kwargs) -> None:
        """Função de inicialização do programa"""
        # Define tamanho da janela
        try:
            self.__this_width = kwargs["width"]
        except KeyError:
            print("Err width")
        try:
            self.__this_height = kwargs["height"]
        except KeyError:
            print("Err height")

        # Define titulo da janela
        self.__root.title("Sem título - Bloco de anotações")
        # Centraliza janela
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        # left-align
        left = (screen_width / 2) - (self.__this_width / 2)
        # right-align
        top = (screen_height / 2) - (self.__this_height / 2)
        # top and botton align
        self.__root.geometry(
            "%dx%d+%d+%d" % (self.__this_width, self.__this_height, left, top)
        )
        # Para fazer o redimensionamento do Textarea
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Adiciona os controles (widget)
        self.__this_text_area.grid(sticky=N + E + S + W)
        # Para abrir um novo arquivo
        self.__this_file_menu.add_command(label="Novo", command=self.__newFile)
        # Para abrir um arquivo já existente
        self.__this_file_menu.add_command(label="Abrir", command=self.__openFile)
        # Para salvar o arquivo
        self.__this_file_menu.add_command(label="Salvar", command=self.__saveFile)
        # Cria nova linha das opções
        self.__this_file_menu.add_separator()
        # Sair do programa
        self.__this_file_menu.add_command(label="Sair", command=self.__quitNotepad)
        # Adiciona as configs para manipular o arquivo no menu bar
        self.__this_menu_bar.add_cascade(label="File", menu=self.__this_file_menu)
        # Recortar
        self.__this_edit_menu.add_command(label="Recortar", command=self.__cut)
        # Copiar
        self.__this_edit_menu.add_command(label="Copiar", command=self.__copy)
        # Colar
        self.__this_edit_menu.add_command(label="Colar", command=self.__paste)
        # Adiciona as configs do editar na menu bar
        self.__this_menu_bar.add_cascade(label="Editar", menu=self.__this_edit_menu)

        # Sobre o programa e creditos
        self.__this_about_menu.add_command(
            label="Sobre", command=self.__applicationAbout
        )
        # Adiciona as configs do sobre no menu bar
        self.__this_menu_bar.add_cascade(label="Sobre", menu=self.__this_about_menu)
        # Aplica as configs na menu bar
        self.__root.config(menu=self.__this_menu_bar)

        # Define a Scrollbar e posição
        self.__this_scroll_bar.pack(side=RIGHT, fill=Y)
        # Ajuste do automatico do Scrollbar dependendo do conteudo
        self.__this_scroll_bar.config(command=self.__this_text_area.yview)
        self.__this_text_area.config(yscrollcommand=self.__this_scroll_bar.set)

    def __quitNotepad(self) -> None:
        """Função para sair do programa"""
        self.__root.destroy()

    def __applicationAbout(self) -> None:
        """Função do sobre o programa"""
        showinfo(title="Notepad - Bloco de anotações", message="Feito por Lucas Turos")

    def __openFile(self) -> None:
        """Função para abrir os arquivos"""
        self.__file = askopenfilename(
            defaultextension=".txt",
            filetypes=[("Todos os arquivos", "*.*"), ("Arquivo .txt", "*.txt")],
        )

        if self.__file == "":
            # Não foi aberto o arquivo
            self.__file = None
        else:
            # Se abriu o arquivo
            self.__root.title(os.path.basename(self.__file) + " - Bloco de anotações")
            self.__this_text_area.delete(1.0, END)
            file_txt = open(self.__file, "r")
            self.__this_text_area.insert(1.0, file_txt.read())
            file_txt.close()

    def __newFile(self) -> None:
        """Função Novo arquivo"""
        self.__root.title("Sem título - Bloco de anotações")
        self.__file = None
        self.__this_text_area.delete(1.0, END)

    def __saveFile(self) -> None:
        """Função para Salvar arquivo"""
        self.__file = asksaveasfilename(
            initialfile="Sem_Titulo.txt",
            defaultextension=".txt",
            filetypes=[("Todos os arquivos", "*.*"), ("Arquivo .txt", "*.txt")],
        )

        if self.__file == "":
            # Não foi salvo o arquivo
            self.__file = None
        else:
            # Salvar
            file_txt = open(self.__file, "w")
            file_txt.write(self.__this_text_area.get(1.0, END))
            file_txt.close()
            self.__root.title(os.path.basename(self.__file) + " - Bloco de anotações")

    def __cut(self) -> None:
        """Função para recortar texto"""
        self.__this_text_area.event_generate("<<Cut>>")

    def __copy(self) -> None:
        """Função para copiar texto"""
        self.__this_text_area.event_generate("<<Copy>>")

    def __paste(self) -> None:
        """Função para colar texto"""
        self.__this_text_area.event_generate("<<Paste>>")

    def run(self) -> None:
        """Executa a aplicação"""
        self.__root.mainloop()
