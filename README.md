🛡️ PhishGuard | URL Threat Scanner

PhishGuard is a heuristic-based URL phishing detection tool built with Python and Flask. It analyzes URLs for suspicious patterns and visually communicates the threat level with an interactive and dynamic interface.

🔹 Project Overview

PhishGuard scans a URL for common phishing indicators and calculates a risk score to classify the URL as either Safe or Suspicious. The frontend responds dynamically:

✅ Safe URLs → Green-themed interface

⚠️ Suspicious URLs → Red glow, pulsing threat box, and a “LOCKDOWN MODE” banner

The project simulates real-world phishing detection logic in an educational, interactive way, making it resume-ready and interview-friendly.

🔹 Key Features

Heuristic Analysis: Detects multiple phishing patterns like:

IP address in the URL

Excessively long URLs (>75 characters)

Presence of @ symbol

Hyphens in the domain

Multiple subdomains

Missing HTTPS

Risk Scoring: Each triggered pattern adds to a cumulative score.

Dynamic UI Feedback: Background color, badges, and animations indicate the level of threat.

Educational Tool: Helps users understand phishing detection heuristics.

🔹 Technologies Used

Python 3.x

Flask (backend & templating)

HTML5 & CSS3 (frontend with animations)

Jinja2 (template rendering)