# Zhopin Barb website

Static bilingual website. No application server or database is required.

## Maintain the English content

Run these Python scripts in this order (standard library only):

1. python tools/upgrade-site.py
2. python tools/add-inquiry.py
3. python tools/add-international.py

The English project and capability data lives in tools/upgrade-site.py. The international buyer copy lives in tools/add-international.py. Persian pages retain their existing content. These scripts regenerate the English pages, language links and sitemap; edit generated English pages through the scripts to avoid losing edits.

## Hosting

Publish the site root, retaining CNAME, .nojekyll, page paths and assets. The current canonical host is https://zhopinbarb.ir. English pages are under /en/. Keep HTTPS enabled.

## Inquiry behavior

The inquiry form prepares a mailto link or copies text to the clipboard. It does not send a request, upload files, retain form data or promise a response time. Customers attach technical files in their email application. A server-backed submission service requires separate implementation and testing.

## Verification before publishing

Check both languages on desktop and mobile. Test language links, portfolio search plus category filters, Escape-to-close image viewer, required inquiry fields, project prefilling and inquiry text. Ensure sitemap URLs exist and reciprocal language annotations remain intact. Do not assert certifications, export history, shipping coverage or performance figures without company confirmation.

## Signature design and route finder

After the three build commands above, run `python tools/add-signature.py`.
The appearance is in `signature.css`; `route-guide.js` contains the bilingual rule-based route matching and inquiry handoff. This is a guided selector, not an AI quotation engine. It does not store personal data, calculate prices or certify material suitability. No third-party API is required.

## Articles and formal typography

After add-signature.py, run tools/apply-formal.py and then tools/add-articles.py. Article text and bilingual metadata are maintained in tools/add-articles.py. Estedad is self-hosted under assets/fonts with its SIL Open Font License. formal.css controls the font and article layouts. The developer credit is applied by apply-formal.py.

## Historical photographs

Run `python tools/add-history.py` after the other content scripts to restore the bilingual about-page history. Original supplied screenshots are preserved in assets/history; history.css frames their photographic regions without altering people or event content. Captions distinguish the former company Avijeh Sanat Negin Besat from the current legal company. Dates refer to post publication, not independently verified event dates. No certification or individual award is inferred from these posts.
