#!/usr/bin/env python3
"""Sinh trang chủ (giới thiệu + hỗ trợ) của eze-site cho vi và en: python3 _tools/gen_landing.py

Sửa nội dung ở đây rồi chạy lại, đừng sửa tay index.html (hai bản ngôn ngữ sẽ lệch nhau).
"""
import html, os, sys

SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = "https://anhnh-design.github.io/eze/"
EMAIL = "anhnh.design@gmail.com"

C = {
 "vi": {
  "dir": "", "root": "", "other": "en/", "other_lang": "en", "other_label": "English",
  "store": "https://apps.apple.com/vn/app/id6838168921",
  "title": "EzE – Ghi chi tiêu bằng Action Button",
  "desc": "Chuyển khoản xong, bấm Action Button. EzE đọc màn hình ngay trên iPhone, ghi số tiền, người nhận và tự gắn danh mục. Không cần liên kết ngân hàng.",
  "nav": [("#features", "Tính năng"), ("#privacy", "Quyền riêng tư"), ("#pricing", "Giá"), ("#support", "Hỗ trợ")],
  "download": "Tải trên App Store",
  "eyebrow": "Ghi chi tiêu cho iPhone",
  "h1": "Bấm Action Button,<br>chi tiêu tự ghi",
  "lead": "Chuyển khoản xong, bấm một nút. EzE đọc màn hình xác nhận của app ngân hàng, ghi số tiền, người nhận và tự gắn danh mục. Không cần liên kết tài khoản ngân hàng.",
  "note": "Miễn phí · iPhone, iOS 18 trở lên",
  "hero_alt": "Thông báo EzE đã lưu khoản chuyển 128.000 đ vào danh mục Mua sắm",
  "how_eyebrow": "Cách hoạt động",
  "how_h2": "Ba giây sau khi trả tiền",
  "steps": [
   ("Trả tiền như mọi khi", "Chuyển khoản hay quét QR trong app ngân hàng, ví điện tử."),
   ("Bấm Action Button", "EzE chụp màn hình xác nhận và đọc chữ ngay trên iPhone."),
   ("Xong", "Giao dịch được lưu kèm danh mục. Một thẻ nhỏ hiện lên để bạn đổi danh mục nếu cần."),
  ],
  "tip": "iPhone không có Action Button? Dùng Chạm vào mặt lưng, Trung tâm điều khiển hoặc màn hình khoá. App có sẵn hướng dẫn cài đặt từng bước.",
  "features_eyebrow": "Tính năng",
  "features_h2": "Mọi thứ để biết tiền đi đâu",
  "features": [
   ("list", "Tự gắn danh mục cho mọi khoản chi",
    "EzE nhận ra cửa hàng và người nhận quen, rồi nhớ cách bạn phân loại để lần sau tự làm.",
    ["Từ điển tên cửa hàng Việt Nam, cập nhật thường xuyên", "Quy tắc theo người nhận: phân loại một lần, áp dụng mãi",
     "Đoán danh mục bằng Apple Intelligence ngay trên máy (máy hỗ trợ)"],
    "Danh sách giao dịch theo ngày, mỗi khoản có biểu tượng danh mục"),
   ("reports", "Biết tiền đi đâu mỗi tháng",
    "Tổng chi, tổng thu và chênh lệch theo ngày, tuần, tháng. Biểu đồ chi theo ngày và theo danh mục.",
    ["Chọn ngày bắt đầu tháng theo ngày nhận lương", "Xem riêng từng loại tiền, không quy đổi lẫn lộn",
     "Chạm vào một danh mục để xem từng giao dịch"],
    "Trang báo cáo tháng với biểu đồ chi theo ngày và biểu đồ tròn theo danh mục"),
   ("wallets", "Ví, thẻ tín dụng và quỹ tiết kiệm",
    "Theo dõi số dư từng ví, dư nợ thẻ và tiến độ tiết kiệm ở một chỗ.",
    ["Nhắc hạn thanh toán thẻ để không mất phí trễ hạn", "Chuyển tiền giữa các ví, trả thẻ, góp quỹ",
     "Ví không tính vào tổng cho thẻ tín dụng và tiết kiệm"],
    "Trang ví với tổng số dư, cảnh báo thẻ quá hạn và danh sách ví"),
   ("entry", "Trả tiền mặt? Nhập tay 3 giây",
    "Bàn phím số lớn, chọn danh mục một chạm. Nút “+” luôn ở góc màn hình.",
    ["Chia sẻ ảnh chụp màn hình vào EzE để ghi", "Xuất và nhập dữ liệu bằng Excel, CSV",
     "Nhập lịch sử chi tiêu từ Google Sheets"],
    "Màn nhập giao dịch với bàn phím số và danh sách danh mục"),
  ],
  "privacy_eyebrow": "Quyền riêng tư",
  "privacy_h2": "Dữ liệu của bạn ở lại trên iPhone",
  "privacy_sub": "EzE không có máy chủ lưu giao dịch. Chúng tôi không xem được dữ liệu của bạn.",
  "cards": [
   ("📱", "Chỉ lưu trên máy", "Giao dịch nằm trong iPhone của bạn, không đồng bộ lên máy chủ nào."),
   ("🏦", "Không đăng nhập ngân hàng", "Không tài khoản, không liên kết ngân hàng, không xin mật khẩu."),
   ("🖼️", "Ảnh đọc xong là bỏ", "Chữ được đọc ngay trên máy. Không lưu số tài khoản."),
   ("🔒", "Khoá bằng Face ID", "Che nội dung app khi bạn đưa máy cho người khác."),
  ],
  "privacy_link": "Đọc chính sách quyền riêng tư",
  "gallery_h2": "Xem qua EzE",
  "gallery_alts": ["Bấm Action Button, chi tiêu tự ghi", "Tự gắn danh mục cho mọi khoản chi", "Biết tiền đi đâu mỗi tháng",
                   "Ví, thẻ tín dụng và quỹ tiết kiệm", "Trả tiền mặt? Nhập tay 3 giây"],
  "pricing_eyebrow": "Giá",
  "pricing_h2": "Miễn phí để bắt đầu",
  "free": ("Miễn phí", "0 ₫", "Dùng mãi mãi",
           ["Ghi tự động và nhập tay không giới hạn", "Báo cáo đầy đủ", "Mỗi loại một ví: chi tiêu, thẻ tín dụng, tiết kiệm"]),
  "pro": ("EzE Pro", "Trọn đời", "99.000 ₫", "Trả một lần, không đăng ký",
          ["Mọi thứ của bản miễn phí", "Không giới hạn số ví", "Không quảng cáo", "Khôi phục trên iPhone khác cùng Apple ID"]),
  "support_eyebrow": "Hỗ trợ",
  "support_h2": "Câu hỏi thường gặp",
  "faq": [
   ("iPhone nào dùng được EzE?", "Mọi iPhone chạy iOS 18 trở lên. Action Button có trên iPhone 15 Pro, 15 Pro Max, dòng iPhone 16, 16e, dòng iPhone 17 và iPhone Air. Máy khác dùng Chạm vào mặt lưng, Trung tâm điều khiển hoặc màn hình khoá."),
   ("Dữ liệu của tôi lưu ở đâu?", 'Chỉ trên iPhone của bạn. App không có tài khoản và không có máy chủ lưu giao dịch. Xem <a href="privacy/">Chính sách quyền riêng tư</a>.'),
   ("Xoá app rồi cài lại có mất dữ liệu không?", "Có. App không có sao lưu iCloud riêng. Trước khi xoá app hoặc đổi máy, hãy vào <strong>Cài đặt › Xuất &amp; nhập dữ liệu</strong> để lưu file Excel hoặc CSV, rồi nhập lại ở máy mới."),
   ("Chụp màn hình bằng nút Tác vụ không chạy?", "Kiểm tra trong app Phím tắt: phím tắt EzE đã được gán cho nút Tác vụ (Cài đặt iOS › Nút Tác vụ) và đã chọn “Luôn cho phép” khi phím tắt hỏi quyền. Bạn có thể xem lại hướng dẫn trong <strong>Cài đặt › Xem lại hướng dẫn cài đặt</strong> của app."),
   ("Đã mua EzE Pro nhưng đổi máy?", "Mở màn hình EzE Pro và bấm <strong>Khôi phục giao dịch</strong>, dùng cùng Apple ID đã mua."),
  ],
  "contact_h3": "Liên hệ hỗ trợ",
  "contact_p": f'Gặp lỗi hoặc có góp ý? Viết cho chúng tôi: <a href="mailto:{EMAIL}">{EMAIL}</a>. Nếu có thể, hãy ghi kèm phiên bản app (cuối trang Cài đặt) và đời iPhone.',
  "cta_h2": "Bắt đầu ghi chi tiêu từ hôm nay",
  "cta_sub": "Một nút bấm sau mỗi lần trả tiền. Cuối tháng bạn biết tiền đã đi đâu.",
  "footer_privacy": "Quyền riêng tư", "footer_support": "Hỗ trợ",
 },
 "en": {
  "dir": "en/", "root": "../", "other": "../", "other_lang": "vi", "other_label": "Tiếng Việt",
  "store": "https://apps.apple.com/app/id6838168921",
  "title": "EzE – Log spending with the Action Button",
  "desc": "Paid? Press the Action Button. EzE reads the screen on your iPhone, logs the amount and recipient, and picks the category. No bank login.",
  "nav": [("#features", "Features"), ("#privacy", "Privacy"), ("#pricing", "Pricing"), ("#support", "Support")],
  "download": "Download on the App Store",
  "eyebrow": "Expense tracker for iPhone",
  "h1": "One press.<br>Spending logged.",
  "lead": "Paid by bank transfer? Press one button. EzE reads your banking app's confirmation screen, logs the amount and recipient, and picks the category. No bank account linking.",
  "note": "Free · iPhone, iOS 18 or later",
  "hero_alt": "EzE notification showing a ₫128,000 transfer saved under Shopping",
  "how_eyebrow": "How it works",
  "how_h2": "Three seconds after you pay",
  "steps": [
   ("Pay as usual", "Transfer or scan a QR code in your banking or e-wallet app."),
   ("Press the Action Button", "EzE captures the confirmation screen and reads it on your iPhone."),
   ("Done", "The transaction is saved with a category. A small card pops up so you can change it if needed."),
  ],
  "tip": "No Action Button? Use Back Tap, Control Center or the Lock Screen. The app walks you through setup step by step.",
  "features_eyebrow": "Features",
  "features_h2": "Everything to see where your money goes",
  "features": [
   ("list", "Every payment, auto-categorized",
    "EzE recognizes stores and the people you pay often, and remembers how you categorize them.",
    ["A merchant dictionary that is updated regularly", "Recipient rules: categorize once, applied from then on",
     "Category guesses with Apple Intelligence, on device (supported iPhones)"],
    "Transaction list grouped by day, each with a category icon"),
   ("reports", "See where your money goes",
    "Spending, income and net by day, week or month, with daily and per-category charts.",
    ["Start your month on payday", "Each currency on its own, never mixed",
     "Tap a category to see its transactions"],
    "Monthly report with a daily spending chart and a category donut"),
   ("wallets", "Wallets, cards and savings goals",
    "Track every wallet's balance, card debt and savings progress in one place.",
    ["Card due-date reminders, so you never pay late fees", "Move money between wallets, pay cards, fund goals",
     "Keep cards and savings out of your total"],
    "Wallets screen with total balance, an overdue card alert and the wallet list"),
   ("entry", "Paid in cash? Log it in 3 seconds",
    "A big number pad and one-tap categories. The “+” button is always in the corner.",
    ["Share a screenshot to EzE to log it", "Export and import with Excel or CSV",
     "Import your history from Google Sheets"],
    "Entry screen with a number pad and category list"),
  ],
  "privacy_eyebrow": "Privacy",
  "privacy_h2": "Your data stays on your iPhone",
  "privacy_sub": "EzE has no server holding your transactions. We cannot see your data.",
  "cards": [
   ("📱", "On device only", "Transactions live on your iPhone and never sync to a server."),
   ("🏦", "No bank login", "No account, no bank linking, no passwords."),
   ("🖼️", "Screenshots discarded", "Text is read on device. Account numbers are never stored."),
   ("🔒", "Face ID lock", "Hide the app's content when you hand your phone to someone."),
  ],
  "privacy_link": "Read the privacy policy",
  "gallery_h2": "A quick look",
  "gallery_alts": ["One press. Spending logged.", "Every payment, auto-categorized", "See where your money goes",
                   "Wallets, cards and savings goals", "Paid in cash? Log it in 3 seconds"],
  "pricing_eyebrow": "Pricing",
  "pricing_h2": "Free to start",
  "free": ("EzE", "Free", "Forever",
           ["Unlimited automatic and manual logging", "Full reports", "One wallet of each kind: spending, credit card, savings"]),
  "pro": ("EzE Pro", "Lifetime", "Pay once", "No subscription. Price shown in the App Store.",
          ["Everything in Free", "Unlimited wallets", "No ads", "Restore on another iPhone with the same Apple ID"]),
  "support_eyebrow": "Support",
  "support_h2": "Frequently asked questions",
  "faq": [
   ("Which iPhones can use EzE?", "Any iPhone on iOS 18 or later. The Action Button is on iPhone 15 Pro, 15 Pro Max, the iPhone 16 lineup, 16e, the iPhone 17 lineup and iPhone Air. Other models use Back Tap, Control Center or the Lock Screen."),
   ("Where is my data stored?", 'Only on your iPhone. The app has no account and no server holding your transactions. See the <a href="privacy/">Privacy Policy</a>.'),
   ("Will I lose my data if I delete and reinstall the app?", "Yes. The app has no iCloud backup of its own. Before deleting the app or switching phones, go to <strong>Settings › Export &amp; Import</strong> to save an Excel or CSV file, then import it on the new device."),
   ("The Action Button screenshot doesn't work?", "In the Shortcuts app, check that the EzE shortcut is assigned to the Action Button (iOS Settings › Action Button) and that you chose “Always Allow” when the shortcut asked for permission. You can replay the setup guide from <strong>Settings › Setup guide</strong> in the app."),
   ("Bought EzE Pro and switched phones?", "Open the EzE Pro screen and tap <strong>Restore purchase</strong>, using the same Apple ID you bought with."),
  ],
  "contact_h3": "Contact support",
  "contact_p": f'Found a bug or have feedback? Write to us at <a href="mailto:{EMAIL}">{EMAIL}</a>. If you can, include the app version (bottom of Settings) and your iPhone model.',
  "cta_h2": "Start tracking today",
  "cta_sub": "One press after every payment. At the end of the month, you know where it went.",
  "footer_privacy": "Privacy", "footer_support": "Support",
 },
}

