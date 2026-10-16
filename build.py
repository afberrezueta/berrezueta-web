#!/usr/bin/env python3
"""Genera las páginas del sitio a partir de un solo encabezado y pie (python3 build.py)."""
from pathlib import Path

SITE = "https://berrezuetainc.com"
EMAIL = "contact@berrezuetainc.com"
PHONE_HREF = "+17185025182"
PHONE = "(718) 502-5182"
# La misma dirección que se envió a Meta en la verificación del negocio.
ADDRESS = "6 N Strathmore Street, Valley Stream, NY 11581, USA"
UPDATED_ISO, UPDATED = "2026-10-16", "October 16, 2026"

def head(title, desc, path, extra="", root=""):
    url = f"{SITE}/{path}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#1B2A41">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Berrezueta Inc.">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@700&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}styles.css">{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="top">
  <a class="mark" href="{root or './'}">Berrezueta Inc.</a>
  <nav aria-label="Main"><a href="{root or './'}#what-we-do">What we do</a><a href="{root or './'}#contact">Contact</a></nav>
</header>
"""

def foot(current="", root=""):
    def link(slug, label):
        cur = ' aria-current="page"' if slug == current else ""
        return f'<a href="{root}{slug}"{cur}>{label}</a>'
    return f"""<footer>
  <nav class="links" aria-label="Legal">{link("privacy", "Privacy policy")}{link("data-deletion", "Data deletion")}{link("terms", "Terms of service")}</nav>
  <p class="meta"><span>© 2026 Berrezueta Inc.</span><span>{ADDRESS}</span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_HREF}">{PHONE}</a></p>
</footer>
</div>
</body>
</html>
"""

def doc(title, slug, desc, body):
    return head(f"{title} — Berrezueta Inc.", desc, slug) + f"""<main id="main" class="doc">
<h1>{title}</h1>
<p class="updated">Last updated: <time datetime="{UPDATED_ISO}">{UPDATED}</time></p>
{body}
</main>
""" + foot(slug)

CONTACT_P = f'<p>Berrezueta Inc., {ADDRESS}. Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_HREF}">{PHONE}</a>.</p>'

JSONLD = f"""
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","@id":"{SITE}/#org","name":"Berrezueta Inc.","legalName":"Berrezueta Inc.","url":"{SITE}/","logo":"{SITE}/apple-touch-icon.png","email":"{EMAIL}","telephone":"+1-718-502-5182","address":{{"@type":"PostalAddress","streetAddress":"6 N Strathmore Street","postalCode":"11581","addressLocality":"Valley Stream","addressRegion":"NY","addressCountry":"US"}},"contactPoint":{{"@type":"ContactPoint","contactType":"customer service","email":"{EMAIL}","telephone":"+1-718-502-5182","areaServed":"US","availableLanguage":["en","es"]}}}}
</script>"""

INDEX = head("Berrezueta Inc. — E-commerce and technology, Valley Stream, NY",
             "Berrezueta Inc. sells products online and builds software and AI tools for small businesses. Based in Valley Stream, New York.",
             "", JSONLD) + f"""<main id="main">
  <div class="hero">
    <h1>Berrezueta Inc.</h1>
    <p class="shelf"><span>E-commerce and technology</span><span>Registered in New York</span><span>Valley Stream, NY</span></p>
    <p class="intro">We sell products online and build the software that helps small businesses run.</p>
  </div>

  <section id="what-we-do" aria-labelledby="what-we-do-title">
    <h2 id="what-we-do-title">What we do</h2>
    <p class="lead">Berrezueta Inc. works on two connected lines of business.</p>
    <div class="two">
      <div>
        <h3>E-commerce</h3>
        <p>We research product demand, source from vetted suppliers and sell online to customers in the United States.</p>
      </div>
      <div>
        <h3>Technology</h3>
        <p>We build software and AI tools for research, content and operations, including assistants that customers and staff can reach on WhatsApp.</p>
        <p class="product">Our product <a href="https://www.deltalyn.com/">Deltalyn</a> publishes daily scenarios for US stocks and crypto, with a public, auto-graded record of every call. It provides general information, not personalized financial advice.</p>
      </div>
    </div>
  </section>

  <section id="contact" aria-labelledby="contact-title">
    <h2 id="contact-title">Contact</h2>
    <dl class="contact">
      <dt>Company</dt><dd>Berrezueta Inc., New York</dd>
      <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      <dt>Phone</dt><dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd>
      <dt>Address</dt><dd>{ADDRESS}</dd>
    </dl>
  </section>
</main>
""" + foot()

PRIVACY = doc("Privacy policy", "privacy", "How Berrezueta Inc. collects, uses and protects personal information.", f"""<p>This policy explains how Berrezueta Inc. ("we", "us") collects, uses and protects personal information when you visit our website, buy from us or message us, including on WhatsApp.</p>

