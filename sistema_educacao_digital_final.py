"""
Projeto Integrado Multidisciplinar (PIM)
Universidade Paulista - CST em Análise e Desenvolvimento de Sistemas
1º Semestre - 2025

Plataforma de Educação Digital Segura para Inclusão Digital e Proteção de Dados
"""

import json
import os
import hashlib
from datetime import datetime
import statistics
import secrets
import re
from conteudo_cursos import MAPEAMENTO_CURSOS

# Constantes do sistema
ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_CURSOS = "cursos.json"
ARQUIVO_ACESSOS = "acessos.json"
''
# Módulo de Armazenamento de Dados
class GerenciadorDados:
    @staticmethod
    def carregar_dados(arquivo):
        """Carrega dados de um arquivo JSON"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def salvar_dados(arquivo, dados):
        """Salva dados em um arquivo JSON"""
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def registrar_acesso(acessos, usuario_id, acao):
        """Registra um acesso ao sistema para análise estatística"""
        registro = {
            "usuario": usuario_id,
            "acao": acao,
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        acessos.append(registro)
        GerenciadorDados.salvar_dados(ARQUIVO_ACESSOS, acessos)
        return acessos

# Módulo de Autenticação
class GerenciadorAutenticacao:
    @staticmethod
    def gerar_salt():
        """Gera um salt aleatório para uso na criptografia de senhas"""
        return secrets.token_hex(16)

    @staticmethod
    def criptografar_senha(senha, salt):
        """Criptografa a senha usando SHA-256 com salt"""
        senha_com_salt = senha.encode('utf-8') + salt.encode('utf-8')
        return hashlib.sha256(senha_com_salt).hexdigest()

    @staticmethod
    def validar_email(email):
        """Valida o formato do email"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None

    @staticmethod
    def validar_senha(senha):
        """Valida a força da senha"""
        if len(senha) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres!"
        
        # Verificar se a senha contém pelo menos um número e uma letra
        if not (any(c.isdigit() for c in senha) and any(c.isalpha() for c in senha)):
            return False, "A senha deve conter pelo menos um número e uma letra!"
        
        return True, "Senha válida"

    @staticmethod
    def cadastrar_usuario(usuarios, acessos):
        """Cadastra um novo usuário no sistema"""
        print("\n=== Cadastro de Usuário ===")
        
        # Validação do nome de usuário
        while True:
            usuario = input("Nome de usuário: ").strip()
            if not usuario:
                print("O nome de usuário não pode estar vazio!")
                continue
            if usuario in usuarios:
                print("Usuário já existe! Escolha outro nome de usuário.")
                continue
            break
            
        # Validação do nome completo
        while True:
            nome = input("Nome completo: ").strip()
            if not nome:
                print("O nome completo não pode estar vazio!")
                continue
            break
            
        # Validação do email
        while True:
            email = input("E-mail: ").strip()
            if not GerenciadorAutenticacao.validar_email(email):
                print("Formato de e-mail inválido! Por favor, insira um e-mail válido.")
                continue
            break
            
        # Validação da senha
        while True:
            print("Senha (mínimo 8 caracteres, deve conter números e letras): ")
            senha = input()
            valida, mensagem = GerenciadorAutenticacao.validar_senha(senha)
            if not valida:
                print(mensagem)
                continue
                
            print("Confirme a senha: ")
            senha_confirmacao = input()
            if senha != senha_confirmacao:
                print("As senhas não coincidem!")
                continue
                
            break
            
        # Gerar salt único para este usuário
        salt = GerenciadorAutenticacao.gerar_salt()
        
        # Criar o usuário com permissões básicas
        usuarios[usuario] = {
            "nome": nome,
            "senha": GerenciadorAutenticacao.criptografar_senha(senha, salt),
            "salt": salt,
            "email": email,
            "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "cursos_inscritos": [],
            "resultados_exercicios": {},
            "permissoes": ["visualizar_cursos", "inscrever_cursos", "visualizar_estatisticas_basicas"]
        }
        
        GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, usuarios)
        acessos = GerenciadorDados.registrar_acesso(acessos, usuario, "cadastro")
        print("\nCadastro realizado com sucesso!")
        return usuarios, acessos

    @staticmethod
    def login(usuarios, acessos):
        """Realiza o login do usuário"""
        print("\n=== Login ===")
        usuario = input("Usuário: ").strip()
        print("Senha: ")
        senha = input()
        
        if usuario in usuarios:
            salt = usuarios[usuario]["salt"]
            senha_criptografada = GerenciadorAutenticacao.criptografar_senha(senha, salt)
            
            if usuarios[usuario]["senha"] == senha_criptografada:
                acessos = GerenciadorDados.registrar_acesso(acessos, usuario, "login")
                print(f"\nBem-vindo, {usuarios[usuario]['nome']}!")
                return usuario, acessos
            else:
                acessos = GerenciadorDados.registrar_acesso(acessos, usuario, "tentativa_login_falha")
        
        print("\nUsuário ou senha incorretos.")
        return None, acessos

    @staticmethod
    def alterar_senha(usuarios, usuario_logado, acessos):
        """Altera a senha do usuário logado"""
        print("\n=== Alterar Senha ===")
        print("Senha atual: ")
        senha_atual = input()
        salt = usuarios[usuario_logado]["salt"]
        
        if usuarios[usuario_logado]["senha"] != GerenciadorAutenticacao.criptografar_senha(senha_atual, salt):
            print("Senha atual incorreta!")
            return usuarios, acessos
            
        while True:
            print("Nova senha (mínimo 8 caracteres, deve conter números e letras): ")
            nova_senha = input()
            valida, mensagem = GerenciadorAutenticacao.validar_senha(nova_senha)
            if not valida:
                print(mensagem)
                continue
                
            print("Confirme a nova senha: ")
            confirmacao = input()
            if nova_senha != confirmacao:
                print("As senhas não coincidem!")
                continue
                
            break
            
        # Gerar novo salt para aumentar a segurança
        novo_salt = GerenciadorAutenticacao.gerar_salt()
        usuarios[usuario_logado]["salt"] = novo_salt
        usuarios[usuario_logado]["senha"] = GerenciadorAutenticacao.criptografar_senha(nova_senha, novo_salt)
        
        GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, usuarios)
        acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, "alterar_senha")
        print("\nSenha alterada com sucesso!")
        return usuarios, acessos

