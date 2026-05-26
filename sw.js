const CACHE='budgetio-v2';
const ASSETS=['/','index.html','manifest.json','sw.js'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
  if(e.request.url.includes('googleapis')||e.request.url.includes('fonts.google')||e.request.url.includes('gsi'))return;
  e.respondWith(caches.match(e.request).then(c=>c||fetch(e.request).then(r=>{
    if(r&&r.status===200&&r.type==='basic'){const cl=r.clone();caches.open(CACHE).then(c=>c.put(e.request,cl));}
    return r;
  })).catch(()=>caches.match('index.html')));
});