<h2>Information we collect</h2>
<ul>
<li><strong>Information you give us:</strong> your name, email, phone number, shipping address and the content of messages you send us.</li>
<li><strong>Order information:</strong> the products you buy and your order history. Payments are handled by our payment processors; we do not store full card numbers.</li>
<li><strong>Messaging information:</strong> when you message us on WhatsApp, we receive your phone number, your profile name and the messages you send, through the WhatsApp Business Platform operated by Meta.</li>
<li><strong>Technical information:</strong> basic data such as browser type and pages visited, collected by our hosting and e-commerce providers.</li>
</ul>

<h2>Cookies and third-party services on this website</h2>
<p>This website sets no cookies and uses no analytics. It is hosted on GitHub Pages and loads fonts from Google Fonts, so those providers receive your IP address and browser information when you visit.</p>

<h2>How we use it</h2>
<ul>
<li>To process and deliver orders and answer your questions.</li>
<li>To reply to your WhatsApp messages. Some replies may be prepared with the help of automated and AI tools.</li>
<li>To run, secure and improve our services, and to meet legal obligations.</li>
</ul>
<p>We do not sell your personal information.</p>

<h2>Who we share it with</h2>
<p>We share information only with providers that help us operate, and only as needed: our e-commerce platform, payment processors, shipping carriers, hosting providers, Meta (for WhatsApp messaging) and AI service providers that process message content on our behalf. We may also disclose information when required by law.</p>

<h2>How long we keep it</h2>
<p>We keep information only as long as needed for the purposes above or as required by law, then delete or anonymize it.</p>

<h2>Your choices and rights</h2>
<p>You can ask us to access, correct or delete your personal information, or stop messaging you, at any time. See <a href="{SITE}/data-deletion">{SITE}/data-deletion</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Security</h2>
<p>We use reasonable technical and organizational measures to protect your information. No method of transmission or storage is completely secure.</p>

<h2>Children</h2>
<p>Our services are not directed to children under 13, and we do not knowingly collect their information.</p>

<h2>Changes</h2>
<p>We may update this policy. The date at the top shows the latest version.</p>

<h2>Contact</h2>
{CONTACT_P}""")

DELETION = doc("Data deletion", "data-deletion", "How to ask Berrezueta Inc. to delete your personal data.", f"""<p>You can ask us to delete the personal information we hold about you, including WhatsApp messages and order information.</p>
<h2>How to ask</h2>
<p>Email <a href="mailto:{EMAIL}?subject=Data%20deletion%20request">{EMAIL}</a> with the subject "Data deletion request", or call <a href="tel:{PHONE_HREF}">{PHONE}</a>. Include the phone number or email you used with us so we can find your information.</p>
<h2>What happens next</h2>
<p>We confirm your request within 7 days and complete the deletion within 30 days. You will receive a confirmation once your data has been deleted. We may keep records we are legally required to retain, such as tax and transaction records, and we will tell you if that applies.</p>""")

TERMS = doc("Terms of service", "terms", "Terms for using the Berrezueta Inc. website, products and messaging services.", f"""<p>These terms apply when you use the Berrezueta Inc. website, buy from us or message us. By using them, you agree to these terms.</p>
<h2>Orders</h2>
<p>Prices, availability and shipping times are shown at checkout. We may cancel an order if a product is unavailable or a price was listed in error, and we will refund any amount charged.</p>
<h2>Returns and refunds</h2>
<p>Return and refund conditions are provided at checkout and in your order confirmation. Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> for help with an order.</p>
<h2>Messaging</h2>
<p>Information we send through WhatsApp or other channels, including content prepared with AI tools, is for general information and may contain errors. It is not professional, legal or financial advice.</p>
<h2>Acceptable use</h2>
<p>Do not misuse our services, interfere with their operation or use them for anything unlawful.</p>
<h2>Liability</h2>
<p>To the extent allowed by law, Berrezueta Inc. is not liable for indirect or consequential damages arising from use of our services.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of New York, USA.</p>
<h2>Contact</h2>
{CONTACT_P}""")

# 404 se sirve en cualquier profundidad: rutas absolutas desde la raíz.
NOT_FOUND = head("Page not found — Berrezueta Inc.", "This page does not exist.", "404",
                 '\n<meta name="robots" content="noindex">', root="/") + """<main id="main" class="doc">
<h1>Page not found</h1>
<p>The page you are looking for does not exist or has moved. <a href="/">Go to the home page</a>.</p>
</main>
""" + foot(root="/")

PAGES = {"index.html": INDEX, "privacy.html": PRIVACY, "data-deletion.html": DELETION, "terms.html": TERMS, "404.html": NOT_FOUND}

if __name__ == "__main__":
    for name, html in PAGES.items():
        Path(name).write_text(html)
    print("generadas:", ", ".join(PAGES))
