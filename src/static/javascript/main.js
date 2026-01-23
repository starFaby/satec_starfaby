import Index from "./index.js"
import NavbarDesplazamiento from "./navbar.js"
import Comentario from "./btnComentario.js"
// import Autocomplete from "./satec.js"
/** eventos */
import "./caracteresDispon.js"

$(document).ready(function () {
    const aux = new Index()
    aux.textVoz()

    /** Navbar de desplazamiento */
    const auxNavbarDesplazamiento = new NavbarDesplazamiento()
    auxNavbarDesplazamiento.nabDesplazamiento()
    auxNavbarDesplazamiento.menuDesplazamiento()

    /** Comentario */
    const auxComenatrio = new Comentario()
    auxComenatrio.viewComentario()
    /*
    // Ejemplo 1: Autocompletado de usuarios
    const autocompleteUsuarios = new Autocomplete(
        'buscarCanton',
        'sugerenciasCantones',
        '/crcnt'
    );
    
    // Ejemplo 2: Autocompletado de productos
    const autocompleteProductos = new Autocomplete(
        'buscarProducto',
        'sugerenciasProductos',
        '/buscar_productos'
    );
    */
    
    
})