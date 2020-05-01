getData();

function getData() {
  fetch("http://damianra.pythonanywhere.com/api/v1/ult-actualization")
    .then(response => response.json())
    .then(data => {
      var lastConfirmed = data.data.casos;
      var lastDeaths = data.data.muertes;
      var lastRecovered = data.data.recuperados;
      var lastActives = data.data.casos - data.data.recuperados - data.data.muertes;
      SetData(lastConfirmed, lastDeaths, lastRecovered, lastActives)
    });
}

function SetData(confirmed, deaths, recovered, actives) {
  document.getElementById('confirmedLast').textContent = confirmed
  document.getElementById('deathsLast').textContent = deaths
  document.getElementById('recoveredLast').textContent = recovered
  document.getElementById('activesLast').textContent = actives
}