GALLERY = ["01-hero", "02-list", "03-reports", "04-wallets", "05-entry"]


def page(lang):
    c = C[lang]
    r = c["root"]
    img = f"{r}assets/img/{lang}/"
    e = html.escape
    nav = "".join(f'<a class="opt" href="{h}">{e(t)}</a>' for h, t in c["nav"])
    steps = "".join(f'<div class="step"><h3>{e(t)}</h3><p>{e(p)}</p></div>' for t, p in c["steps"])
    feats = "".join(f'''
    <div class="feature">
      <div class="text">
        <h3>{e(t)}</h3>
        <p>{e(p)}</p>
        <ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul>
      </div>
      <div class="shot"><div class="phone sm"><img src="{img}screen-{k}.jpg" alt="{e(alt)}" width="1100" height="2390" loading="lazy"></div></div>
    </div>''' for k, t, p, items, alt in c["features"])
    cards = "".join(f'<div class="card"><div class="ic" aria-hidden="true">{ic}</div><h3>{e(t)}</h3><p>{e(p)}</p></div>' for ic, t, p in c["cards"])
    gallery = "".join(f'<img src="{img}{g}.jpg" alt="{e(a)}" width="1000" height="2174" loading="lazy">' for g, a in zip(GALLERY, c["gallery_alts"]))
    fname, fprice, fper, fitems = c["free"]
    pname, pbadge, pprice, pper, pitems = c["pro"]
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in c["faq"])
    url = BASE + c["dir"]
    alt_url = BASE + ("" if lang == "en" else "en/")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(c["title"])}</title>
  <meta name="description" content="{e(c["desc"])}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="{lang}" href="{url}">
  <link rel="alternate" hreflang="{c["other_lang"]}" href="{alt_url}">
  <meta name="apple-itunes-app" content="app-id=6838168921">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(c["title"])}">
  <meta property="og:description" content="{e(c["desc"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}assets/img/{lang}/01-hero.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{r}assets/icon.png">
  <link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
  <link rel="stylesheet" href="{r}assets/landing.css">
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="./"><img src="{r}assets/icon.png" alt="" width="32" height="32">EzE</a>
    <nav>{nav}<a href="{c["other"]}" hreflang="{c["other_lang"]}">{e(c["other_label"])}</a></nav>
  </div>
