getData()

var lastConfirmed 
let lastDeaths 
let lastRecovered
// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function charPor(){

var ctx = document.getElementById("myPieChart");

var myPieChart = new Chart(ctx, {
  
  type: 'doughnut',
  data: {
    labels: ["Confirmados", "Muertes", "Recuperados"],
    datasets: [{
      data: [lastConfirmed, lastDeaths, lastRecovered],
      backgroundColor: ['#36b9cc', '#e74a3b', '#1cc88a'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

}
function getData() {
  fetch("http://damianra.pythonanywhere.com/api/v1/ult-actualization")
    .then(response => response.json())
    .then(data => {
       lastConfirmed = data.data.casos;
       lastDeaths = data.data.muertes;
       lastRecovered = data.data.recuperados;
       charPor()
    });
}