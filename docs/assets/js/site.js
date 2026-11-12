
(() => {
  const d=document;
  const menu=d.querySelector('[data-menu]');
  const nav=d.querySelector('.nav-links');
  menu?.addEventListener('click',()=>{const next=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(next));nav?.classList.toggle('is-open',next)});
  nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('is-open');menu?.setAttribute('aria-expanded','false')}));
  d.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){nav?.classList.remove('is-open');menu.setAttribute('aria-expanded','false');menu.focus()}});
  const progress=d.querySelector('.reading-line');
  const scroll=()=>{if(progress){const total=d.documentElement.scrollHeight-innerHeight;progress.style.width=(total>0?Math.min(100,scrollY/total*100):0)+'%'}};
  addEventListener('scroll',scroll,{passive:true});scroll();
  const appear=d.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');obs.unobserve(e.target)}}),{threshold:.08});appear.forEach(x=>obs.observe(x))}else appear.forEach(x=>x.classList.add('is-visible'));
  const buttons=[...d.querySelectorAll('[data-vlan]')];
  const info=d.querySelector('[data-vlan-detail]');
  function selectVlan(btn){buttons.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));if(!info)return;const title=info.querySelector('[data-vlan-title]'),desc=info.querySelector('[data-vlan-description]'),link=info.querySelector('[data-vlan-link]');if(title)title.textContent=btn.dataset.title||'';if(desc)desc.textContent=btn.dataset.description||'';if(link){link.href=btn.dataset.url||'#docs';link.textContent=btn.dataset.link||link.textContent}}
  buttons.forEach(btn=>btn.addEventListener('click',()=>selectVlan(btn)));if(buttons.length)selectVlan(buttons[0]);
  const filters=[...d.querySelectorAll('[data-filter]')];const photos=[...d.querySelectorAll('.photo[data-category]')];const counter=d.querySelector('[data-count]');
  function applyFilter(type){let count=0;photos.forEach(ph=>{const show=type==='all'||ph.dataset.category===type;ph.hidden=!show;if(show)count++});filters.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===type)));if(counter)counter.textContent=String(count);return count}
  filters.forEach(b=>b.addEventListener('click',()=>applyFilter(b.dataset.filter)));applyFilter('all');
  const dialog=d.querySelector('#gallery-dialog');const img=dialog?.querySelector('[data-dialog-image]');const title=dialog?.querySelector('[data-dialog-title]');const subtitle=dialog?.querySelector('[data-dialog-subtitle]');const prev=dialog?.querySelector('[data-prev]');const next=dialog?.querySelector('[data-next]');const close=dialog?.querySelector('[data-close]');
  let current=0;const visible=()=>photos.filter(x=>!x.hidden);
  function renderPhoto(index){const arr=visible();if(!arr.length)return;current=(index+arr.length)%arr.length;const p=arr[current];const pic=p.querySelector('img');if(img){img.src=pic.src;img.alt=pic.alt}if(title)title.textContent=p.dataset.title;if(subtitle)subtitle.textContent=p.dataset.note;if(prev)prev.disabled=arr.length<=1;if(next)next.disabled=arr.length<=1}
  photos.forEach(p=>p.addEventListener('click',()=>{current=visible().indexOf(p);renderPhoto(current);dialog?.showModal()}));
  prev?.addEventListener('click',()=>renderPhoto(current-1));next?.addEventListener('click',()=>renderPhoto(current+1));close?.addEventListener('click',()=>dialog?.close());
  dialog?.addEventListener('click',e=>{if(e.target===dialog)dialog.close()});
  dialog?.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();renderPhoto(current-1)}if(e.key==='ArrowRight'){e.preventDefault();renderPhoto(current+1)}});
})();
