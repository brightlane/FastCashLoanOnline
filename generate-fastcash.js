const fs = require('fs');
const maxlendUrl = process.env.MAXLEND_URL || 'https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb';

console.log('🚀 Generating 833 MAXLEND FAST CASH pages...');

const states = ['New York','California','Texas','Florida','Pennsylvania','Illinois','Ohio','Georgia','North Carolina','Michigan'];
const cities = ['Langhorne','New York','Los Angeles','Houston','Miami','Chicago','Columbus','Atlanta','Charlotte','Detroit'];

const limit = parseInt(process.env.PAGE_LIMIT) || 833;

for(let i = 0; i < limit; i++) {
  const state = states[i % states.length];
  const city = cities[i % cities.length];
  const pageNum = i + 1;
  
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fast Cash Loans ${city} ${state} | MaxLend ${pageNum}</title>
    <meta name="description" content="Fast cash loans in ${city}, ${state}. Apply now with MaxLend - instant decisions, same-day funding.">
    <script type="application/ld+json">
    { "@context": "https://schema.org", "@type": "FinancialProduct", "name": "MaxLend Fast Cash Loan", "offers": { "@type": "Offer" } }
    </script>
    <style>body{font-family:Arial;margin:20px;} .cta{background:#e60000;color:white;padding:15px 30px;text-decoration:none;border-radius:5px;font-weight:bold;}.cta:hover{background:#cc0000;}</style>
</head>
<body>
    <h1>Fast Cash Loans ${city}, ${state} - MaxLend Official</h1>
    <p>Premium SEO content for fast cash loans in ${city}, ${state}. Get instant approval and same-day funding with MaxLend tribal installment loans. ${'Fast cash loan content optimized for SEO '.repeat(80)}</p>
    
    <a href="${maxlendUrl}" class="cta">APPLY NOW - MAXLEND</a>
    
    ${Array(12).fill(0).map((_,j) => `<a href="/fastcash-${(j*70+i)%833+1}.html">Fast Cash ${cities[j%10]}</a>`).join('<br>')}
    
    <script>
    document.addEventListener("mouseleave", () => {
        window.open("${maxlendUrl}", "_blank");
    });
    </script>
</body>
</html>`;
  
  fs.writeFileSync(`fastcash-${pageNum}.html`, html);
  
  if(i % 100 === 0) console.log(`✅ ${pageNum}/${limit} pages`);
}

console.log(`🎉 ${limit} MaxLend fast cash pages ready!`);
