---
title: "Digital Security"
layout: archive
permalink: /en_digital_security/
lang: en
seo_description: >
  Practical digital security guides covering phishing, smishing, passwords, passkeys, MFA, backups, ransomware, identity theft, privacy, and small business cyber hygiene.
sidebar:
    nav: "sidebar-category"
---

The Digital Security category turns common cyber risks into practical routines for individuals, families, small businesses, and small teams. It focuses on real situations such as phishing messages, account takeover, failed backups, payment fraud, home router settings, and cloud sharing mistakes.

The articles refer to official sources such as CISA, NIST, FTC, KISA BohoNara, and privacy reporting channels. The goal is not to recommend expensive tools. The goal is to build habits: pause before clicking, verify through a trusted route, keep accounts recoverable, and report incidents early.

Start with phishing triage, password managers, and MFA. If you run a shop or small team, read the small-business baseline, invoice payment fraud, and employee phishing drill articles together.

## Start Here

- [A 30-Second Phishing Triage](/en_digital_security/phishing-message-triage/)
- [Password Manager First Setup](/en_digital_security/password-manager-first-setup/)
- [Small Business Cyber Baseline](/en_digital_security/small-business-cyber-baseline/)

## Latest Articles

{% assign posts = site.categories["en_Digital_Security"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
