from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)



def is_ip_address(url):
    ip_pattern = re.compile(
        r'^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}'
    )
    return bool(ip_pattern.match(url))


def url_length_check(url):
    return len(url) > 75


def has_at_symbol(url):
    return '@' in url


def has_hyphen(domain):
    return '-' in domain


def has_multiple_subdomains(domain):
    return domain.count('.') > 2


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

    verdict = "⚠️ Suspicious / Phishing URL" if score >= 4 else "✅ Safe URL"
    return score, verdict



@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    result = None
    status = None
    risk_percent = 0

    if request.method == "POST":
        url = request.form.get("url")
        score, result = analyze_url(url)

        if score >= 4:
            status = "suspicious"
        else:
            status = "safe"

        risk_percent = int((score / 8) * 100)

    return render_template(
        "index.html",
        score=score,
        result=result,
        status=status,
        risk_percent=risk_percent
    )


if __name__ == "__main__":
    app.run(debug=True)