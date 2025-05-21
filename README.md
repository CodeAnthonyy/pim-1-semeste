# Documentação do Sistema de Educação Digital

 Visão Geral do Sistema

O sistema principal (`sistema_educacao_digital_final.py`) é uma plataforma de educação digital que gerencia cursos, usuários e suas interações. Ele oferece:

1. Autenticação de usuários (login/cadastro)
2. Gerenciamento de cursos e conteúdos educacionais
3. Sistema de exercícios e avaliação
4. Geração de relatórios e estatísticas
5. Controle de permissões de usuários

 Funcionalidades Principais

1. Autenticação:
   - Cadastro de novos usuários com validação de senha e email
   - Login seguro com senhas criptografadas
   - Alteração de senha

2. Gerenciamento de Cursos:
   - Listagem de cursos disponíveis
   - Inscrição em cursos
   - Visualização de conteúdo dos cursos
   - Realização de exercícios e avaliação automática

3. **Relatórios e Estatísticas**:
   - Visualização de estatísticas do sistema
   - Geração de relatórios em arquivos TXT
   - Análise de desempenho dos usuários

4. **Controle de Acesso**:
   - Sistema de permissões granular
   - Diferentes níveis de acesso para usuários comuns e administradores

# Arquivos JSON e suas Funções

1. usuarios.json:
   - Armazena todos os dados dos usuários cadastrados
   - Estrutura de cada usuário:
     - Nome completo e dados de login (senha criptografada + salt)
     - Email e data de cadastro
     - Lista de cursos inscritos
     - Resultados de exercícios realizados
     - Permissões de acesso no sistema

2. cursos.json:
   - Contém a lista de cursos disponíveis na plataforma
   - Para cada curso armazena:
     - Título e descrição
     - Número de módulos
     - Nível de dificuldade
     - Carga horária

3. acessos.json:
   - Registra todas as interações dos usuários com o sistema
   - Armazena:
     - Usuário que realizou a ação
     - Tipo de ação (login, visualização de conteúdo, etc.)
     - Data e hora exata da ação
   - Usado para gerar estatísticas e relatórios de uso

4. conteudo_cursos.py (não é JSON, mas importante):
   - Contém todo o conteúdo educacional dos cursos
   - Organizado por cursos e tópicos
   - Inclui os exercícios de avaliação para cada curso
   - Usa um dicionário para mapear cada curso ao seu conteúdo

#Fluxo Principal do Sistema

1. Inicializa carregando todos os dados dos arquivos JSON
2. Exibe menu principal com opções de login, cadastro e visualização de cursos
3. Após login, mostra menu específico com base nas permissões do usuário
4. Todas as interações são registradas no arquivo de acessos
5. Ao sair, os dados são persistidos nos arquivos JSON

O sistema foi projetado para ser modular, seguro e extensível, permitindo fácil adição de novos cursos e funcionalidades.
