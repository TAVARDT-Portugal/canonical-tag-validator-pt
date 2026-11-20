#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TAVARDT Portugal | Verificador de URL Canonico e Consolidacao de Paginas
Repository: https://github.com/TAVARDT-Portugal/canonical-tag-validator-pt
Official Tool: https://tools.tavardt.com/pt/verificador-url-canonica/
Enterprise Portal: https://ag.tavardt.com/pt/

Audits canonical links, duplicate tag detection, absolute URL verification, and crawl efficiency.
"""

import sys
import argparse
import json
import re
import urllib.request
import urllib.error
from urllib.parse import urlparse, urljoin

BANNER = "TAVARDT Portugal | Verificador de URL Canonico e Consolidacao de Paginas"
DESC = "Inspecao tecnica de etiquetas canonicas, deteccao de conflitos e conformidade W3C."
TARGET_PROMPT = "URL alvo para verificacao de apontador canonico"
JSON_HELP = "Apresenta o relatorio exclusivamente no formato JSON"
FETCHING = "A analisar consolidacao canonica em:"
STATUS_CODE = "Codigo de resposta HTTP:"
CANONICAL_FOUND = "URL Canonico declarado:"
NO_CANONICAL = "Nenhum apontador canonico identificado."
TAG_COUNT = "Total de etiquetas canonicas encontradas:"
IS_ABSOLUTE = "Utiliza caminho absoluto:"
IS_HTTPS = "Utiliza protocolo seguro HTTPS:"
IS_SELF_REF = "Apontamento autorreferencial:"
DEST_STATUS = "Status HTTP do URL de destino:"
SCORE_TITLE = "Pontuacao de Consolidacao Semantica:"
STATUS_PASS = "CONFORME"
STATUS_WARN = "AVISO"
STATUS_FAIL = "CRITICO"
WARN_NO_CANONICAL = "AVISO: Ausencia de etiqueta canonical. Risco de conteudo duplicado."
WARN_MULTIPLE = "ALERTA CRITICO: Multiplas etiquetas canonicas detetadas na mesma pagina."
WARN_RELATIVE = "AVISO: O URL canonico utiliza caminho relativo em vez de absoluto."
WARN_HTTP = "AVISO: O URL canonico utiliza protocolo HTTP inseguro."
WARN_DEST_ERR = "ALERTA CRITICO: O URL canonico de destino respondeu com codigo HTTP {status}."
FOOTER = "Para diagnostico avancado, consulte a ferramenta oficial: https://tools.tavardt.com/pt/verificador-url-canonica/"

def audit_canonical(target_url):
    parsed = urlparse(target_url)
    if not parsed.scheme:
        target_url = "https://" + target_url
        parsed = urlparse(target_url)

    req = urllib.request.Request(
        target_url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; TAVARDT-CanonicalAuditor/1.0; +https://ag.tavardt.com/pt/)"}
    )

    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            status_code = resp.status
            final_url = resp.geturl()
            raw_data = resp.read()
            encoding = resp.headers.get_content_charset() or "utf-8"
            html = raw_data.decode(encoding, errors="replace")
            http_link_header = resp.headers.get("Link", "")
    except urllib.error.HTTPError as e:
        return {
            "url": target_url,
            "status_code": e.code,
            "valid": False,
            "error": f"HTTP {e.code}"
        }
    except Exception as e:
        return {
            "url": target_url,
            "status_code": 0,
            "valid": False,
            "error": str(e)
        }

    # Extract all canonical tags from HTML
    canonical_tags = []
    matches = re.findall(r'<link[^>]+rel=[\'"]canonical[\'"][^>]*>', html, re.I)
    matches += re.findall(r'<link[^>]+href=[\'"][^\'"]+[\'"][^>]+rel=[\'"]canonical[\'"][^>]*>', html, re.I)
    
    seen_hrefs = set()
    for tag_str in matches:
        hr_m = re.search(r'href=[\'"]([^\'"]+)[\'"]', tag_str, re.I)
        if hr_m:
            href_val = hr_m.group(1).strip()
            if href_val not in seen_hrefs:
                seen_hrefs.add(href_val)
                canonical_tags.append({"raw_href": href_val, "source": "html"})

    # Extract from HTTP Link header if present
    if http_link_header:
        links = http_link_header.split(",")
        for l in links:
            if 'rel="canonical"' in l or "rel='canonical'" in l:
                hr_m = re.search(r'<([^>]+)>', l)
                if hr_m:
                    href_val = hr_m.group(1).strip()
                    if href_val not in seen_hrefs:
                        seen_hrefs.add(href_val)
                        canonical_tags.append({"raw_href": href_val, "source": "http_header"})

    findings = []
    score = 100
    declared_canonical = None
    is_absolute = False
    is_https = False
    is_self_ref = False
    dest_status_code = None

    if not canonical_tags:
        score -= 40
        findings.append({"level": "WARNING", "message": WARN_NO_CANONICAL})
    else:
        declared_canonical = canonical_tags[0]["raw_href"]
        if len(canonical_tags) > 1:
            score -= 35
            findings.append({"level": "CRITICAL", "message": WARN_MULTIPLE})

        # Check absolute vs relative
        can_parsed = urlparse(declared_canonical)
        if not can_parsed.scheme or not can_parsed.netloc:
            is_absolute = False
            score -= 20
            findings.append({"level": "WARNING", "message": WARN_RELATIVE})
            full_canonical_url = urljoin(final_url, declared_canonical)
        else:
            is_absolute = True
            full_canonical_url = declared_canonical

        # Check HTTPS
        can_full_parsed = urlparse(full_canonical_url)
        if can_full_parsed.scheme == "https":
            is_https = True
        else:
            is_https = False
            score -= 15
            findings.append({"level": "WARNING", "message": WARN_HTTP})

        # Check self-referential
        clean_target = final_url.rstrip("/")
        clean_canonical = full_canonical_url.rstrip("/")
        if clean_target == clean_canonical:
            is_self_ref = True

        # Check destination status code
        try:
            dest_req = urllib.request.Request(
                full_canonical_url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; TAVARDT-CanonicalAuditor/1.0; +https://ag.tavardt.com/pt/)"}
            )
            with urllib.request.urlopen(dest_req, timeout=10) as dest_resp:
                dest_status_code = dest_resp.status
        except urllib.error.HTTPError as e:
            dest_status_code = e.code
            score -= 30
            findings.append({"level": "CRITICAL", "message": WARN_DEST_ERR.replace("{status}", str(e.code))})
        except:
            dest_status_code = 0

    score = max(0, min(100, score))

    return {
        "url": target_url,
        "final_url": final_url,
        "status_code": status_code,
        "valid": True,
        "declared_canonical": declared_canonical,
        "canonical_tags_count": len(canonical_tags),
        "is_absolute": is_absolute,
        "is_https": is_https,
        "is_self_ref": is_self_ref,
        "dest_status_code": dest_status_code,
        "score": score,
        "findings": findings
    }

def main():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("url", help=TARGET_PROMPT)
    parser.add_argument("--json", action="store_true", help=JSON_HELP)

    args = parser.parse_args()
    result = audit_canonical(args.url)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print("=" * 70)
    print(BANNER)
    print("=" * 70)
    print(f"{FETCHING} {result['url']}")
    print(f"{STATUS_CODE} {result['status_code']}")

    if not result.get("valid"):
        print("ERRO: Nao foi possivel carregar a URL.")
        if "error" in result:
            print(f"Detalhes: {result['error']}")
        sys.exit(1)

    if result.get("declared_canonical"):
        print(f"{CANONICAL_FOUND} {result['declared_canonical']}")
    else:
        print(NO_CANONICAL)

    print(f"{TAG_COUNT} {result.get('canonical_tags_count', 0)}")
    print(f"{IS_ABSOLUTE} {'SIM' if result.get('is_absolute') else 'NAO'}")
    print(f"{IS_HTTPS} {'SIM' if result.get('is_https') else 'NAO'}")
    print(f"{IS_SELF_REF} {'SIM' if result.get('is_self_ref') else 'NAO'}")
    if result.get("dest_status_code"):
        print(f"{DEST_STATUS} {result['dest_status_code']}")

    print("-" * 70)
    print(f"{SCORE_TITLE} {result['score']}/100")
    if result["score"] >= 80:
        status_text = STATUS_PASS
    elif result["score"] >= 50:
        status_text = STATUS_WARN
    else:
        status_text = STATUS_FAIL
    print(f"Status: {status_text}")

    if result.get("findings"):
        print("-" * 70)
        print("Observacoes e Alertas:")
        for f in result["findings"]:
            print(f"  [{f['level']}] {f['message']}")

    print("=" * 70)
    print(FOOTER)
    print("=" * 70)

if __name__ == "__main__":
    main()
