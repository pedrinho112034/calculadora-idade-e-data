from datetime import datetime, date, timedelta


def validar_data(data_str, nome_campo):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError(f"Data inválida para {nome_campo}: '{data_str}'. Use o formato dd/mm/aaaa.")


def calcular_idade(data_nascimento):
    hoje = date.today()
    nascimento = validar_data(data_nascimento, "data de nascimento")

    if nascimento > hoje:
        raise ValueError("A data de nascimento não pode ser no futuro.")

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade


def calcular_idade_completa(data_nascimento):
    hoje = date.today()
    nascimento = validar_data(data_nascimento, "data de nascimento")

    if nascimento > hoje:
        raise ValueError("A data de nascimento não pode ser no futuro.")

    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day

    if dias < 0:
        meses -= 1
        ultimo_dia_mes_anterior = (date(hoje.year, hoje.month, 1) - timedelta(days=1)).day
        dias += ultimo_dia_mes_anterior

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias


def dias_para_data_futura(data_futura):
    hoje = datetime.today()
    futura = validar_data(data_futura, "data futura")
    hoje_datetime = datetime.combine(hoje.date(), datetime.min.time())
    diferenca = (datetime.combine(futura, datetime.min.time()) - hoje_datetime).days

    if diferenca < 0:
        return "A data já passou."
    return diferenca


if __name__ == "__main__":
    try:
        nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        data_futura = input("Digite a data futura (dd/mm/aaaa): ")

        anos, meses, dias = calcular_idade_completa(nascimento)
        print(f"Idade: {anos} anos, {meses} meses e {dias} dias")
        print(f"Dias para {data_futura}: {dias_para_data_futura(data_futura)} dias")
    except ValueError as e:
        print(f"Erro: {e}")

