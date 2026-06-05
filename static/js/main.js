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

// Grafico de movimientos por mes

// ingresos
let labels_ingresos_fecha = Object.keys(df_fecha_ingreso);
let data_ingresos_fecha = Object.values(df_fecha_ingreso);

// gastos
let labels_gastos_fecha = Object.keys(df_fecha_gasto);
let data_gastos_fecha = Object.values(df_fecha_gasto);

// grafico gastos

let ctx4 = document.getElementById('lineChartMovimientos').getContext('2d');
let grafico_gastos_fecha = new Chart(ctx4, {
    type:"line",
    data:{
        labels: labels_gastos_fecha,
        datasets:[{
            label: 'Gastos',
            data: data_gastos_fecha,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
        },
        {
            label: 'Ingresos',
            data: data_ingresos_fecha,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
        }],
    },
})

// grafico doughnut ingresos x categoria 

// data_ingresos, labels_ingresos

let ctx5 = document.getElementById('financeChartCategory').getContext('2d');
let grafico_doughnut_ingresos = new Chart(ctx5, {
    type:"doughnut",
    data:{
        labels: labels_ingresos,
        datasets:[{
            label: 'Ingresos',
            data: data_ingresos,
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',   // cyan
                'rgba(99, 102, 241, 0.2)',   // indigo
                'rgba(168, 85, 247, 0.2)',   // violeta
                'rgba(34, 197, 94, 0.2)',    // verde
                'rgba(249, 115, 22, 0.2)',   // naranja
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(99, 102, 241, 1)',
                'rgba(168, 85, 247, 1)',
                'rgba(34, 197, 94, 1)',
                'rgba(249, 115, 22, 1)',
            ],
            borderWidth: 1,
        }],
    },
    options: {
    responsive: true,
    plugins: {
        legend: {
            position: 'bottom',
        },
        tooltip: {
            callbacks: {
                label: function(context) {
                    let label = context.label;
                    let dataArray = context.dataset.data;
                    let total = dataArray.reduce((a, b) => a + b, 0);
                    let currentValue = context.raw;
                    let percentage = ((currentValue / total) * 100).toFixed(1);
                    return label + ': ' + percentage + '%';
                }
            }
        }
    }
}
})