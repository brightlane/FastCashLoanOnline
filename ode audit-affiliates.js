// audit-affiliates.js
const fs = require('fs');
const pages = fs.readdirSync('.').filter(f => f.endsWith('.html'));
let count = 0;
pages.forEach(p => {
  if (fs.readFileSync(p, 'utf8').includes('007949096598005765')) count++;
});
console.log(`✅ ${count}/${pages.length} pages have MaxLend affiliate`);
