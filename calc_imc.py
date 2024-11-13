import tkinter as tk
from tkinter import messagebox, Toplevel, filedialog
import csv

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.peso = None
        self.altura = None
        self.imc_historico = []

    def set_peso_altura(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        if self.altura > 0 and self.peso is not None:
            return self.peso / (self.altura ** 2)
        return None

    def adicionar_imc_ao_historico(self, imc):
        self.imc_historico.append(imc)

    def obter_historico(self):
        return self.imc_historico

class JanelaInformacoes:
    def __init__(self, root):
        self.root = root

    def abrir(self):
        nova_janela = Toplevel(self.root)
        nova_janela.title("Informações sobre o IMC")
        nova_janela.geometry("400x300")

        info_text = """
            O Índice de Massa Corporal (IMC) é uma medida usada para avaliar se uma pessoa está dentro
            do peso ideal em relação à sua altura. A fórmula é:
            IMC = Peso (kg) / Altura (m)^2

            Classificação:
            - Abaixo de 18,5: Abaixo do peso
            - Entre 18,5 e 24,9: Peso normal
            - Entre 25,0 e 29,9: Sobrepeso
            - Acima de 30: Obesidade
        """
        label = tk.Label(nova_janela, text=info_text, wraplength=350, justify="left")
        label.pack(pady=10)

        fechar_botao = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        fechar_botao.pack(pady=10)

class JanelaHistorico:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

    def exibir(self):
        nova_janela = Toplevel(self.root)
        nova_janela.title("Histórico de IMC")
        nova_janela.geometry("300x200")

        historico_texto = "\n".join([f"IMC {i+1}: {imc:.2f}" for i, imc in enumerate(self.usuario.obter_historico())])
        label_historico = tk.Label(nova_janela, text=historico_texto)
        label_historico.pack(pady=10)

        fechar_botao = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        fechar_botao.pack(pady=10)

class JanelaSalvarHistorico:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

    def salvar(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Cálculo", "IMC"])
                for i, imc in enumerate(self.usuario.obter_historico()):
                    writer.writerow([f"IMC {i+1}", f"{imc:.2f}"])

class JanelaRecomendacao:
    def __init__(self, root):
        self.root = root

    def mostrar(self, imc):
        if imc < 18.5:
            recomendacao = "Você está abaixo do peso. Consulte um médico ou nutricionista."
        elif 18.5 <= imc <= 24.9:
            recomendacao = "Você está com peso normal. Mantenha um estilo de vida saudável!"
        elif 25 <= imc <= 29.9:
            recomendacao = "Você está com sobrepeso. Considere ajustar sua dieta e atividade física."
        else:
            recomendacao = "Você está com obesidade. É recomendável procurar um profissional de saúde."
        
        messagebox.showinfo("Recomendação", recomendacao)

class AplicacaoIMC:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")
        self.usuario = None

        # Título
        self.lbl_titulo = tk.Label(root, text="Calculadora de IMC", font=("Helvetica", 24, "bold"), bg="#f0f8ff")
        self.lbl_titulo.pack(pady=20)

        # Nome
        self.lbl_nome = tk.Label(root, text="Nome do usuário:", font=("Helvetica", 16), bg="#f0f8ff")
        self.lbl_nome.pack(pady=5)
        self.entry_nome = tk.Entry(root, font=("Helvetica", 16), bd=2, relief=tk.SUNKEN)
        self.entry_nome.pack(pady=5)

        # Peso
        self.lbl_peso = tk.Label(root, text="Peso (kg):", font=("Helvetica", 16), bg="#f0f8ff")
        self.lbl_peso.pack(pady=5)
        self.entry_peso = tk.Entry(root, font=("Helvetica", 16), bd=2, relief=tk.SUNKEN)
        self.entry_peso.pack(pady=5)

        # Altura
        self.lbl_altura = tk.Label(root, text="Altura (m):", font=("Helvetica", 16), bg="#f0f8ff")
        self.lbl_altura.pack(pady=5)
        self.entry_altura = tk.Entry(root, font=("Helvetica", 16), bd=2, relief=tk.SUNKEN)
        self.entry_altura.pack(pady=5)

        # Botões
        self.btn_info = tk.Button(root, text="Info", font=("Helvetica", 16), bg="#f0f8ff", command=self.abrir_informacoes)
        self.btn_info.pack(pady=5)

        self.btn_calcular = tk.Button(root, text="Calcular IMC", command=self.calcular_imc, font=("Helvetica", 16), bg="#4CAF50", fg="white", bd=0, padx=20, pady=10)
        self.btn_calcular.pack(pady=20)

        self.btn_historico = tk.Button(root, text="Exibir Histórico", command=self.exibir_historico, font=("Helvetica", 16), bg="#2196F3", fg="white", bd=0, padx=20, pady=10)
        self.btn_historico.pack(pady=10)

        self.btn_salvar = tk.Button(root, text="Salvar Histórico", command=self.salvar_historico, font=("Helvetica", 16), bg="#FF9800", fg="white", bd=0, padx=20, pady=10)
        self.btn_salvar.pack(pady=10)

        self.btn_peso_ideal = tk.Button(root, text="Calcular Peso Ideal", command=self.calcular_peso_ideal, font=("Helvetica", 16), bg="#009688", fg="white", bd=0, padx=20, pady=10)
        self.btn_peso_ideal.pack(pady=10)

        self.btn_modo = tk.Button(root, text="Modo Claro/Escuro", command=self.alternar_modo, font=("Helvetica", 16), bg="#9E9E9E", fg="white", bd=0, padx=20, pady=10)
        self.btn_modo.pack(pady=10)

    def criar_usuario(self):
        nome = self.entry_nome.get()
        if nome:
            self.usuario = Usuario(nome)
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome de usuário.")

    def abrir_informacoes(self):
        info_janela = JanelaInformacoes(self.root)
        info_janela.abrir()

    def exibir_historico(self):
        if self.usuario:
            historico_janela = JanelaHistorico(self.root, self.usuario)
            historico_janela.exibir()
        else:
            messagebox.showwarning("Erro", "Por favor, crie um usuário primeiro.")

    def salvar_historico(self):
        if self.usuario:
            salvar_janela = JanelaSalvarHistorico(self.root, self.usuario)
            salvar_janela.salvar()
        else:
            messagebox.showwarning("Erro", "Por favor, crie um usuário primeiro.")

    def mostrar_recomendacao(self, imc):
        recomendacao_janela = JanelaRecomendacao(self.root)
        recomendacao_janela.mostrar(imc)

    def calcular_peso_ideal(self):
        try:
            altura = float(self.entry_altura.get())
            if altura > 0:
                peso_min = 18.5 * (altura ** 2)
                peso_max = 24.9 * (altura ** 2)
                messagebox.showinfo("Peso Ideal", f"Seu peso ideal está entre {peso_min:.2f} kg e {peso_max:.2f} kg.")
            else:
                messagebox.showwarning("Erro", "A altura deve ser maior que zero.")
        except ValueError:
            messagebox.showwarning("Erro", "Por favor, insira um valor numérico válido.")

    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            
            if not self.usuario:
                self.criar_usuario()

            if self.usuario:
                self.usuario.set_peso_altura(peso, altura)
                imc = self.usuario.calcular_imc()
                if imc:
                    self.usuario.adicionar_imc_ao_historico(imc)
                    messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}")
                    self.mostrar_recomendacao(imc)  # Exibe recomendação com base no IMC
                else:
                    messagebox.showwarning("Erro", "Valores inválidos para IMC.")
            else:
                messagebox.showwarning("Erro", "Por favor, insira um nome de usuário.")
        
        except ValueError:
            messagebox.showwarning("Erro", "Por favor, insira valores numéricos válidos.")

    def alternar_modo(self):
        if self.root.cget("bg") == "#f0f8ff":  # Modo claro
            self.root.configure(bg="#2c2f33")
            self.lbl_titulo.config(bg="#2c2f33", fg="white")
            self.lbl_peso.config(bg="#2c2f33", fg="white")
            self.lbl_altura.config(bg="#2c2f33", fg="white")
            self.lbl_nome.config(bg="#2c2f33", fg="white")
            self.btn_calcular.config(bg="#4CAF50", fg="white")
            self.btn_historico.config(bg="#2196F3", fg="white")
            self.btn_salvar.config(bg="#FF9800", fg="white")
            self.btn_peso_ideal.config(bg="#009688", fg="white")
            self.btn_modo.config(bg="#9E9E9E", fg="white")
        else:  # Modo escuro
            self.root.configure(bg="#f0f8ff")
            self.lbl_titulo.config(bg="#f0f8ff", fg="black")
            self.lbl_peso.config(bg="#f0f8ff", fg="black")
            self.lbl_altura.config(bg="#f0f8ff", fg="black")
            self.lbl_nome.config(bg="#f0f8ff", fg="black")
            self.btn_calcular.config(bg="#4CAF50", fg="white")
            self.btn_historico.config(bg="#2196F3", fg="white")
            self.btn_salvar.config(bg="#FF9800", fg="white")
            self.btn_peso_ideal.config(bg="#009688", fg="white")
            self.btn_modo.config(bg="#9E9E9E", fg="white")

# Configuração da janela principal
root = tk.Tk()
app = AplicacaoIMC(root)
root.mainloop()