</header>

<main>
  <div class="hero">
    <div class="wrap">
      <div>
        <p class="eyebrow">{e(c["eyebrow"])}</p>
        <h1>{c["h1"]}</h1>
        <p class="lead">{e(c["lead"])}</p>
        <a class="btn" href="{c["store"]}">{e(c["download"])}</a>
        <p class="note">{e(c["note"])}</p>
      </div>
      <div class="shot"><div class="phone"><img src="{img}screen-hero-screen.jpg" alt="{e(c["hero_alt"])}" width="1100" height="2390"></div></div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <p class="eyebrow">{e(c["how_eyebrow"])}</p>
      <h2>{e(c["how_h2"])}</h2>
      <div class="steps">{steps}</div>
      <p class="tip">{e(c["tip"])}</p>
    </div>
  </section>

  <section id="features" class="soft">
    <div class="wrap">
      <p class="eyebrow">{e(c["features_eyebrow"])}</p>
      <h2>{e(c["features_h2"])}</h2>
      <div class="features">{feats}
      </div>
    </div>
  </section>

  <section id="privacy">
    <div class="wrap">
      <p class="eyebrow">{e(c["privacy_eyebrow"])}</p>
      <h2>{e(c["privacy_h2"])}</h2>
      <p class="sub">{e(c["privacy_sub"])} <a href="privacy/">{e(c["privacy_link"])}</a></p>
      <div class="cards">{cards}</div>
    </div>
  </section>

  <section class="soft">
    <div class="wrap">
      <h2 class="center">{e(c["gallery_h2"])}</h2>
      <div class="gallery">{gallery}</div>
    </div>
  </section>

  <section id="pricing">
    <div class="wrap center">
      <p class="eyebrow">{e(c["pricing_eyebrow"])}</p>
      <h2>{e(c["pricing_h2"])}</h2>
      <div class="plans" style="margin-top:40px">
        <div class="plan">
          <h3>{e(fname)}</h3>
          <div class="price">{e(fprice)}</div>
          <p class="per">{e(fper)}</p>
          <ul>{"".join(f"<li>{e(i)}</li>" for i in fitems)}</ul>
        </div>
        <div class="plan pro">
          <h3>{e(pname)}<span class="badge">{e(pbadge)}</span></h3>
          <div class="price">{e(pprice)}</div>
          <p class="per">{e(pper)}</p>
          <ul>{"".join(f"<li>{e(i)}</li>" for i in pitems)}</ul>
        </div>
      </div>
    </div>
  </section>

  <section id="support" class="soft">
    <div class="wrap">
      <div class="center">
        <p class="eyebrow">{e(c["support_eyebrow"])}</p>
        <h2>{e(c["support_h2"])}</h2>
      </div>
      <div class="faq" style="margin-top:32px">{faq}</div>
      <div class="contact">
        <h3>{e(c["contact_h3"])}</h3>
        <p>{c["contact_p"]}</p>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap">
      <img class="icon" src="{r}assets/icon.png" alt="" width="96" height="96" loading="lazy">
      <h2>{e(c["cta_h2"])}</h2>
      <p class="sub">{e(c["cta_sub"])}</p>
      <a class="btn lime" href="{c["store"]}">{e(c["download"])}</a>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <span>© 2026 EzE</span>
    <nav><a href="privacy/">{e(c["footer_privacy"])}</a><a href="#support">{e(c["footer_support"])}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{c["other"]}" hreflang="{c["other_lang"]}">{e(c["other_label"])}</a></nav>
  </div>
</footer>
</body>
</html>
'''


for lang in ("vi", "en"):
    path = os.path.join(SITE, C[lang]["dir"], "index.html")
    with open(path, "w") as f:
        f.write(page(lang))
    print("wrote", path)
