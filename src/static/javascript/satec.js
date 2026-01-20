document.addEventListener('DOMContentLoaded', function() {
    const productoInput = document.getElementById('producto');
    const suggestionsDiv = document.getElementById('suggestions');
    const selectedProductDiv = document.getElementById('selectedProduct');
    const detailNombre = document.getElementById('detailNombre');
    const detailCategoria = document.getElementById('detailCategoria');
    const detailPrecio = document.getElementById('detailPrecio');
    
    let timeoutId;
    let currentSearchTerm = '';
    
    // Función para buscar sugerencias
    async function buscarSugerencias(termino) {
        if (!termino.trim()) {
            suggestionsDiv.style.display = 'none';
            return;
        }
        
        try {
            const response = await fetch(`/autocomplete?q=${encodeURIComponent(termino)}`);
            const sugerencias = await response.json();
            
            mostrarSugerencias(sugerencias);
        } catch (error) {
            console.error('Error al buscar sugerencias:', error);
        }
    }
    
    // Función para mostrar sugerencias
    function mostrarSugerencias(sugerencias) {
        if (sugerencias.length === 0) {
            suggestionsDiv.innerHTML = `
                <div class="suggestion-item">
                    <div class="suggestion-main">No se encontraron resultados</div>
                    <div class="suggestion-details">Intenta con otro término de búsqueda</div>
                </div>
            `;
            suggestionsDiv.style.display = 'block';
            return;
        }
        
        suggestionsDiv.innerHTML = sugerencias.map(sug => `
            <div class="suggestion-item" data-value="${sug.value}" 
                data-categoria="${sug.categoria}" data-precio="${sug.precio}">
                <div class="suggestion-main">${sug.value}</div>
                <div class="suggestion-details">${sug.label}</div>
            </div>
        `).join('');
        
        suggestionsDiv.style.display = 'block';
        
        // Agregar event listeners a las sugerencias
        document.querySelectorAll('.suggestion-item').forEach(item => {
            item.addEventListener('click', function() {
                seleccionarProducto(
                    this.dataset.value,
                    this.dataset.categoria,
                    this.dataset.precio
                );
            });
        });
    }
    
    // Función para seleccionar un producto
    function seleccionarProducto(nombre, categoria, precio) {
        productoInput.value = nombre;
        suggestionsDiv.style.display = 'none';
        
        // Mostrar detalles del producto seleccionado
        detailNombre.textContent = nombre;
        detailCategoria.textContent = categoria;
        detailPrecio.textContent = `$${parseFloat(precio).toFixed(2)}`;
        
        selectedProductDiv.style.display = 'block';
    }
    
    // Evento de entrada en el campo de búsqueda
    productoInput.addEventListener('input', function() {
        const termino = this.value.trim();
        currentSearchTerm = termino;
        
        // Ocultar detalles del producto seleccionado
        selectedProductDiv.style.display = 'none';
        
        // Limpiar timeout anterior
        clearTimeout(timeoutId);
        
        // Esperar 300ms antes de buscar (debouncing)
        timeoutId = setTimeout(() => {
            if (termino === currentSearchTerm) {
                buscarSugerencias(termino);
            }
        }, 300);
    });
    
    // Ocultar sugerencias al hacer clic fuera
    document.addEventListener('click', function(event) {
        if (!productoInput.contains(event.target) && !suggestionsDiv.contains(event.target)) {
            suggestionsDiv.style.display = 'none';
        }
    });
    
    // Manejar teclas especiales
    productoInput.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            suggestionsDiv.style.display = 'none';
        }
        
        if (event.key === 'ArrowDown' && suggestionsDiv.style.display === 'block') {
            const firstSuggestion = suggestionsDiv.querySelector('.suggestion-item');
            if (firstSuggestion) firstSuggestion.focus();
        }
    });
});