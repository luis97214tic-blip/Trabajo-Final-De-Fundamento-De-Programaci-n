Algoritmo Sistema_Elecciones
	
    Definir dni, verificarDni Como Entero
    Definir huella, voto, confirmacion Como Caracter
	
    // Registrar ciudadano
    Escribir "Ingrese su numero de DNI:"
    Leer dni
	
    // Verificar DNI
    Escribir "Verifique su numero de DNI:"
    Leer verificarDni
	
    Si dni = verificarDni Entonces
		
        // Verificar huella
        Escribir "Ingrese su huella digital:"
        Leer huella
		
        Escribir "Bienvenido al sistema"
		
        // Seleccionar voto
        Escribir "Seleccione su voto:"
        Escribir "voto1"
        Escribir "voto2"
        Escribir "voto3"
        Leer voto
		
        // Confirmar voto
        Escribir "Confirme su voto (SI/NO):"
        Leer confirmacion
		
        Si confirmacion = "SI" Entonces
            Escribir "Su voto se guardo correctamente."
        SiNo
            Escribir "El voto no fue registrado."
        FinSi
		
    SiNo
        Escribir "Los DNI no coinciden."
    FinSi
	
FinAlgoritmo