# Módulo de Cursos
class GerenciadorCursos:
    @staticmethod
    def listar_cursos(cursos, detalhado=False):
        """Lista todos os cursos disponíveis"""
        print("\n=== Cursos Disponíveis ===")
        if not cursos:
            print("Nenhum curso disponível no momento.")
            return
            
        for curso_id, curso in cursos.items():
            print(f"\nID: {curso_id}")
            print(f"Título: {curso['titulo']}")
            print(f"Descrição: {curso['descricao']}")
            
            if detalhado:
                print(f"Módulos: {curso['modulos']}")
                print(f"Nível: {curso['nivel']}")
                print(f"Carga horária: {curso['carga_horaria']} horas")

    @staticmethod
    def adicionar_curso(cursos, usuario_logado, acessos):
        """Adiciona um novo curso ao sistema"""
        print("\n=== Adicionar Curso ===")
        
        # Validação do ID do curso
        while True:
            curso_id = input("ID do curso: ").strip()
            if not curso_id:
                print("O ID do curso não pode estar vazio!")
                continue
            if curso_id in cursos:
                print("Já existe um curso com este ID! Escolha outro ID.")
                continue
            break
            
        # Validação do título
        while True:
            titulo = input("Título: ").strip()
            if not titulo:
                print("O título não pode estar vazio!")
                continue
            break
            
        # Validação da descrição
        while True:
            descricao = input("Descrição: ").strip()
            if not descricao:
                print("A descrição não pode estar vazia!")
                continue
            break
            
        # Validação do número de módulos
        while True:
            try:
                modulos = int(input("Número de módulos: "))
                if modulos <= 0:
                    print("O número de módulos deve ser maior que zero!")
                    continue
                break
            except ValueError:
                print("Por favor, insira um número válido!")
                
        # Validação do nível
        niveis_validos = ["iniciante", "intermediário", "avançado"]
        while True:
            nivel = input("Nível (iniciante/intermediário/avançado): ").strip().lower()
            if nivel not in niveis_validos:
                print(f"Nível inválido! Escolha entre: {', '.join(niveis_validos)}")
                continue
            break
            
        # Validação da carga horária
        while True:
            try:
                carga_horaria = int(input("Carga horária (horas): "))
                if carga_horaria <= 0:
                    print("A carga horária deve ser maior que zero!")
                    continue
                break
            except ValueError:
                print("Por favor, insira um número válido!")
        
        cursos[curso_id] = {
            "titulo": titulo,
            "descricao": descricao,
            "modulos": modulos,
            "nivel": nivel,
            "carga_horaria": carga_horaria
        }
        
        GerenciadorDados.salvar_dados(ARQUIVO_CURSOS, cursos)
        acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"adicionar_curso_{curso_id}")
        print("\nCurso adicionado com sucesso!")
        return cursos, acessos

    @staticmethod
    def remover_curso(cursos, usuarios, usuario_logado, acessos):
        """Remove um curso do sistema"""
        print("\n=== Remover Curso ===")
        
        if not cursos:
            print("Não há cursos para remover.")
            return cursos, usuarios, acessos
            
        GerenciadorCursos.listar_cursos(cursos)
        curso_id = input("\nID do curso a ser removido: ").strip()
        
        if curso_id in cursos:
            # Confirmação para evitar remoções acidentais
            confirmacao = input(f"Tem certeza que deseja remover o curso '{cursos[curso_id]['titulo']}'? (s/n): ").strip().lower()
            if confirmacao != 's':
                print("Operação cancelada.")
                return cursos, usuarios, acessos
                
            del cursos[curso_id]
            GerenciadorDados.salvar_dados(ARQUIVO_CURSOS, cursos)
            
            # Remove o curso das inscrições de todos os usuários
            for usuario in usuarios.values():
                if "cursos_inscritos" in usuario and curso_id in usuario["cursos_inscritos"]:
                    usuario["cursos_inscritos"].remove(curso_id)
                # Remove também os resultados de exercícios deste curso
                if "resultados_exercicios" in usuario and curso_id in usuario["resultados_exercicios"]:
                    del usuario["resultados_exercicios"][curso_id]
            
            GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, usuarios)
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"remover_curso_{curso_id}")
            print("\nCurso removido com sucesso!")
        else:
            print("Curso não encontrado!")
            
        return cursos, usuarios, acessos

    @staticmethod
    def inscrever_curso(cursos, usuarios, usuario_logado, acessos):
        """Inscreve o usuário em um curso"""
        print("\n=== Inscrever-se em Curso ===")
        
        if not cursos:
            print("Não há cursos disponíveis para inscrição.")
            return usuarios, acessos
            
        # Mostrar apenas cursos em que o usuário não está inscrito
        cursos_disponiveis = {}
        for curso_id, curso in cursos.items():
            if curso_id not in usuarios[usuario_logado].get("cursos_inscritos", []):
                cursos_disponiveis[curso_id] = curso
                
        if not cursos_disponiveis:
            print("Você já está inscrito em todos os cursos disponíveis!")
            return usuarios, acessos
            
        print("\n=== Cursos Disponíveis para Inscrição ===")
        for curso_id, curso in cursos_disponiveis.items():
            print(f"\nID: {curso_id}")
            print(f"Título: {curso['titulo']}")
            print(f"Descrição: {curso['descricao']}")
            print(f"Nível: {curso['nivel']}")
            print(f"Carga horária: {curso['carga_horaria']} horas")
            
        curso_id = input("\nDigite o ID do curso para se inscrever (ou 0 para cancelar): ").strip()
        
        if curso_id == "0":
            print("Operação cancelada.")
            return usuarios, acessos
            
        if curso_id in cursos_disponiveis:
            if "cursos_inscritos" not in usuarios[usuario_logado]:
                usuarios[usuario_logado]["cursos_inscritos"] = []
                
            usuarios[usuario_logado]["cursos_inscritos"].append(curso_id)
            GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, usuarios)
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"inscricao_curso_{curso_id}")
            print(f"\nInscrição realizada com sucesso no curso '{cursos[curso_id]['titulo']}'!")
        else:
            print("Curso não encontrado ou você já está inscrito nele!")
            
        return usuarios, acessos

    @staticmethod
    def meus_cursos(cursos, usuarios, usuario_logado):
        """Mostra os cursos em que o usuário está inscrito"""
        print("\n=== Meus Cursos ===")
        
        cursos_inscritos = usuarios[usuario_logado].get("cursos_inscritos", [])
        
        if not cursos_inscritos:
            print("Você não está inscrito em nenhum curso.")
            return
            
        for curso_id in cursos_inscritos:
            if curso_id in cursos:
                curso = cursos[curso_id]
                print(f"\nID: {curso_id}")
                print(f"Título: {curso['titulo']}")
                print(f"Descrição: {curso['descricao']}")
                print(f"Módulos: {curso['modulos']}")
                print(f"Nível: {curso['nivel']}")
                print(f"Carga horária: {curso['carga_horaria']} horas")
                
                # Mostrar resultado do exercício se o usuário já realizou
                if "resultados_exercicios" in usuarios[usuario_logado] and curso_id in usuarios[usuario_logado]["resultados_exercicios"]:
                    resultado = usuarios[usuario_logado]["resultados_exercicios"][curso_id]
                    print(f"Nota: {resultado['nota']}/10")
                    print(f"Acertos: {resultado['acertos']}/5")
                    print(f"Data de realização: {resultado['data_realizacao']}")

    @staticmethod
    def visualizar_conteudo_curso(cursos, usuarios, usuario_logado, acessos):
        """Permite visualizar o conteúdo de um curso"""
        print("\n=== Visualizar Conteúdo de Curso ===")
        
        cursos_inscritos = usuarios[usuario_logado].get("cursos_inscritos", [])
        
        if not cursos_inscritos:
            print("Você não está inscrito em nenhum curso.")
            return acessos
            
        # Listar cursos inscritos
        print("Seus cursos:")
        for i, curso_id in enumerate(cursos_inscritos, 1):
            if curso_id in cursos:
                print(f"{i}. {cursos[curso_id]['titulo']}")
                
        try:
            escolha = int(input("\nEscolha o número do curso para visualizar o conteúdo (ou 0 para voltar): "))
            if escolha == 0:
                return acessos
                
            if 1 <= escolha <= len(cursos_inscritos):
                curso_id = cursos_inscritos[escolha - 1]
                
                # Verificar se o curso tem conteúdo disponível
                if curso_id not in MAPEAMENTO_CURSOS:
                    print("Este curso ainda não possui conteúdo disponível.")
                    return acessos
                    
                conteudo = MAPEAMENTO_CURSOS[curso_id]["conteudo"]
                
                while True:
                    print(f"\n=== Conteúdo do Curso: {cursos[curso_id]['titulo']} ===")
                    print("Tópicos disponíveis:")
                    
                    # Listar tópicos
                    for i, (topico_id, topico) in enumerate(conteudo.items(), 1):
                        print(f"{i}. {topico['titulo']}")
                        
                    print(f"{len(conteudo) + 1}. Voltar")
                    
                    try:
                        escolha_topico = int(input("\nEscolha o número do tópico para visualizar: "))
                        
                        if escolha_topico == len(conteudo) + 1:
                            break
                            
                        if 1 <= escolha_topico <= len(conteudo):
                            topico_id = list(conteudo.keys())[escolha_topico - 1]
                            topico = conteudo[topico_id]
                            
                            print(f"\n=== {topico['titulo']} ===")
                            print(topico['conteudo'])
                            
                            input("\nPressione Enter para continuar...")
                            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"visualizar_topico_{curso_id}_{topico_id}")
                        else:
                            print("Opção inválida!")
                    except ValueError:
                        print("Por favor, digite um número válido!")
                
                acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"visualizar_conteudo_{curso_id}")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")
            
        return acessos

    @staticmethod
    def realizar_exercicios(cursos, usuarios, usuario_logado, acessos):
        """Permite ao usuário realizar os exercícios de um curso"""
        print("\n=== Realizar Exercícios ===")
        
        cursos_inscritos = usuarios[usuario_logado].get("cursos_inscritos", [])
        
        if not cursos_inscritos:
            print("Você não está inscrito em nenhum curso.")
            return usuarios, acessos
            
        # Listar cursos inscritos
        print("Seus cursos:")
        for i, curso_id in enumerate(cursos_inscritos, 1):
            if curso_id in cursos:
                print(f"{i}. {cursos[curso_id]['titulo']}")
                
                # Mostrar se já realizou os exercícios
                if "resultados_exercicios" in usuarios[usuario_logado] and curso_id in usuarios[usuario_logado]["resultados_exercicios"]:
                    print(f"   (Exercícios já realizados - Nota: {usuarios[usuario_logado]['resultados_exercicios'][curso_id]['nota']}/10)")
                
        try:
            escolha = int(input("\nEscolha o número do curso para realizar os exercícios (ou 0 para voltar): "))
            if escolha == 0:
                return usuarios, acessos
                
            if 1 <= escolha <= len(cursos_inscritos):
                curso_id = cursos_inscritos[escolha - 1]
                
                # Verificar se o curso tem exercícios disponíveis
                if curso_id not in MAPEAMENTO_CURSOS:
                    print("Este curso ainda não possui exercícios disponíveis.")
                    return usuarios, acessos
                    
                # Verificar se o usuário já realizou os exercícios
                if "resultados_exercicios" in usuarios[usuario_logado] and curso_id in usuarios[usuario_logado]["resultados_exercicios"]:
                    refazer = input("Você já realizou estes exercícios. Deseja refazê-los? (s/n): ").strip().lower()
                    if refazer != 's':
                        return usuarios, acessos
                
                exercicios = MAPEAMENTO_CURSOS[curso_id]["exercicios"]
                
                print(f"\n=== Exercícios do Curso: {cursos[curso_id]['titulo']} ===")
                print("Você responderá a 5 questões de múltipla escolha.")
                print("Cada acerto vale 2 pontos, totalizando 10 pontos possíveis.")
                input("Pressione Enter para começar...")
                
                respostas = []
                acertos = 0
                
                for i, exercicio in enumerate(exercicios, 1):
                    print(f"\nQuestão {i}: {exercicio['pergunta']}")
                    
                    for j, opcao in enumerate(exercicio['opcoes'], 0):
                        print(f"{j}. {opcao}")
                        
                    while True:
                        try:
                            resposta = int(input("\nSua resposta (0-3): "))
                            if 0 <= resposta <= 3:
                                break
                            else:
                                print("Por favor, escolha uma opção entre 0 e 3.")
                        except ValueError:
                            print("Por favor, digite um número válido!")
                    
                    respostas.append(resposta)
                    
                    if resposta == exercicio['resposta_correta']:
                        acertos += 1
                        print("Resposta correta!")
                    else:
                        print(f"Resposta incorreta. A resposta correta é: {exercicio['resposta_correta']}. {exercicio['opcoes'][exercicio['resposta_correta']]}")
                
                nota = acertos * 2  # Cada acerto vale 2 pontos
                
                print(f"\n=== Resultado ===")
                print(f"Acertos: {acertos}/5")
                print(f"Nota final: {nota}/10")
                
                # Salvar resultado
                if "resultados_exercicios" not in usuarios[usuario_logado]:
                    usuarios[usuario_logado]["resultados_exercicios"] = {}
                    
                usuarios[usuario_logado]["resultados_exercicios"][curso_id] = {
                    "data_realizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "respostas": respostas,
                    "acertos": acertos,
                    "nota": nota
                }
                
                GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, usuarios)
                acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, f"realizar_exercicios_{curso_id}")
                
                print("\nSeus resultados foram salvos com sucesso!")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")
            
        return usuarios, acessos

