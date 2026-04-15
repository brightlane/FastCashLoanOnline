const fs = require('fs');
let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

const pages = fs.readdirSync('.')
  .filter(f => f.startsWith('fastcash-') && f.endsWith('.html'))
  .sort();

pages.forEach(page => {
  const num = page.match(/fastcash-(\d+)\.html/)[1];
  sitemap += `<url><loc>/fastcash-${num}.html</loc><lastmod>${new Date().toISOString().split('T')[0]}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>`;
});

sitemap += '</urlset>';
fs.writeFileSync('sitemap.xml', sitemap);
fs.writeFileSync('robots.txt', 'User-agent: *\nAllow: /\nSitemap: /sitemap.xml');

console.log(`✅ Sitemap: ${pages.length} fast cash pages + robots.txt`);
