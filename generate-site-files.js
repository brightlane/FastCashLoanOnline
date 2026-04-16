// 🔥 GENERATE-SITE-FILES.JS - COMPLETE FAST CASH SITE
// All files needed for maximum SEO + conversions

const fs = require('fs');
const MAXLEND_URL = 'https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb';

console.log('🚀 Generating COMPLETE Fast Cash site...\n');

// 1. INDEX.HTML (Main Landing)
const indexHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>Fast Cash Loans Online | Same Day Funding | MaxLend</title>
<meta name="description" content="Fast cash loans online with instant approval. Same day funding nationwide. Bad credit OK. Apply now with MaxLend.">
<link rel="canonical" href="https://brightlane.github.io/FastCashLoanOnline/">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FinancialProduct","name":"Fast Cash Loans"}
</script>
<style>body{font-family:Arial;background:#f4f4f4;margin:0;padding:20px;max-width:900px;margin:auto;}
.cta{background:#e60000;color:white;padding:20px 40px;text-decoration:none;border-radius:8px;font-size:1.3em;font-weight:bold;display:inline-block;margin:20px 0;box-shadow:0 5px 15px rgba(230,0,0,0.4);}
.cta:hover{background:#cc0000;transform:scale(1.02);}
nav a{margin:0 15px;color:#004080;text-decoration:none;font-weight:bold;}
</style>
</head>
<body>
<nav><a href="/">Home</a><a href="/directory.html">Directory</a><a href="/blog.html">Blog</a><a href="/sitemap.xml">Sitemap</a></nav>
<header style="background:#004080;color:white;padding:40px;text-align:center;border-radius:10px;margin-bottom:30px;">
<h1>Fast Cash Loans Online</h1>
<p>Instant Approval • Same Day Funding • Nationwide</p>
<a href="${MAXLEND_URL}" class="cta">APPLY NOW - MAXLEND</a>
</header>
<section>
<h2>Why Choose Fast Cash Loans?</h2>
<p>Quick approval, no credit hassles, funds in your account same day. MaxLend tribal loans available in most states including Pennsylvania.</p>
<ul>
<li>Bad credit accepted</li>
<li>No hard credit pull</li>
<li>Direct lender</li>
<li>24/7 online application</li>
</ul>
<a href="/directory.html" style="background:#0066cc;color:white;padding:15px 30px;text-decoration:none;border-radius:5px;">Browse All Locations</a>
</section>
<footer style="margin-top:50px;padding:30px;background:#333;color:white;text-align:center;">
<p>&copy; 2026 FastCashLoanOnline | <a href="${MAXLEND_URL}">MaxLend Partner</a> | <a href="/privacy.html">Privacy</a></p>
</footer>
</body></html>`;
fs.writeFileSync('index.html', indexHtml);

// 2. BLOG.HTML
const blogHtml = `<!DOCTYPE html>
<html><head><title>Fast Cash Loan Blog | Tips & Guides</title><meta name="viewport" content="width=device-width"></head>
<body>
<h1>Fast Cash Loan Blog</h1>
${Array.from({length: 12}, (_,i) => `<article><h2>Fast Cash Tips #${i+1}</h2><p>Blog content for SEO. <a href="${MAXLEND_URL}">Apply MaxLend</a></p></article>`).join('')}
<a href="/directory.html">All Fast Cash Locations</a>
</body></html>`;
fs.writeFileSync('blog.html', blogHtml);

// 3. 404.HTML (SEO Gold)
const notFound = `<!DOCTYPE html>
<html><head><title>Page Not Found | Fast Cash Loans</title><meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="3;url=/directory.html">
</head><body>
<h1>404 - Page Moved</h1>
<p>Redirecting to <a href="/directory.html">Fast Cash Directory</a>...</p>
</body></html>`;
fs.writeFileSync('404.html', notFound);

// 4. PRIVACY.HTML
fs.writeFileSync('privacy.html', `<!DOCTYPE html><html><head><title>Privacy Policy</title></head><body><h1>Privacy Policy</h1><p>We respect your privacy. Affiliate links via MaxLend tracked responsibly.</p><a href="${MAXLEND_URL}">Fast Cash Loans</a></body></html>`);

// 5. STATES.HTML
const states = ['PA','NY','CA','TX','FL','IL','OH','GA','NC','MI'];
const statesHtml = `<!DOCTYPE html><html><head><title>Fast Cash Loans All States</title></head><body><h1>Fast Cash By State</h1>${states.map(s => `<a href="/directory.html#${s}">${s} Loans</a><br>`).join('')}<a href="${MAXLEND_URL}">Apply Now</a></body></html>`;
fs.writeFileSync('states.html', statesHtml);

// 6. NAP NAP NAP (Local SEO)
fs.writeFileSync('local-business.html', `<!DOCTYPE html><html><head><title>Fast Cash Philadelphia PA</title>
<script type="application/ld+json">{"@type":"LocalBusiness","name":"Fast Cash Loans","address":{"@type":"PostalAddress","addressLocality":"Philadelphia","addressRegion":"PA"}}</script></head>
<body><h1>Fast Cash Philadelphia PA</h1><a href="${MAXLEND_URL}">MaxLend Apply</a></body></html>`);

// 7. CRAWL-ME PAGE
fs.writeFileSync('crawl-me.html', `<!DOCTYPE html><html><head><title>Crawl Directory</title><meta name="robots" content="index,follow"></head>
<body><h1>SEO Crawl Hub</h1>${Array.from({length: 50}, (_,i) => `<a href="/fastcash-${i+1}.html">FastCash ${i+1}</a><br>`).join('')}<a href="${MAXLEND_URL}">MaxLend</a></body></html>`);

console.log('✅ 7 ESSENTIAL FILES CREATED:');
console.log('   index.html ✓ blog.html ✓ 404.html ✓ privacy.html');
console.log('   states.html ✓ local-business.html ✓ crawl-me.html');
console.log('   👉 Add to nav: Home | Directory | Blog | States | Sitemap');
console.log('\n🚀 DEPLOY NOW → git add . && git commit -m "Complete site files" && git push');
