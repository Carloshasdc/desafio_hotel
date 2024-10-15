class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Função: {self.funcao}, Salário: R${self.salario:.2f}"


class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.ocupado = False

    def __str__(self):
        return f"Quarto {self.numero} ({self.tipo}), Preço por diária: R${self.preco_diaria:.2f}, Ocupado: {'Sim' if self.ocupado else 'Não'}"


class Reserva:
    def __init__(self, nome_cliente, quarto, dias):
        self.nome_cliente = nome_cliente
        self.quarto = quarto
        self.dias = dias
        self.valor_total = self.calcular_total()

    def calcular_total(self):
        return self.quarto.preco_diaria * self.dias

    def __str__(self):
        return f"Reserva para {self.nome_cliente}, Quarto {self.quarto.numero}, Dias: {self.dias}, Total: R${self.valor_total:.2f}"


class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, nome, funcao, salario):
        funcionario = Funcionario(nome, funcao, salario)
        self.funcionarios.append(funcionario)

    def adicionar_quarto(self, numero, tipo, preco_diaria):
        quarto = Quarto(numero, tipo, preco_diaria)
        self.quartos.append(quarto)

    def fazer_reserva(self, nome_cliente, numero_quarto, dias):
        quarto = next((q for q in self.quartos if q.numero == numero_quarto and not q.ocupado), None)
        if quarto is not None:
            quarto.ocupado = True
            reserva = Reserva(nome_cliente, quarto, dias)
            self.reservas.append(reserva)
            return reserva
        else:
            return f"Quarto {numero_quarto} não está disponível."

    def listar_funcionarios(self):
        return [str(funcionario) for funcionario in self.funcionarios]

    def listar_quartos(self):
        return [str(quarto) for quarto in self.quartos]

    def listar_reservas(self):
        return [str(reserva) for reserva in self.reservas]

    def calcular_conta(self, numero_quarto):
        reserva = next((r for r in self.reservas if r.quarto.numero == numero_quarto), None)
        if reserva:
            return f"Conta total para o Quarto {numero_quarto}: R${reserva.valor_total:.2f}"
        else:
            return f"Reserva não encontrada para o Quarto {numero_quarto}."

    def __str__(self):
        return f"Hotel: {self.nome}, Funcionários: {len(self.funcionarios)}, Quartos: {len(self.quartos)}, Reservas: {len(self.reservas)}"
 
        

# Criando um hotel
hotel = Hotel("Hotel das Estrelas")

# Adicionando funcionários
hotel.adicionar_funcionario("João", "Gerente", 3000)
hotel.adicionar_funcionario("Maria", "Recepcionista", 1500)

# Adicionando quartos
hotel.adicionar_quarto(101, "Simples", 200)
hotel.adicionar_quarto(102, "Luxo", 350)

# Fazendo reservas
print(hotel.fazer_reserva("Carlos", 101, 3))
print(hotel.fazer_reserva("Ana", 102, 2))

# Listando funcionários
print("\nFuncionários do hotel:")
for f in hotel.listar_funcionarios():
    print(f)

# Listando quartos
print("\nQuartos do hotel:")
for q in hotel.listar_quartos():
    print(q)

# Listando reservas
print("\nReservas do hotel:")
for r in hotel.listar_reservas():
    print(r)

# Calculando a conta de um quarto
print("\nConta para o quarto 101:")
print(hotel.calcular_conta(101))
