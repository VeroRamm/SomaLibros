function ingresar() {
    
  let t = document.getElementById("titulo").value;
  let a = document.getElementById("autor").value;
  let c = document.getElementById("categoria").value;
  let d = document.getElementById("descripcion").value;
  let i = document.getElementById("portada").value;
  let e = document.getElementById("editorial").value;
  let p = document.getElementById("precio").value;
  let s = document.getElementById("estado").value;
  
  let options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      titulo: t,
      autor: a,
      categoria: c,
      descripcion: d,
      portada: i,
      editorial: e,
      precio: p,
      estado: s
    })
  }
  fetch('http://127.0.0.1:5000/books', options)
    .then (function(){
      location.reload();
      alert("Libro ingresado");
      console.log("Libro ingresado");
    })
    .catch(function(err){
      console.log(err);

    })
}
    

  