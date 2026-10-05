from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
changes={
'از ایدهٔ شما،<br>تا <em>قطعهٔ واقعی.</em>':'طراحی مهندسی،<br><em>ساخت قطعات سفارشی.</em>',
'مسیر پروژه‌ام را پیدا کنم':'بررسی مسیر اجرای پروژه',
'کاوش نمونه‌کارها':'مشاهده سوابق ساخت',
'از کجا<br>شروع کنیم؟':'بررسی اولیهٔ<br>نیازمندی‌های پروژه',
'سه انتخاب ساده، برای پیدا کردن خدمت و نمونه‌کار نزدیک به نیاز شما.':'با تعیین مرحلهٔ پروژه، حوزهٔ محصول و تعداد موردنیاز، خدمات و سوابق ساخت مرتبط معرفی می‌شوند.',
'نقطهٔ شروع پیشنهادی':'خدمت پیشنهادی برای بررسی اولیه',
'درباره پروژهٔ شما صحبت کنیم.':'بررسی فنی و امکان‌سنجی سفارش',
'دربارهٔ پروژهٔ شما صحبت کنیم.':'بررسی فنی و امکان‌سنجی سفارش',
'گفت‌وگو درباره سفارش مشابه':'درخواست بررسی سفارش مشابه',
'گفت‌وگو درباره پروژه':'درخواست بررسی پروژه',
'شروع یک پروژهٔ تازه.':'ارتباط با مجموعه و ارائهٔ درخواست ساخت',
'با ایده، عکس، نقشه یا نمونهٔ موجود تماس بگیرید؛ کامل‌بودن مدارک شرط شروع گفت‌وگو نیست.':'برای بررسی اولیه، ارائهٔ شرح نیاز، تصویر، نقشه یا نمونهٔ موجود کفایت می‌کند. مشخصات تکمیلی پیش از نهایی‌سازی سفارش تعیین خواهد شد.',
'درخواست دقیق‌تر، بررسی بهتر.':'تدوین درخواست فنی ساخت',
'متن آماده است؛ هنوز ارسال نشده.':'متن درخواست آماده شده است؛ ارسال توسط متقاضی انجام می‌شود.',
'روش مناسب برای هر محصول.':'انتخاب فرآیند متناسب با الزامات محصول',
'محصولات واقعی، مسیرهای متفاوت ساخت.':'سوابق طراحی و ساخت محصولات سفارشی',
'پیش از تولید،<br>مسیر را روشن می‌کنیم.':'تعیین الزامات فنی<br>پیش از آغاز تولید',
'نگاهی به ساخت':'شرح فنی و ملاحظات ساخت',
'کیفیت موردنیاز، هزینهٔ مناسب.':'انطباق مشخصات فنی و مدیریت هزینهٔ ساخت',
'از نیاز فنی شما،<br>تا مسیر روشن ساخت.':'بررسی سفارش‌های صنعتی<br>برای همکاری بین‌المللی',
'اگر نقشه کامل نداشته باشم چه می‌شود؟':'بررسی سفارش بدون نقشهٔ کامل چگونه انجام می‌شود؟',
'Your next part.<br><em>Made possible.</em>':'Engineering design.<br><em>Custom manufacturing.</em>',
'Find your project route':'Review project requirements',
'Where do<br>we start?':'Initial project<br>assessment',
'Three simple choices to find a relevant capability, a comparable project and a starting point for your inquiry.':'Specify the project stage, product category and required quantity to identify relevant services and manufacturing references.',
'Let’s define your next project.':'Technical inquiries and project assessment',
'Tell us what you need to make.':'Submit your manufacturing requirements.',
'A clearer brief. A better starting point.':'Preparation of a technical inquiry',
'Your brief is ready. It has not been sent.':'The inquiry has been prepared. Submission remains with the applicant.',
'Before you get started':'Information for prospective customers',
'Let’s':'Let us'
}
for p in list(R.rglob('*.html'))+[R/'professional.js',R/'route-guide.js']:
 s=p.read_text(encoding='utf-8-sig')
 for a,b in changes.items():s=s.replace(a,b)
 if p.suffix=='.html':
  s=re.sub(r'<link rel="preload" href="/Vazirmatn.woff2"[^>]*>','',s)
  if '/formal.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="/formal.css?v=20261005c"><link rel="preload" href="/assets/fonts/Estedad-variable.woff2" as="font" type="font/woff2" crossorigin></head>')
  if 'class="developer-credit"' not in s:s=s.replace('</footer>','<div class="container developer-credit" lang="fa" dir="rtl">توسعه توسط تیم تایگرو</div></footer>')
  s=re.sub(r'/(professional|route-guide)\.js\?v=[^" ]+',r'/\1.js?v=20261005c',s)
 p.write_text(s,encoding='utf8')
print('Formal copy, font references and developer credit applied')
