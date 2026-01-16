import re
from urllib.parse import urlparse


def is_ip_address(url):
    ip_pattern = re.compile(
        r'^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}'
    )
    return bool(ip_pattern.match(url))


def url_length_check(url):
    return len(url) > 75


def has_at_symbol(url):
    return "@" in url


def has_hyphen(domain):
    return "-" in domain


def has_multiple_subdomains(domain):
    return domain.count(".") > 2


def uses_https(url):
    return url.startswith("https://")


def analyze_url(url):
    score = 0
    parsed = urlparse(url)
    domain = parsed.netloc

    if is_ip_address(url):
        score += 2
    if url_length_check(url):
        score += 1
    if has_at_symbol(url):
        score += 2
    if has_hyphen(domain):
        score += 1
    if has_multiple_subdomains(domain):
        score += 1
    if not uses_https(url):
        score += 1

    verdict = "⚠️ Suspicious / Phishing URL" if score >= 2 else "✅ Safe URL"
    return score, verdict
