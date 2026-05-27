/* zirconeey.github.io 弃用域名的最后一版 Service Worker —— "自杀 SW"
 *
 * 背景：本域名 2026-05-22 已停止更新，内容全站迁到 ruizhou03.github.io。
 * 静态页 index.html / 404.html 是跳转 stub。但老访客的浏览器仍持有当年
 * 注册的 SW + 缓存，于是 SW 拦截请求 → 命中旧缓存 → 用户看到几个月前的
 * 学习资料 / 百宝箱页面，且永远不会自动回到 ruizhou03。
 *
 * 修复路径：浏览器对 sw.js 永远会绕过自身做"无缓存"更新检查（每次导航 +
 * 24h 兜底）。我们利用这条把这份新 SW 推上去，老 SW 升级后：
 *   1. install → skipWaiting，避免老客户端 release 之前一直待命
 *   2. activate →
 *      a. 清空本域名下所有缓存
 *      b. clients.claim()  接管已打开的页面
 *      c. navigate 每个 client 让它重新发起导航请求
 *      d. registration.unregister()  以后再访问这个域名连 SW 都不挂
 *   3. fetch  仅在还没 unregister 完之前作为兜底，截到任何 navigate 直接
 *      返回硬编码跳转 HTML —— 用户瞬间被弹去 ruizhou03，对应路径保留
 */

const REDIRECT_HTML = `<!DOCTYPE html>
<html lang="zh"><head><meta charset="UTF-8">
<meta name="robots" content="noindex">
<title>已迁移 · ruizhou03.github.io</title>
<script>location.replace('https://ruizhou03.github.io'+location.pathname+location.search+location.hash);</script>
<meta http-equiv="refresh" content="0; url=https://ruizhou03.github.io/">
</head><body>本站已迁移到 <a href="https://ruizhou03.github.io/">ruizhou03.github.io</a>，正在跳转…</body></html>`;

self.addEventListener('install', () => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    // 1) 清掉本域名下所有历史 cache（含 zirconeey-pages-* / zirconeey-assets-*
    //    + 任何更早的命名空间），让老 HTML 副本彻底失效
    const names = await caches.keys();
    await Promise.all(names.map((n) => caches.delete(n)));

    // 2) 接管所有已打开的客户端，并触发它们重新导航
    //    重新导航会进 fetch handler，被下面的 REDIRECT_HTML 截胡
    await self.clients.claim();
    const all = await self.clients.matchAll({ type: 'window' });
    for (const c of all) {
      try { await c.navigate(c.url); } catch (_) { /* 跨域或权限错就放过 */ }
    }

    // 3) 注销自己。已派发出去的事件（包括上面的 navigate）继续走完，
    //    后续访问这个域名时浏览器不会再装 SW，直接走静态 stub
    try { await self.registration.unregister(); } catch (_) {}
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  // 只截顶层导航请求；图片 / JS / 字体之类不管，避免误伤兼容
  if (req.mode !== 'navigate') return;
  event.respondWith(
    new Response(REDIRECT_HTML, {
      status: 200,
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-store',
      },
    })
  );
});
