
# 📊 Análise de Sentimento com Streamlit e Transformers

Este projeto é uma aplicação web simples para **análise de sentimento** utilizando o modelo pré-treinado da biblioteca `transformers`. A interface é construída com **Streamlit**, oferecendo uma experiência interativa e fácil de usar.

## 🎯 Funcionalidades

- **Análise rápida de sentimentos** (Positivo, Negativo, Neutro) para textos inseridos pelo usuário.
- Interface intuitiva com **resultados coloridos**:  
  - Verde para **Positivo** 😊  
  - Vermelho para **Negativo** 😡  
  - Amarelo para **Neutro** 😐
- **Imagem inicial** e **layout centralizado** para uma interface visualmente atraente.
- Fácil de configurar e rodar localmente.

---

## 🚀 Demonstração

Você pode rodar este projeto localmente seguindo os passos abaixo ou publicá-lo no **Streamlit Cloud**.

---

## 🛠️ Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado e as bibliotecas necessárias. 

---

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-sentimento-streamlit.git
   cd analise-sentimento-streamlit
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

   > **Nota:** As bibliotecas principais são:
   > - `streamlit` para a interface web.
   > - `transformers` para o pipeline de análise de sentimento.

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

5. Acesse a aplicação em seu navegador:
   ```
   http://localhost:8501
   ```

---

## 📂 Estrutura do Projeto

```bash
.
├── app.py               # Código principal da aplicação
├── requirements.txt     # Bibliotecas necessárias
└── README.md            # Documentação do projeto
```

---

## 🧑‍💻 Contribuindo

Contribuições são bem-vindas! Se você quiser melhorar este projeto, siga as instruções abaixo:

1. Fork o repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b feature-sua-feature
   ```
3. Faça as alterações desejadas e commit:
   ```bash
   git commit -m "Adiciona nova feature: sua feature"
   ```
4. Envie a sua branch para o GitHub:
   ```bash
   git push origin feature-sua-feature
   ```
5. Abra um **Pull Request** e descreva suas alterações.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

```
MIT License

Copyright (c) [2024] [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ✨ Créditos

- **Streamlit** – Framework para criação de aplicações web interativas.
- **Hugging Face Transformers** – Biblioteca para modelos de NLP pré-treinados.

---

## 📧 Contato

Se tiver dúvidas ou sugestões, entre em contato:  
📧 **seu-email@example.com**

---

## 🌟 Agradecimentos

Se você gostou deste projeto, deixe uma ⭐ no repositório para ajudar a divulgá-lo!

---

### Exemplo de Arquivo `requirements.txt`
```txt
streamlit==1.25.0  # Verifique a versão mais recente se necessário
transformers==4.34.0  # Ou a versão mais atual disponível
```