# Módulo de Estatísticas e Relatórios
class GerenciadorEstatisticas:
    @staticmethod
    def visualizar_estatisticas(usuarios, cursos, acessos):
        """Exibe estatísticas básicas do sistema"""
        print("\n=== Estatísticas do Sistema ===")
        
        # Estatísticas de usuários
        total_usuarios = len(usuarios)
        
        print(f"\nTotal de usuários: {total_usuarios}")
        
        # Estatísticas de cursos
        total_cursos = len(cursos)
        cursos_por_nivel = {}
        for curso in cursos.values():
            nivel = curso["nivel"]
            cursos_por_nivel[nivel] = cursos_por_nivel.get(nivel, 0) + 1
        
        print(f"\nTotal de cursos: {total_cursos}")
        for nivel, quantidade in cursos_por_nivel.items():
            print(f"Cursos nível {nivel}: {quantidade}")
        
        # Estatísticas de acessos
        if acessos:
            acessos_por_tipo = {}
            for acesso in acessos:
                tipo = acesso["acao"]
                acessos_por_tipo[tipo] = acessos_por_tipo.get(tipo, 0) + 1
            
            print("\nAcessos ao sistema:")
            for tipo, quantidade in acessos_por_tipo.items():
                print(f"{tipo}: {quantidade}")
            
            # Cálculo de média, moda e mediana de acessos por dia
            acessos_por_data = {}
            for acesso in acessos:
                data = acesso["data_hora"].split()[0]  # Pega apenas a data
                acessos_por_data[data] = acessos_por_data.get(data, 0) + 1
            
            acessos_diarios = list(acessos_por_data.values())
            
            if acessos_diarios:
                print("\nEstatísticas de acessos diários:")
                print(f"Média: {statistics.mean(acessos_diarios):.2f}")
                try:
                    print(f"Moda: {statistics.mode(acessos_diarios)}")
                except statistics.StatisticsError:
                    print("Moda: Múltiplos valores")
                print(f"Mediana: {statistics.median(acessos_diarios)}")
        else:
            print("\nNenhum registro de acesso encontrado.")
            
        # Estatísticas de notas dos exercícios
        notas = []
        for usuario in usuarios.values():
            if "resultados_exercicios" in usuario:
                for resultado in usuario["resultados_exercicios"].values():
                    notas.append(resultado["nota"])
        
        if notas:
            print("\nEstatísticas de notas dos exercícios:")
            print(f"Total de exercícios realizados: {len(notas)}")
            print(f"Média: {statistics.mean(notas):.2f}")
            try:
                print(f"Moda: {statistics.mode(notas)}")
            except statistics.StatisticsError:
                print("Moda: Múltiplos valores")
            print(f"Mediana: {statistics.median(notas)}")
            print(f"Nota mais alta: {max(notas)}")
            print(f"Nota mais baixa: {min(notas)}")

    @staticmethod
    def gerar_relatorio_usuarios(usuarios, usuario_logado, acessos):
        """Gera um relatório de usuários em arquivo TXT"""
        data_atual = datetime.now().strftime("%Y%m%d")
        nome_arquivo = f"relatorio_usuarios_{data_atual}.txt"
        
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("=== Relatório de Usuários ===\n")
                f.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                total_usuarios = len(usuarios)
                
                f.write(f"Total de usuários: {total_usuarios}\n\n")
                f.write("Lista de usuários:\n")
                
                for usuario_id, dados in usuarios.items():
                    f.write(f"\nUsuário: {usuario_id}\n")
                    f.write(f"Nome: {dados['nome']}\n")
                    f.write(f"E-mail: {dados['email']}\n")
                    f.write(f"Data de cadastro: {dados['data_cadastro']}\n")
                    
                    if "cursos_inscritos" in dados and dados["cursos_inscritos"]:
                        f.write(f"Cursos inscritos: {len(dados['cursos_inscritos'])}\n")
                    else:
                        f.write("Cursos inscritos: 0\n")
                        
                    if "resultados_exercicios" in dados and dados["resultados_exercicios"]:
                        f.write("Resultados de exercícios:\n")
                        for curso_id, resultado in dados["resultados_exercicios"].items():
                            f.write(f"  Curso ID {curso_id}: Nota {resultado['nota']}/10, Acertos {resultado['acertos']}/5, Data: {resultado['data_realizacao']}\n")
            
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, "gerar_relatorio_usuarios")
            print(f"\nRelatório de usuários gerado com sucesso: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {str(e)}")
            
        return acessos

    @staticmethod
    def gerar_relatorio_cursos(cursos, usuarios, usuario_logado, acessos):
        """Gera um relatório de cursos em arquivo TXT"""
        data_atual = datetime.now().strftime("%Y%m%d")
        nome_arquivo = f"relatorio_cursos_{data_atual}.txt"
        
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("=== Relatório de Cursos ===\n")
                f.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                total_cursos = len(cursos)
                
                f.write(f"Total de cursos: {total_cursos}\n\n")
                
                if total_cursos > 0:
                    # Estatísticas por nível
                    cursos_por_nivel = {}
                    for curso in cursos.values():
                        nivel = curso["nivel"]
                        cursos_por_nivel[nivel] = cursos_por_nivel.get(nivel, 0) + 1
                    
                    f.write("Cursos por nível:\n")
                    for nivel, quantidade in cursos_por_nivel.items():
                        f.write(f"{nivel}: {quantidade}\n")
                    
                    # Estatísticas de inscrições
                    inscricoes_por_curso = {}
                    for usuario in usuarios.values():
                        if "cursos_inscritos" in usuario:
                            for curso_id in usuario["cursos_inscritos"]:
                                inscricoes_por_curso[curso_id] = inscricoes_por_curso.get(curso_id, 0) + 1
                    
                    f.write("\nInscrições por curso:\n")
                    for curso_id, quantidade in inscricoes_por_curso.items():
                        if curso_id in cursos:
                            f.write(f"{cursos[curso_id]['titulo']} (ID: {curso_id}): {quantidade} inscritos\n")
                    
                    # Estatísticas de notas por curso
                    notas_por_curso = {}
                    for usuario in usuarios.values():
                        if "resultados_exercicios" in usuario:
                            for curso_id, resultado in usuario["resultados_exercicios"].items():
                                if curso_id not in notas_por_curso:
                                    notas_por_curso[curso_id] = []
                                notas_por_curso[curso_id].append(resultado["nota"])
                    
                    f.write("\nEstatísticas de notas por curso:\n")
                    for curso_id, notas in notas_por_curso.items():
                        if curso_id in cursos:
                            f.write(f"{cursos[curso_id]['titulo']} (ID: {curso_id}):\n")
                            f.write(f"  Total de avaliações: {len(notas)}\n")
                            f.write(f"  Média: {statistics.mean(notas):.2f}\n")
                            try:
                                f.write(f"  Moda: {statistics.mode(notas)}\n")
                            except statistics.StatisticsError:
                                f.write("  Moda: Múltiplos valores\n")
                            f.write(f"  Mediana: {statistics.median(notas)}\n")
                            f.write(f"  Nota mais alta: {max(notas)}\n")
                            f.write(f"  Nota mais baixa: {min(notas)}\n\n")
                    
                    f.write("\nLista de cursos:\n")
                    for curso_id, curso in cursos.items():
                        f.write(f"\nID: {curso_id}\n")
                        f.write(f"Título: {curso['titulo']}\n")
                        f.write(f"Descrição: {curso['descricao']}\n")
                        f.write(f"Módulos: {curso['modulos']}\n")
                        f.write(f"Nível: {curso['nivel']}\n")
                        f.write(f"Carga horária: {curso['carga_horaria']} horas\n")
                else:
                    f.write("Não há cursos cadastrados no sistema.\n")
            
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, "gerar_relatorio_cursos")
            print(f"\nRelatório de cursos gerado com sucesso: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {str(e)}")
            
        return acessos

    @staticmethod
    def gerar_relatorio_acessos(acessos, usuario_logado):
        """Gera um relatório de acessos em arquivo TXT"""
        data_atual = datetime.now().strftime("%Y%m%d")
        nome_arquivo = f"relatorio_acessos_{data_atual}.txt"
        
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("=== Relatório de Acessos ===\n")
                f.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                total_acessos = len(acessos)
                
                f.write(f"Total de acessos: {total_acessos}\n\n")
                
                if total_acessos > 0:
                    # Estatísticas por tipo de acesso
                    acessos_por_tipo = {}
                    for acesso in acessos:
                        tipo = acesso["acao"]
                        acessos_por_tipo[tipo] = acessos_por_tipo.get(tipo, 0) + 1
                    
                    f.write("Acessos por tipo:\n")
                    for tipo, quantidade in acessos_por_tipo.items():
                        f.write(f"{tipo}: {quantidade}\n")
                    
                    # Estatísticas por data
                    acessos_por_data = {}
                    for acesso in acessos:
                        data = acesso["data_hora"].split()[0]  # Pega apenas a data
                        acessos_por_data[data] = acessos_por_data.get(data, 0) + 1
                    
                    f.write("\nAcessos por data:\n")
                    for data, quantidade in acessos_por_data.items():
                        f.write(f"{data}: {quantidade}\n")
                    
                    # Últimos 10 acessos
                    f.write("\nÚltimos 10 acessos:\n")
                    for acesso in acessos[-10:]:
                        f.write(f"Usuário: {acesso['usuario']}, Ação: {acesso['acao']}, Data/Hora: {acesso['data_hora']}\n")
                else:
                    f.write("Não há registros de acesso no sistema.\n")
            
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, "gerar_relatorio_acessos")
            print(f"\nRelatório de acessos gerado com sucesso: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {str(e)}")
            
        return acessos

    @staticmethod
    def gerar_relatorio_notas(usuarios, usuario_logado, acessos):
        """Gera um relatório detalhado de notas dos exercícios"""
        data_atual = datetime.now().strftime("%Y%m%d")
        nome_arquivo = f"relatorio_notas_{data_atual}.txt"
        
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write("=== Relatório de Notas dos Exercícios ===\n")
                f.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                # Coletar todas as notas
                todas_notas = []
                notas_por_usuario = {}
                
                for usuario_id, usuario in usuarios.items():
                    if "resultados_exercicios" in usuario and usuario["resultados_exercicios"]:
                        notas_usuario = []
                        
                        for curso_id, resultado in usuario["resultados_exercicios"].items():
                            todas_notas.append(resultado["nota"])
                            notas_usuario.append(resultado["nota"])
                        
                        if notas_usuario:
                            notas_por_usuario[usuario_id] = notas_usuario
                
                # Estatísticas gerais
                if todas_notas:
                    f.write("Estatísticas gerais:\n")
                    f.write(f"Total de avaliações: {len(todas_notas)}\n")
                    f.write(f"Média geral: {statistics.mean(todas_notas):.2f}\n")
                    try:
                        f.write(f"Moda: {statistics.mode(todas_notas)}\n")
                    except statistics.StatisticsError:
                        f.write("Moda: Múltiplos valores\n")
                    f.write(f"Mediana: {statistics.median(todas_notas)}\n")
                    f.write(f"Nota mais alta: {max(todas_notas)}\n")
                    f.write(f"Nota mais baixa: {min(todas_notas)}\n\n")
                    
                    # Distribuição de notas
                    distribuicao = {0: 0, 2: 0, 4: 0, 6: 0, 8: 0, 10: 0}
                    for nota in todas_notas:
                        distribuicao[nota] = distribuicao.get(nota, 0) + 1
                    
                    f.write("Distribuição de notas:\n")
                    for nota, quantidade in distribuicao.items():
                        f.write(f"Nota {nota}: {quantidade} ocorrências\n")
                    
                    # Estatísticas por usuário
                    f.write("\nEstatísticas por usuário:\n")
                    for usuario_id, notas in notas_por_usuario.items():
                        f.write(f"\nUsuário: {usuario_id} ({usuarios[usuario_id]['nome']})\n")
                        f.write(f"  Total de avaliações: {len(notas)}\n")
                        f.write(f"  Média: {statistics.mean(notas):.2f}\n")
                        try:
                            f.write(f"  Moda: {statistics.mode(notas)}\n")
                        except statistics.StatisticsError:
                            f.write("  Moda: Múltiplos valores\n")
                        f.write(f"  Mediana: {statistics.median(notas)}\n")
                        f.write(f"  Nota mais alta: {max(notas)}\n")
                        f.write(f"  Nota mais baixa: {min(notas)}\n")
                        
                        # Detalhes dos resultados
                        f.write("  Detalhes dos resultados:\n")
                        for curso_id, resultado in usuarios[usuario_id]["resultados_exercicios"].items():
                            f.write(f"    Curso ID {curso_id}: Nota {resultado['nota']}/10, Acertos {resultado['acertos']}/5, Data: {resultado['data_realizacao']}\n")
                else:
                    f.write("Não há registros de notas no sistema.\n")
            
            acessos = GerenciadorDados.registrar_acesso(acessos, usuario_logado, "gerar_relatorio_notas")
            print(f"\nRelatório de notas gerado com sucesso: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao gerar relatório: {str(e)}")
            
        return acessos

