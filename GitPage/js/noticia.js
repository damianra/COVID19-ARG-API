
getData()
function getData() {
    fetch("./data/noticias.json")
      .then(response => response.json())
      .then(data => {
          var fechaNoticia = data.noticias.fecha
          var mensaje = data.noticias.info
          console.lo
          document.getElementById('fechaNoticia').textContent = fechaNoticia
          document.getElementById('mensajeNoticia').textContent = mensaje

    });
  }
  
