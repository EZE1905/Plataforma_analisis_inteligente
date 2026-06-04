// cambiando el input de archivo para mostrar un succes 

let input_archivo = document.getElementById('file');
let label_archivo = document.getElementById('file-label');

input_archivo.addEventListener('change', function() {
    if (input_archivo.files.length > 0) {
        label_archivo.textContent = "✔ " + input_archivo.files[0].name;
        label_archivo.classList.add('file-selected');
    } else {
        label_archivo.textContent = 'Elegir archivo';
        label_archivo.classList.remove('file-selected');
    }
});

// Creando un loading spinner para mostrar mientras se procesa el archivo

const form = document.querySelector('.upload-form');
const loading = document.getElementById('loading');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    loading.classList.remove('hidden');

    setTimeout(() => {
        form.submit();
    }, 600);
});

// Graficos

let ingresos = ingresos_raw;
let gastos = gastos_raw;
let balance = balance_raw;

let ctx = document.getElementById('financeChart').getContext('2d');

let grafico = new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: ['Ingresos', 'Gastos', 'Balance'],
        datasets: [{
            label: 'Finanzas',
            data: [ingresos, gastos, balance],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom',
            },
        },
    }
})

// Grafico de gastos por categoria

// gastos
let labels_gastos = Object.keys(gasto_x_categoria);
let data_gastos = Object.values(gasto_x_categoria);

// ingresos
let labels_ingresos = Object.keys(ingreso_x_categoria);
let data_ingresos = Object.values(ingreso_x_categoria);

// grafico gastos

let ctx2 = document.getElementById('barChartGastos').getContext('2d');
let grafico_gastos = new Chart(ctx2, {
    type:"bar",
    data:{
        labels: labels_gastos,
        datasets:[{
            label: 'Gastos',
            data: data_gastos,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
        }],
    },
})

// grafico ingresos 

let ctx3 = document.getElementById('barChartIngresos').getContext('2d');
let grafico_ingresos = new Chart(ctx3, {
    type:"bar",
    data:{
        labels: labels_ingresos,
        datasets:[{
            label: 'Ingresos',
            data: data_ingresos,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
        }]
        },
    })