# Módulo Principal
class SistemaEducacaoDigital:
    def __init__(self):
        """Inicializa o sistema, carregando os dados dos arquivos JSON"""
        self.usuarios = GerenciadorDados.carregar_dados(ARQUIVO_USUARIOS)
        self.cursos = GerenciadorDados.carregar_dados(ARQUIVO_CURSOS)
        self.acessos = GerenciadorDados.carregar_dados(ARQUIVO_ACESSOS)
        self.usuario_logado = None
        
        # Se os arquivos não existirem, cria estruturas vazias
        if not self.usuarios:
            self.usuarios = {}
            GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, self.usuarios)
            
        if not self.cursos:
            self.cursos = {
                "1": {
                    "titulo": "Introdução ao Pensamento Computacional",
                    "descricao": "Curso básico sobre lógica de programação",
                    "modulos": 5,
                    "nivel": "iniciante",
                    "carga_horaria": 20
                },
                "2": {
                    "titulo": "Segurança Digital para Iniciantes",
                    "descricao": "Aprenda boas práticas de segurança na internet",
                    "modulos": 4,
                    "nivel": "iniciante",
                    "carga_horaria": 15
                },
                "3": {
                    "titulo": "Introdução ao Python",
                    "descricao": "Aprenda os fundamentos da linguagem Python",
                    "modulos": 5,
                    "nivel": "iniciante",
                    "carga_horaria": 25
                }
            }
            GerenciadorDados.salvar_dados(ARQUIVO_CURSOS, self.cursos)
            
        if not self.acessos:
            self.acessos = []
            GerenciadorDados.salvar_dados(ARQUIVO_ACESSOS, self.acessos)

    def visualizar_dados(self):
        """Mostra os dados do usuário logado"""
        usuario = self.usuarios[self.usuario_logado]
        print("\n=== Meus Dados ===")
        print(f"Nome: {usuario['nome']}")
        print(f"Usuário: {self.usuario_logado}")
        print(f"E-mail: {usuario['email']}")
        print(f"Data de cadastro: {usuario['data_cadastro']}")
        
        if "cursos_inscritos" in usuario and usuario["cursos_inscritos"]:
            print("\nCursos inscritos:")
            for curso_id in usuario["cursos_inscritos"]:
                if curso_id in self.cursos:
                    print(f"- {self.cursos[curso_id]['titulo']}")
                    
        if "resultados_exercicios" in usuario and usuario["resultados_exercicios"]:
            print("\nResultados de exercícios:")
            for curso_id, resultado in usuario["resultados_exercicios"].items():
                if curso_id in self.cursos:
                    print(f"- {self.cursos[curso_id]['titulo']}: Nota {resultado['nota']}/10, Acertos {resultado['acertos']}/5")
                    print(f"  Data de realização: {resultado['data_realizacao']}")

    def gerenciar_permissoes(self):
        """Gerencia as permissões dos usuários"""
        if "gerenciar_permissoes" not in self.usuarios[self.usuario_logado].get("permissoes", []):
            print("\nVocê não tem permissão para acessar esta funcionalidade.")
            return
            
        print("\n=== Gerenciar Permissões ===")
        print("1. Listar usuários e suas permissões")
        print("2. Adicionar permissão a um usuário")
        print("3. Remover permissão de um usuário")
        print("4. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            self.listar_permissoes_usuarios()
        elif opcao == "2":
            self.adicionar_permissao()
        elif opcao == "3":
            self.remover_permissao()
        elif opcao == "4":
            return
        else:
            print("Opção inválida!")

    def listar_permissoes_usuarios(self):
        """Lista todos os usuários e suas permissões"""
        print("\n=== Lista de Usuários e Permissões ===")
        for usuario_id, dados in self.usuarios.items():
            print(f"\nUsuário: {usuario_id}")
            print(f"Nome: {dados['nome']}")
            
            permissoes = dados.get("permissoes", [])
            if permissoes:
                print("Permissões:")
                for permissao in permissoes:
                    print(f"- {permissao}")
            else:
                print("Sem permissões específicas.")

    def adicionar_permissao(self):
        """Adiciona uma permissão a um usuário"""
        print("\n=== Adicionar Permissão ===")
        
        # Lista de todas as permissões disponíveis
        permissoes_disponiveis = [
            "visualizar_cursos", 
            "inscrever_cursos", 
            "visualizar_estatisticas_basicas",
            "adicionar_cursos",
            "remover_cursos",
            "gerar_relatorios",
            "visualizar_estatisticas_avancadas",
            "gerenciar_permissoes"
        ]
        
        # Listar usuários
        print("Usuários disponíveis:")
        for usuario_id, dados in self.usuarios.items():
            print(f"- {usuario_id} ({dados['nome']})")
            
        usuario_id = input("\nDigite o ID do usuário: ").strip()
        
        if usuario_id not in self.usuarios:
            print("Usuário não encontrado!")
            return
            
        # Listar permissões disponíveis que o usuário ainda não possui
        permissoes_atuais = self.usuarios[usuario_id].get("permissoes", [])
        permissoes_para_adicionar = [p for p in permissoes_disponiveis if p not in permissoes_atuais]
        
        if not permissoes_para_adicionar:
            print("O usuário já possui todas as permissões disponíveis!")
            return
            
        print("\nPermissões disponíveis para adicionar:")
        for i, permissao in enumerate(permissoes_para_adicionar, 1):
            print(f"{i}. {permissao}")
            
        try:
            indice = int(input("\nDigite o número da permissão a adicionar: "))
            if 1 <= indice <= len(permissoes_para_adicionar):
                permissao = permissoes_para_adicionar[indice - 1]
                
                if "permissoes" not in self.usuarios[usuario_id]:
                    self.usuarios[usuario_id]["permissoes"] = []
                    
                self.usuarios[usuario_id]["permissoes"].append(permissao)
                GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, self.usuarios)
                self.acessos = GerenciadorDados.registrar_acesso(self.acessos, self.usuario_logado, f"adicionar_permissao_{permissao}_para_{usuario_id}")
                print(f"\nPermissão '{permissao}' adicionada com sucesso para o usuário '{usuario_id}'!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

    def remover_permissao(self):
        """Remove uma permissão de um usuário"""
        print("\n=== Remover Permissão ===")
        
        # Listar usuários
        print("Usuários disponíveis:")
        for usuario_id, dados in self.usuarios.items():
            print(f"- {usuario_id} ({dados['nome']})")
            
        usuario_id = input("\nDigite o ID do usuário: ").strip()
        
        if usuario_id not in self.usuarios:
            print("Usuário não encontrado!")
            return
            
        # Listar permissões atuais do usuário
        permissoes_atuais = self.usuarios[usuario_id].get("permissoes", [])
        
        if not permissoes_atuais:
            print("O usuário não possui permissões para remover!")
            return
            
        print("\nPermissões atuais do usuário:")
        for i, permissao in enumerate(permissoes_atuais, 1):
            print(f"{i}. {permissao}")
            
        try:
            indice = int(input("\nDigite o número da permissão a remover: "))
            if 1 <= indice <= len(permissoes_atuais):
                permissao = permissoes_atuais[indice - 1]
                
                # Não permitir remover permissões básicas
                permissoes_basicas = ["visualizar_cursos", "inscrever_cursos", "visualizar_estatisticas_basicas"]
                if permissao in permissoes_basicas:
                    print("Não é possível remover permissões básicas!")
                    return
                    
                self.usuarios[usuario_id]["permissoes"].remove(permissao)
                GerenciadorDados.salvar_dados(ARQUIVO_USUARIOS, self.usuarios)
                self.acessos = GerenciadorDados.registrar_acesso(self.acessos, self.usuario_logado, f"remover_permissao_{permissao}_de_{usuario_id}")
                print(f"\nPermissão '{permissao}' removida com sucesso do usuário '{usuario_id}'!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

    def gerar_relatorios(self):
        """Menu para geração de relatórios"""
        if "gerar_relatorios" not in self.usuarios[self.usuario_logado].get("permissoes", []):
            print("\nVocê não tem permissão para acessar esta funcionalidade.")
            return
            
        print("\n=== Gerar Relatórios ===")
        print("1. Relatório de usuários")
        print("2. Relatório de cursos")
        print("3. Relatório de acessos")
        print("4. Relatório de notas")
        print("5. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            self.acessos = GerenciadorEstatisticas.gerar_relatorio_usuarios(self.usuarios, self.usuario_logado, self.acessos)
        elif opcao == "2":
            self.acessos = GerenciadorEstatisticas.gerar_relatorio_cursos(self.cursos, self.usuarios, self.usuario_logado, self.acessos)
        elif opcao == "3":
            self.acessos = GerenciadorEstatisticas.gerar_relatorio_acessos(self.acessos, self.usuario_logado)
        elif opcao == "4":
            self.acessos = GerenciadorEstatisticas.gerar_relatorio_notas(self.usuarios, self.usuario_logado, self.acessos)
        elif opcao == "5":
            return
        else:
            print("Opção inválida!")

    def gerenciar_cursos(self):
        """Menu para gerenciamento de cursos"""
        print("\n=== Gerenciar Cursos ===")
        print("1. Listar todos os cursos")
        print("2. Adicionar curso")
        print("3. Remover curso")
        print("4. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            GerenciadorCursos.listar_cursos(self.cursos, detalhado=True)
        elif opcao == "2":
            if "adicionar_cursos" not in self.usuarios[self.usuario_logado].get("permissoes", []):
                print("\nVocê não tem permissão para adicionar cursos.")
                return
            self.cursos, self.acessos = GerenciadorCursos.adicionar_curso(self.cursos, self.usuario_logado, self.acessos)
        elif opcao == "3":
            if "remover_cursos" not in self.usuarios[self.usuario_logado].get("permissoes", []):
                print("\nVocê não tem permissão para remover cursos.")
                return
            self.cursos, self.usuarios, self.acessos = GerenciadorCursos.remover_curso(self.cursos, self.usuarios, self.usuario_logado, self.acessos)
        elif opcao == "4":
            return
        else:
            print("Opção inválida!")

    def menu_usuario(self):
        """Menu do usuário"""
        while True:
            print("\n=== Menu do Usuário ===")
            print("1. Meus cursos")
            print("2. Inscrever-se em curso")
            print("3. Visualizar conteúdo de curso")
            print("4. Realizar exercícios")
            print("5. Alterar senha")
            print("6. Visualizar meus dados")
            print("7. Visualizar estatísticas")
            
            # Opções adicionais baseadas em permissões
            permissoes = self.usuarios[self.usuario_logado].get("permissoes", [])
            opcoes_avancadas = []
            
            if any(p in permissoes for p in ["adicionar_cursos", "remover_cursos"]):
                opcoes_avancadas.append(("8", "Gerenciar cursos"))
                
            if "gerar_relatorios" in permissoes:
                opcoes_avancadas.append(("9", "Gerar relatórios"))
                
            if "gerenciar_permissoes" in permissoes:
                opcoes_avancadas.append(("10", "Gerenciar permissões"))
                
            # Mostrar opções avançadas se existirem
            for num, texto in opcoes_avancadas:
                print(f"{num}. {texto}")
                
            print(f"{11 if opcoes_avancadas else 8}. Logout")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                GerenciadorCursos.meus_cursos(self.cursos, self.usuarios, self.usuario_logado)
            elif opcao == "2":
                self.usuarios, self.acessos = GerenciadorCursos.inscrever_curso(self.cursos, self.usuarios, self.usuario_logado, self.acessos)
            elif opcao == "3":
                self.acessos = GerenciadorCursos.visualizar_conteudo_curso(self.cursos, self.usuarios, self.usuario_logado, self.acessos)
            elif opcao == "4":
                self.usuarios, self.acessos = GerenciadorCursos.realizar_exercicios(self.cursos, self.usuarios, self.usuario_logado, self.acessos)
            elif opcao == "5":
                self.usuarios, self.acessos = GerenciadorAutenticacao.alterar_senha(self.usuarios, self.usuario_logado, self.acessos)
            elif opcao == "6":
                self.visualizar_dados()
            elif opcao == "7":
                GerenciadorEstatisticas.visualizar_estatisticas(self.usuarios, self.cursos, self.acessos)
            elif opcao == "8" and any(p in permissoes for p in ["adicionar_cursos", "remover_cursos"]):
                self.gerenciar_cursos()
            elif opcao == "9" and "gerar_relatorios" in permissoes:
                self.gerar_relatorios()
            elif opcao == "10" and "gerenciar_permissoes" in permissoes:
                self.gerenciar_permissoes()
            elif opcao == str(11 if opcoes_avancadas else 8):
                self.acessos = GerenciadorDados.registrar_acesso(self.acessos, self.usuario_logado, "logout")
                self.usuario_logado = None
                break
            else:
                print("Opção inválida!")

    def menu_principal(self):
        """Exibe o menu principal do sistema"""
        while True:
            print("\n=== Plataforma de Educação Digital Segura ===")
            print("1. Login")
            print("2. Cadastrar-se")
            print("3. Visualizar cursos disponíveis")
            print("4. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.usuario_logado, self.acessos = GerenciadorAutenticacao.login(self.usuarios, self.acessos)
                if self.usuario_logado:
                    self.menu_usuario()
            elif opcao == "2":
                self.usuarios, self.acessos = GerenciadorAutenticacao.cadastrar_usuario(self.usuarios, self.acessos)
            elif opcao == "3":
                GerenciadorCursos.listar_cursos(self.cursos)
            elif opcao == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

# Inicialização do sistema
if __name__ == "__main__":
    sistema = SistemaEducacaoDigital()
    sistema.menu_principal()
