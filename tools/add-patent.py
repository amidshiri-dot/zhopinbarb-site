from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
for en in [False,True]:
 p=R/('en/about.html' if en else 'about.html');s=p.read_text(encoding='utf8')
 def t(fa,eng):return eng if en else fa
 body='<section id="patent-certificate" class="section patent-section"><div class="container patent-layout"><div><p class="eyebrow">'+t('سوابق اختراع و مستندات','INVENTION RECORDS & DOCUMENTATION')+'</p><h2>'+t('گواهی ثبت اختراع','Patent registration certificate')+'</h2><p class="body-copy">'+t('تصویر گواهی ثبت اختراع به نام محمدرضا شیری، صادره از سازمان ثبت اسناد و املاک کشور، در این بخش ارائه شده است.','This section presents the patent registration certificate issued in the name of Mohammadreza Shiri by Iran’s Organization for Registration of Deeds and Properties.')+'</p><dl class="patent-facts"><div><dt>'+t('نام مالک و مخترع در سند','Owner and inventor named in the document')+'</dt><dd>'+t('محمدرضا شیری','Mohammadreza Shiri')+'</dd></div><div><dt>'+t('نوع سند','Document type')+'</dt><dd>'+t('گواهی ثبت اختراع','Patent registration certificate')+'</dd></div></dl><a class="inline-link dark" href="/assets/history/patent-certificate-shiri.jpg" target="_blank" rel="noopener noreferrer">'+t('مشاهدهٔ تصویر کامل گواهی','View the full certificate image')+' ↗</a></div><figure class="patent-image"><a href="/assets/history/patent-certificate-shiri.jpg" target="_blank" rel="noopener noreferrer" aria-label="'+t('مشاهده گواهی ثبت اختراع در اندازهٔ اصلی','Open the patent certificate at original size')+'"><img src="/assets/history/patent-certificate-shiri.jpg" alt="'+t('تصویر گواهی ثبت اختراع به نام محمدرضا شیری','Patent registration certificate in the name of Mohammadreza Shiri')+'" width="959" height="1280" loading="lazy"></a><figcaption>'+t('تصویر سند ارائه‌شده توسط مجموعه','Document image supplied by the company')+'</figcaption></figure></div></section>'
 s=re.sub(r'<section id="patent-certificate".*?</section>','',s,flags=re.S)
 s=s.replace('</main>',body+'</main>').replace('/history.css?v=20261005','/history.css?v=20261005patent')
 p.write_text(s,encoding='utf8')
print('Patent certificate added to both about pages')
