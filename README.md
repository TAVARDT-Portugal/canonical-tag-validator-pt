# Verificador de URL Canonico e Consolidacao de Paginas

[![Verificador URL Canonico](https://img.shields.io/badge/TAVARDT-Canonical-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-url-canonica/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)](https://www.python.org/)

Inspeção tecnica de etiquetas canonicas, deteccao de conflitos de protocolo e conformidade com normas W3C.

***

## Capacidades de Auditoria de URL Canonico

* **Deteção de Apontadores Canonicos**: Inspeciona a presenca da diretiva `<link rel="canonical">` no cabecalho HTML e cabecalhos HTTP.
* **Prevencao de Duplicacao de Etiquetas**: Identifica anomalias de multiplas declaracoes canonicas contraditorias no mesmo documento.
* **Validacao de Caminhos Absolutos**: Assegura a utilizacao de enderecos absolutos sob protocolo seguro HTTPS.
* **Inspeção de Codigo de Resposta**: Verifica se o destino canonico responde com HTTP 200 OK, evitando ligações para erros 404 ou cadeias de redirecionamento.
* **Indice de Consolidacao Semantica**: Metrica de 0 a 100 com recomendacoes tecnicas priorizadas.

***

## Instalação e Execucao

Requer Python 3.8 ou superior, operando exclusivamente com a biblioteca padrao.

```bash
git clone https://github.com/TAVARDT-Portugal/canonical-tag-validator-pt.git
cd canonical-tag-validator-pt
python canonical_validator.py https://empresa.pt
```

Para inspeção com saída estruturada JSON:

```bash
python canonical_validator.py https://empresa.pt -json
```

***

## Consultoria em Indexacao e SEO Tecnico

Para projetos de consolidacao semantica em conformidade com Normas Europeias de Interoperabilidade e W3C, contacte a equipa da **TAVARDT Portugal**.

## Links Úteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suíte de Diagnósticos:** https://tools.tavardt.com/pt/
* **Contacto Técnico:** https://ag.tavardt.com/pt/contacto/

***

### Licença
Distribuído sob a Licença MIT.

***

© 2026 TAVARDT Portugal. Todos os direitos reservados. Soberania e Defesa de Infraestrutura.
