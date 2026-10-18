// Lädt Videos erst nach dem Klick (kein Netzwerkverkehr vorher), mit Untertitel-Spur.
document.querySelectorAll('.video[data-src]').forEach(function (el) {
  var btn = el.querySelector('.video-start');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var v = document.createElement('video');
    v.src = el.dataset.src; v.controls = true; v.autoplay = true; v.playsInline = true;
    v.preload = 'auto'; v.title = el.dataset.title;
    v.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#000';
    if (el.dataset.width) { v.width = +el.dataset.width; v.height = +el.dataset.height; }
    if (el.dataset.vtt) {
      var t = document.createElement('track');
      t.kind = 'captions'; t.srclang = 'de'; t.label = 'Deutsch'; t.src = el.dataset.vtt;
      v.appendChild(t);
    }
    btn.replaceWith(v);
  });
});
