# 🎓 Plataforma de Formatura  

Este é um projeto desenvolvido em Django para gerenciar eventos de formatura. A plataforma permite que os usuários confirmem presença e adquiram presentes de forma simples e organizada. Foi criado pensando na experiência dos convidados e na praticidade para os organizadores.  

---

## 🌟 Funcionalidades  

- **Confirmação de Presença:** Os convidados podem confirmar sua presença diretamente pela plataforma.  
- **Lista de Presentes:** Exibe presentes disponíveis com opções de ordenação (preço e nome).  
  - Ordenação por preço: menor para maior ou maior para menor.  
  - Ordenação por nome: A-Z ou Z-A.  
- **Galeria de Imagens:** Exibição de fotos relacionadas ao evento.  
- **Pagamentos via PIX:** Geração de QR Code para facilitar o pagamento dos presentes.  
- **Design Responsivo:** Interface amigável e adaptada para dispositivos móveis e desktops.  
- **Sistema de Menus:** Sidebar dinâmica para navegação fácil entre páginas.  
- **Interface Personalizada:** Botões estilizados e opções de filtros para os usuários.  

---

## 🛠️ Tecnologias Utilizadas  

- **Linguagem:** Python 3.9  
- **Framework Web:** Django 4.x  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Banco de Dados:** PostgreSQL (padrão) ou outro configurado no `.env`.  
- **Outros:** Font Awesome (ícones)  

---

## 🚀 Como Executar o Projeto  

### **Pré-requisitos**  
- Python 3.9 ou superior  
- Gerenciador de pacotes `pip`  
- Virtualenv (recomendado)  

### **Passo a passo**  

1. **Clone o repositório:**  
   ```bash
   git clone https://github.com/NatanOliveiraslv/formatura_app
   cd seu-repositorio
   ```

2. **Crie e ative um ambiente virtual:**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Crie um arquivo `.env` na raiz do projeto e adicione as configurações de banco de dados e PIX:**  
   ```
   SECRET_KEY=<sua-secret-key>
   DB_NAME=<nome-do-banco>
   DB_USER=<usuario-do-banco>
   DB_PASSWORD=<senha-do-banco>
   DB_HOST=<host-do-banco>
   DB_PORT=<porta-do-banco>

   NOME=<seu-nome>
   CHAVE_PIX=<sua-chave-pix>
   CIDADE=<sua-cidade>
   ```

5. **Configure o banco de dados:**  
   - Aplique as migrações:  
     ```bash
     python manage.py migrate
     ```

6. **Adicione os arquivos estáticos:**  
   ```bash
   python manage.py collectstatic
   ```

7. **Inicie o servidor local:**  
   ```bash
   python manage.py runserver
   ```

8. **Acesse o projeto no navegador:**  
   - URL padrão: [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 📝 Como Contribuir  

1. Faça um fork do projeto.  
2. Crie uma branch para sua feature ou correção:  
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:  
   ```bash
   git commit -m 'Minha nova feature'
   ```
4. Envie para o repositório original:  
   ```bash
   git push origin minha-feature
   ```
5. Abra um pull request.  

---

## 📧 Contato  

- Desenvolvedor: **Natan Oliveira da Silva**  
- E-mail: seu-email@example.com  
- LinkedIn: (www.linkedin.com/in/natan-oliveira-silva)  

---

© 2024 Desenvolvido por **Natan Oliveira da Silva**.