# Verificador de URL Canonico e Consolidacao de Paginas

[![Verificador URL Canonico](https://img.shields.io/badge/TAVARDT-Canonical-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-url-canonica/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

Inspecao tecnica de etiquetas canonicas, deteccao de conflitos de protocolo e conformidade com normas W3C.

Desenvolvido e mantido pela divisao de arquitetura de indexacao da **TAVARDT**.

***

## Capacidades de Auditoria de URL Canonico

* **Detecao de Apontadores Canonicos**: Inspeciona a presenca da diretiva `<link rel="canonical">` no cabecalho HTML e cabecalhos HTTP.
* **Prevencao de Duplicacao de Etiquetas**: Identifica anomalias de multiplas declaracoes canonicas contraditorias no mesmo documento.
* **Validacao de Caminhos Absolutos**: Assegura a utilizacao de enderecos absolutos sob protocolo seguro HTTPS.
* **Inspecao de Codigo de Resposta**: Verifica se o destino canonico responde com HTTP 200 OK, evitando ligacoes para erros 404 ou cadeias de redirecionamento.
* **Indice de Consolidacao Semantica**: Metrica de 0 a 100 com recomendacoes tecnicas priorizadas.

***

## Instalacao e Execucao

Requer Python 3.8 ou superior, operando exclusivamente com a biblioteca padrao.

```bash
git clone https://github.com/TAVARDT-Portugal/canonical-tag-validator-pt.git
cd canonical-tag-validator-pt
python canonical_validator.py https://empresa.pt
```

Para inspecao com saida estruturada JSON:

```bash
python canonical_validator.py https://empresa.pt -json
```

***

## Diagnostico Completo na Web

Para verificacao completa e profunda da sua infraestrutura web:

* **Verificador de URL Canonica Oficial**
* **[Portal Corporativo TAVARDT](https://ag.tavardt.com/pt/)**

***

## Consultoria em Indexacao e SEO Tecnico

Para projetos de consolidacao semantica em conformidade com Normas Europeias de Interoperabilidade e W3C, contacte a equipa da **TAVARDT**.

***

© 2026 TAVARDT. Todos os direitos reservados.
