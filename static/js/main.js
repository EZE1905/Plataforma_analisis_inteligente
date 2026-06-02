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
    }, 500);
});