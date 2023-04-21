// Obtener el contenedor del contenido
var content = document.getElementById("content");

// Agregar algunos elementos iniciales
for (var i = 1; i <= 30; i++) {
    var item = document.createElement("div");
    item.className = "item";
    item.innerText = "Elemento " + i;
    content.appendChild(item);
}

// Agregar el evento scroll al objeto window
window.addEventListener("scroll", function () {
    // Verificar si el usuario ha llegado al final de la página
    if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight) {
        // Cargar más contenido dinámicamente
        for (var i = 11; i <= 20; i++) {
            var item = document.createElement("div");
            item.className = "item";
            item.innerText = "Elemento " + i;
            content.appendChild(item);
        }
    }
});
