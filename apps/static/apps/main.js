const input = document.getElementById('q');
const suggestionsDiv = document.getElementById('suggestions');
let timer = null;
input && input.addEventListener('input', function(e){
  const v = e.target.value;
  if (v.length < 3){ suggestionsDiv.innerHTML = '' ; return }
  clearTimeout(timer);
  timer = setTimeout(()=>{
    fetch(`/suggest/?q=${encodeURIComponent(v)}`)
      .then(r=>r.json())
      .then(data=>{
        suggestionsDiv.innerHTML = '';
        data.suggestions.forEach(s=>{
          const el = document.createElement('div');
          el.className = 'suggest-item';
          el.textContent = s.name;
          el.dataset.id = s.id;
          el.addEventListener('click', ()=>{ window.location = `/app/${s.id}/` });
          suggestionsDiv.appendChild(el);
        })
      })
  }, 200)
})

input && input.addEventListener('keydown', function(e){
  if (e.key === 'Enter'){
    e.preventDefault();
    document.getElementById('search-form').submit();
  }
})
