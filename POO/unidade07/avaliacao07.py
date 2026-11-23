from tkinter import *
from tkinter import messagebox
import urllib.request
import urllib.error
import json


class ConsultarCNPJ(Tk):

    def __init__(self):
        super().__init__()
        self.title("Unidade 07 - Questão Aleatória 01")
        self.geometry("620x330")
        self.resizable(False, False)
        self.configure(bg="#d9d9d9")

        # Rodapé
        self.rodape = Frame(self, bg="black")
        self.rodape.pack(fill="x", side="bottom")

        self.var_situacao = StringVar(value="Situação: Aguardando consulta...")
        Label(self.rodape, textvariable=self.var_situacao, bg="black", fg="white",
              font=("Tahoma", 9, "bold"), anchor="w", padx=10, pady=5).pack(fill="x")

        # Cabeçalho
        header = Frame(self, bg="white", bd=1, relief="solid")
        header.pack(fill="x", padx=10, pady=(10, 6))
        Label(header, text="Consulta Informações de Pessoa Jurídica CNPJ",
              bg="white", fg="black", font=("Tahoma", 12, "bold")).pack()

        # Entrada
        frame_cnpj = Frame(self, bg="#d9d9d9")
        frame_cnpj.pack(fill="x", padx=10, pady=4)
        Label(frame_cnpj, text="Informe CNPJ a Consultar:", bg="#d9d9d9",
              font=("Tahoma", 9)).pack(side="left")

        self.entry_cnpj = Entry(frame_cnpj, font=("Tahoma", 10), width=24)
        self.entry_cnpj.pack(side="left", padx=6)
        self.entry_cnpj.bind("<Return>", lambda e: self.consultar_cnpj())

        # Botão
        self.btn_consultar = Button(self, text="Consultar CNPJ", command=self.consultar_cnpj,
                                    font=("Tahoma", 10, "bold"), bg="#1a73e8", fg="white",
                                    activebackground="#1666cc", activeforeground="white",
                                    relief="raised", cursor="hand2", bd=2, padx=12, pady=3)
        self.btn_consultar.pack(pady=8)

        # Campos de resposta
        frame_res = Frame(self, bg="#d9d9d9")
        frame_res.pack(fill="x", padx=10, pady=4)

        self.campos = {}
        rotulos = [("razao", "Razão Social:"),
                   ("fantasia", "Nome Fantasia:"),
                   ("municipio", "Município:"),
                   ("uf", "Estado UF:")]

        for i, (chave, texto) in enumerate(rotulos):
            Label(frame_res, text=texto, bg="#d9d9d9", font=("Tahoma", 9),
                  anchor="w", width=15).grid(row=i, column=0, sticky="w", pady=3)
            var = StringVar()
            Entry(frame_res, textvariable=var, font=("Tahoma", 10), width=48,
                  state="readonly", readonlybackground="#e8e8e8").grid(
                  row=i, column=1, sticky="we", pady=3)
            self.campos[chave] = var

        frame_res.columnconfigure(1, weight=1)

    def consultar_cnpj(self):
        cnpj = "".join(filter(str.isdigit, self.entry_cnpj.get()))

        self.var_situacao.set("Situação: Consultando...")
        self.update_idletasks()

        try:
            url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                dados = json.loads(response.read().decode("utf-8"))

            self.campos["razao"].set(dados.get("razao_social", ""))
            self.campos["fantasia"].set(dados.get("nome_fantasia", ""))
            self.campos["municipio"].set(dados.get("municipio", ""))
            self.campos["uf"].set(dados.get("uf", ""))

            self.var_situacao.set("Situação: CNPJ OK")

        except urllib.error.HTTPError:
            self.limpar_campos()
            self.var_situacao.set("Situação: CNPJ Inválido")
        except Exception:
            self.limpar_campos()
            self.var_situacao.set("Situação: Erro na consulta")

    def limpar_campos(self):
        for var in self.campos.values():
            var.set("")


if __name__ == "__main__":
    app = ConsultarCNPJ()
    app.mainloop()