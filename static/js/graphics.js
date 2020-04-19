let xLabels = []
let xCasesConfirmed = []
let xCasesDeaths = []
let xCasesRecovered = []
let xActives = []
let xCommunityTransmission =[]
let xImported =[]
let xTests = []

getData()

async function plotly(){
var Confirmados = {
  x: xLabels,
  y:  xCasesConfirmed,
  name: 'Confirmados',
  mode: 'lines+markers'
};

var Activos= {
  x: xLabels,
  y: xActives,
  name: 'Activos',
  mode: 'lines+markers'
};
var CasosMuertes = {
  x: xLabels,
  y: xCasesDeaths,
  mode: 'lines+markers',
  name: 'Muertes'

};

var TestConfirmados = {
  x: xLabels,
  y:  xCasesConfirmed,
  mode: 'lines+markers',
  name: 'Test Positivos'
};

var TestsTotales = {
  x: xLabels,
  y: xTests,
  mode: 'lines+markers',
  name: 'Tests Totales'
};
var CasosRecuperados = {
  x: xLabels,
  y: xCasesRecovered,
  mode: 'lines+markers',
  name: 'Recuperados'
};

var CasosImportados = {
  x: xLabels,
  y: xImported,
  mode: 'lines+markers',
  name: 'Casos Importados'
};

var CasosTrasmisionComunitaria = {
  x: xLabels,
  y: xCommunityTransmission,
  mode: 'lines+markers',
  name: 'Casos trasmisión coomunitaria'
};

var layout = {
  title:'Grafico casos totales vs casos activos'
};
var layout2 = {
  title:'Grafico tests positivos vs tests totales'
};
var layout3 = {
  title:'Grafico muertes vs recuperados'
};
var layout4 = {
  title:'Grafico casos importados vs casos trasmisión comunitaria '
};

var data = [Confirmados, Activos];
var data2 = [TestConfirmados, TestsTotales];
var data3 = [CasosRecuperados, CasosMuertes];
var data4 = [CasosImportados, CasosTrasmisionComunitaria];

Plotly.newPlot('plot', data, layout);
Plotly.newPlot('plot2', data2, layout2);
Plotly.newPlot('plot3', data3, layout3);

}

 function getData() {
  fetch("http://127.0.0.1:5000/api/v1/alldata")
    .then(response => response.json())
    .then(data => {
      data["data"].forEach(({date,cases,deaths,recovered,tests,communityTransmission,imported}) => {
        xCasesConfirmed.push(cases)
        xCasesDeaths.push(deaths)
        xCasesRecovered.push(recovered)
        xActives.push(cases - deaths- recovered)
        xLabels.push(date)
        xTests.push(tests)
        xImported.push(imported)
        xCommunityTransmission.push(communityTransmission)
      });

      plotly()
    });

  }
