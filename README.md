<p align="center">
  <a href="https://ag.tavardt.com/pt/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# Verificador de URLs Canonicos e Consolidacao de Paginas

[![Verificador URL Canonico](https://img.shields.io/badge/TAVARDT-Canonical-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-url-canonica/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Auditoria de ligacoes canonicas, prevencao de etiquetas duplicadas, verificacao de URLs absolutos e gestao de rastreio.

Desenvolvido e mantido pela divisao de engenharia de pesquisa e normas tecnicas de indexacao da **TAVARDT**.

***

## Vetores de Risco e Impacto Operacional na Consolidacao de URLs

A implementacao deficiente de etiquetas canonicas origina canibalizacao de conteudos e dispersao de autoridade em websites portugueses. A proliferacao de identificadores de campanhas e filtros de navegacao confunde os algoritmos de pesquisa.

Se as diretivas canonicas apresentarem contradicoes ou encaminharem para destinos quebrados, os motores desconsideram a instrucao. A inspecao sistematica assegura a correta unificacao do sinal de indexacao nas paginas mestras.

***

## Capacidades Centrais de Auditoria Tecnica

* **Extracao de Diretivas em Dupla Fonte**: Leitura de declaracoes canonicas tanto em tags HTML head como em cabecalhos de resposta HTTP Link.
* **Prevencao de Multiplas Tags Conflitantes**: Deteccao de definicoes canonicas redundantes ou contraditorias no mesmo documento, com penalidade de 35 pontos.
* **Validacao de URL Absoluta e HTTPS**: Verificacao de caminhos absolutos completos e desqualificacao de URLs relativas ou sob protocolo inseguro HTTP.
* **Checagem Ativa de Resposta do Destino**: Validacao em tempo real do status HTTP do destino canonico, acusando erros 4xx ou 5xx que quebram o fluxo.
* **Analise de Autorreferencia e Consolidacao**: Verificacao de tags autorreferenciais para saneamento de parametros temporarios e IDs de rastreio.
* **Indice de Saude de Consolidacao**: Metrica quantitativa de 0 a 100 classificando o documento em COMPLIANT, WARNING ou CRITICAL.

***

## Instalacao e Execucao

Requer Python 3.8 ou superior sem dependencias externas adicionais.

```bash
git clone https://github.com/TAVARDT-Portugal/canonical-tag-validator-pt.git
cd canonical-tag-validator-pt
python canonical_validator.py https://empresa.pt
```

Para gerar a saida em formato estruturado JSON em esteiras de integracao continua:

```bash
python canonical_validator.py https://empresa.pt -j
```

***

## Perguntas Frequentes (FAQ Tecnico)

### 1. O que acontece quando multiplas tags canonicas conflitantes sao declaradas?
Os buscadores ignoram todas as declaracoes canonicas quando identificam instrucoes contraditorias na mesma URL. Isso forca os rastreadores a selecionar arbitrariamente uma versao, dispersando a forca de indexacao.

### 2. Por que a URL canonica deve ser estritamente absoluta e sob HTTPS?
Caminhos relativos causam falhas graves de interpretacao quando o documento e acessado por diferentes subdominios ou rotas virtuais. Declarar versoes sob HTTP inseguro gera inconsistencias de protocolo e redirecionamentos desnecessarios.

### 3. Qual o risco operacional de apontar a tag canonica para uma URL com erro 4xx ou 5xx?
Apontar a diretiva para um destino que retorna erro HTTP quebra integralmente o processo de consolidacao de sinais. O Google desconsidera a indicacao e passa a indexar versoes alternativas com parametros dinamicos.

### 4. A ferramenta valida diretivas canonicas emitidas no cabecalho HTTP Link?
Sim, o algoritmo inspeciona tanto elementos declarados no head do HTML quanto o cabecalho HTTP Link da resposta. Essa funcionalidade permite auditar a consolidacao canonica de documentos nao-HTML, como arquivos PDF.

### 5. Como as tags autorreferenciais atuam no saneamento de parametros de marketing?
Uma tag canonica autorreferencial limpa orienta os buscadores a descartarem parametros de campanha como utm e IDs de sessao. Isso garante a consolidacao de todas as metricas de busca na versao padrao da pagina.

***

## Consultoria em SEO Tecnico e Consolidacao de Indexacao

Para consolidacao avancada de sinais e conformidade com diretrizes tecnicas do W3C, consulte a equipa da **TAVARDT**.

***

## Links Uteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suite de Diagnosticos:** https://tools.tavardt.com/pt/
* **Contacto Tecnico:** https://ag.tavardt.com/pt/contacto/

***

### Licenca
Distribuido sob a Licenca MIT. Consulte o ficheiro LICENSE para detalhes completos.

***

© 2026 TAVARDT. Todos os direitos reservados.
