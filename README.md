# < JOBinho/>

:point_right: [CLIQUE AQUI PARA VOTAR](https://discordapp.com/channels/1228404913705451612/1228406162618060913/1238607845293953166) :star:

JOBinho é um assistente virtual inteligente de uma plataforma fictícia chamada SeuJOB que tem o objetivo de auxiliar com dúvidas e análises de currículos.

Esse projeto foi feito como projeto final para a Imersão IA_ da alura em parceria com o Google.

![img](/docs/img/JOBinhoBotBanner.png)


# O que é o JOBinho?


JOBinho é um assistente virtual inteligente criado para o portal de vagas fictício, SeuJOB. Sua principal função é oferecer suporte a candidatos que têm dúvidas sobre como estruturar ou otimizar seus currículos. Através de uma análise detalhada, JOBinho examina cada currículo, fornecendo feedback construtivo e dicas práticas para melhorias. Além disso, ele avalia os currículos com uma nota de 0 a 5, baseando-se em uma estrutura genérica e critérios específicos de avaliação. Essa pontuação ajuda os usuários a entenderem os pontos fortes e as áreas de melhoria de seus documentos, potencializando suas oportunidades no competitivo mercado de trabalho.

## Como utilizar?

O JOBinho está disponível no Telegram pelo link [t.me/seujob_assistant_bot](https://t.me/seujob_assistant_bot). Basta digitar /start que ele começará a responder suas dúvidas sobre currículos, até mesmo fazendo uma avaliação detalhando pontos fortes e fracos.

# Sobre o projeto

O JOBinho foi desenvolvido em **Python**, utilizando algumas bibliotecas, sendo a principal delas a [python-telegram-bot](https://python-telegram-bot.org/), onde ela facilita a implementação de bots do Telegram.

A API do Gemini foi utilizada justamente para:

- Dúvidas sobre currículos
- Melhorias em textos para currículos    
- Análise do conteúdo de texto de currículos


## Análise de Currículos

A análise de currículos no projeto é realizada por um bot de Telegram que integra tecnologias de inteligência artificial. Aqui está uma visão geral sucinta do processo:

1. **Recepção do Currículo**:
   - O usuário envia seu currículo em formato PDF através do bot do Telegram.

2. **Extração de Texto**:
   - O bot utiliza a biblioteca `pypdf` para extrair texto de cada página do currículo PDF.

3. **Análise via Modelo de IA**:
   - O texto extraído é combinado com instruções predefinidas que orientam o modelo de IA sobre como analisar o documento.
   - O modelo, configurado com parâmetros específicos de geração e filtros de segurança, gera um feedback baseado no conteúdo do currículo, avaliando aspectos como estrutura, clareza e conteúdo.

4. **Retorno de Feedback**:
   - O feedback gerado pelo modelo é enviado de volta ao usuário através do Telegram, oferecendo dicas de melhorias e outras recomendações relevantes para otimizar o currículo.

Este processo automático permite uma análise rápida e personalizada de currículos, ajudando os usuários a aprimorarem seus documentos para processos seletivos.

## Gemini API

As requisições ao Gemini são feitas dentro do projeto e estão estruturadas dessa forma:

1. **Configuração do Modelo**:
   - Primeiramente, o modelo do Gemini é configurado usando a função `getModel` do arquivo `geminiHandler.py`. Esta função estabelece os parâmetros de geração (como temperatura e limites de tokens), instruções de sistema, e configurações de segurança para filtrar conteúdos indesejáveis. O modelo especificado é "gemini-1.5-pro-latest".

2. **Preparação dos Dados**:
   - Quando um currículo em PDF é recebido através do bot, ele é primeiramente salvo e seu conteúdo é extraído página por página usando a função `extract_pdf_pages` que utiliza a biblioteca `pypdf`. Este texto é então combinado com uma instrução explícita para análise.

3. **Requisição de Geração de Conteúdo**:
   - Com os dados preparados (texto do currículo e instrução de análise), eles são passados ao modelo configurado através de uma função chamada `pdf_analysis`. Esta função cria um prompt com os dados do currículo e a instrução de análise.
   - A função então invoca o método `generate_content` do modelo do Gemini com o prompt formado. O método processa os dados e gera uma resposta baseada nas instruções fornecidas e no conteúdo do currículo.

4. **Recebimento e Tratamento da Resposta**:
   - A resposta gerada pelo modelo é recebida como texto, que é interpretado como o feedback ou análise do currículo. Este feedback é então enviado de volta ao usuário através do bot do Telegram.

# Author

Feito por [Daniel Lourenço](https://github.com/danluan) 😎

:point_right: [CLIQUE AQUI PARA VOTAR](https://discordapp.com/channels/1228404913705451612/1228406162618060913/1238607845293953166) :star:
