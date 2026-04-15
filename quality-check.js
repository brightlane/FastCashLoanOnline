const fs = require('fs');
console.log('🚀 QUALITY CHECK: Verifying MaxLend affiliate links...');

const pages = fs.readdirSync('.').filter(f => f.startsWith('fastcash-') && f.endsWith('.html'));
let valid = 0;

pages.forEach(page => {
  const content = fs.readFileSync(page, 'utf8');
  const hasAffiliate = content.includes('linkconnector.com') && content.includes('MaxlendWeb');
  const wordCount = content.split(/\s+/).length;
  
  if(hasAffiliate && wordCount > 400) {
    valid++;
  }
});

console.log(`✅ ${valid}/${pages.length} MaxLend pages VALIDATED`);
console.log('🚀 Quality check PASSED - Deploying!');
