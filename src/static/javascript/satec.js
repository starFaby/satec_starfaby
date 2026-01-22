class Autocomplete {

    constructor(inputId, listId, endpoint) {
        this.input = document.getElementById(inputId);
        this.list = document.getElementById(listId);
        this.endpoint = endpoint;
        this.selectedIndex = -1;
        
        this.init();
    }
    
    init() {
        this.input.addEventListener('input', () => this.buscar());
        this.input.addEventListener('keydown', (e) => this.manejarTeclado(e));
        
        // Cerrar lista al hacer clic fuera
        document.addEventListener('click', (e) => {
            if (!this.input.contains(e.target) && !this.list.contains(e.target)) {
                this.ocultarLista();
            }
        });
    }
    
    async buscar() {
        const termino = this.input.value.trim();
        
        if (termino.length < 1) {
            this.ocultarLista();
            return;
        }
        
        try {
            const response = await fetch(`${this.endpoint}?q=${encodeURIComponent(termino)}`);

            const resultados = await response.json();

            this.mostrarResultados(resultados);
        } catch (error) {
            console.error('Error en la búsqueda:', error);
        }
    }
    
    mostrarResultados(resultados) {
        
        if (resultados.length === 0) {
            this.list.innerHTML = '<div class="autocomplete-item">No se encontraron resultados</div>';
            this.list.style.display = 'block';
            console.log("No tiene datos");
            return;
            
        }

        this.list.innerHTML = '';

        resultados.forEach((resultado, index) => {
            
            const item = document.createElement('div');
            item.className = 'autocomplete-item';
            item.textContent = resultado.nombre;
            item.dataset.index = index;

            item.addEventListener('click', () => this.seleccionarItem(resultado.nombre));
            item.addEventListener('mouseenter', () => this.resaltarItem(index));
            
            this.list.appendChild(item);
        });
        
        this.list.style.display = 'block';
        this.selectedIndex = -1;

    }

    seleccionarIdCanton(idCanton){
        print('idCanton')
        print(idCanton)
        print('idCanton')
    }
    
    resaltarItem(index) {
        const items = this.list.getElementsByClassName('autocomplete-item');
        
        // Remover clase activa de todos los items
        Array.from(items).forEach(item => {
            item.classList.remove('active');
        });
        
        // Agregar clase activa al item actual
        if (items[index]) {
            items[index].classList.add('active');
            this.selectedIndex = index;
        }
    }
    
    seleccionarItem(valor) {
        this.input.value = valor;
        this.ocultarLista();
        /* this.enviarSeleccion(valor);*/
    }
    
    manejarTeclado(event) {
        const items = this.list.getElementsByClassName('autocomplete-item');
        
        switch(event.key) {
            case 'ArrowDown':
                event.preventDefault();
                if (this.selectedIndex < items.length - 1) {
                    this.selectedIndex++;
                    this.resaltarItem(this.selectedIndex);
                }
                break;
                
            case 'ArrowUp':
                event.preventDefault();
                if (this.selectedIndex > 0) {
                    this.selectedIndex--;
                    this.resaltarItem(this.selectedIndex);
                }
                break;
                
            case 'Enter':
                event.preventDefault();
                if (this.selectedIndex >= 0 && items[this.selectedIndex]) {
                    this.seleccionarItem(items[this.selectedIndex].textContent);
                } else if (this.input.value.trim()) {
                    this.enviarSeleccion(this.input.value);
                }
                break;
                
            case 'Escape':
                this.ocultarLista();
                break;
        }
    }
    
    ocultarLista() {
        this.list.style.display = 'none';
        this.selectedIndex = -1;
    }
    
    async enviarSeleccion(seleccion) {
        try {
            const response = await fetch('/guardar_seleccion', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ seleccion: seleccion })
            });
            
            const data = await response.json();
            
            // Actualizar la UI con la selección
            const elementoId = this.input.id === 'buscarUsuario' 
                ? 'usuarioSeleccionado' 
                : 'productoSeleccionado';
            
            document.getElementById(elementoId).textContent = seleccion;
            
            // Mostrar mensaje de éxito
            alert(data.message);
            
        } catch (error) {
            console.error('Error al guardar selección:', error);
            alert('Error al guardar la selección');
        }
    }
}
export default Autocomplete;