# LinkedIn Networking Bot

📋 Descrição

Este bot automatiza o envio de convites no LinkedIn com mensagens personalizadas, buscando palavras-chave específicas relacionadas a profissionais de tecnologia. Ele foi desenvolvido com Python e Selenium, garantindo um comportamento humano por meio de atrasos aleatórios e simulação de digitação.


🚀 Funcionalidades
- Login automático no LinkedIn com segurança utilizando variáveis de ambiente.
- Pesquisa de perfis com base em palavras-chave específicas.
- Aplicação de filtros (ex.: filtrar por "Pessoas").
- Envio de convites com mensagens personalizadas.
- Logs detalhados e capturas de tela em caso de falhas.

🛠️ Tecnologias Utilizadas
- **Python** : Linguagem de programação principal.
- **Selenium**: Automação de interações com o navegador.
- **Webdriver Manager**: Gerenciamento automático do ChromeDriver.
- **Dotenv**: Gerenciamento de variáveis de ambiente.
- **Google Chrome**: Navegador utilizado para automação.

🖥️ Pré-requisitos
- Python 3.8 ou superior instalado.
- Google Chrome instalado.
- Variáveis de ambiente configuradas (EMAIL e PASSWORD).
- Uma conta no LinkedIn.

📦 Configuração do Ambiente
- Clone este repositório:

  *git clone https://github.com/Alonso0011/bot-linkedin.git*

- E dê um:

  *cd bot-linkedin*

- Crie um ambiente virtual:

  *python -m venv venv*
  
  *source venv/bin/activate*    # Para Linux/Mac
  
  *venv\Scripts\activate*       # Para Windows
  
- Instale as dependências:

  *pip install -r requirements.txt*

- Crie um arquivo .env na raiz do projeto e adicione suas credenciais:

*EMAIL=seu_email_linkedin*

*PASSWORD=sua_senha_linkedin*

▶️ Como Rodar o Bot

- Certifique-se de que o ambiente virtual está ativado.
- Execute o script:

  **python bot_linkedin.py**
  
O bot irá:

- Fazer login no LinkedIn.
- Realizar a pesquisa com a palavra-chave configurada no código ("Desenvolvedor Backend" por padrão).
- Aplicar o filtro para buscar apenas pessoas.
- Enviar convites com mensagens personalizadas para até 2 perfis (configurado como teste, você pode alterar o limite no código).

⚠️ Limitações e Cuidados

Limites do LinkedIn: O LinkedIn possui restrições diárias para envio de convites (aproximadamente 100 convites/dia). Este bot é configurado para enviar no máximo 2 convites por execução como teste, mas você pode ajustar isso.

Riscos de Detecção:

  - Incluímos atrasos randômicos e simulação de digitação para reduzir a detecção.
  
  - Não exceda os limites do LinkedIn para evitar bloqueios ou suspensão de conta.
  
Uso Responsável: Automatizar interações no LinkedIn pode violar os Termos de Serviço da plataforma. Use-o dentro das regras estabelecidas e por sua conta e risco.
