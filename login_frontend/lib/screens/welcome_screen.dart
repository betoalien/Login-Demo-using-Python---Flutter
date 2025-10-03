import 'package:flutter/material.dart';
import 'login_screen.dart'; // Importamos la pantalla de login
import 'register_screen.dart'; // Importamos la pantalla de registro

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        // SafeArea asegura que el contenido no sea obstruido por muescas del teléfono (notches)
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            // Column apila los widgets verticalmente
            mainAxisAlignment: MainAxisAlignment.center, // Centra los widgets en el eje vertical
            crossAxisAlignment: CrossAxisAlignment.stretch, // Estira los widgets en el eje horizontal
            children: <Widget>[
              const Text(
                'Welcome to Login App!',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 48.0), // Un espacio vertical
              
              // Botón para Iniciar Sesión
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16.0),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                ),
                child: const Text('Login', style: TextStyle(fontSize: 18)),
                onPressed: () {
                  // Lógica de navegación para ir a la pantalla de Login
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const LoginScreen()),
                  );
                },
              ),
              const SizedBox(height: 16.0), // Espacio entre botones

              // Botón para Registrarse
              OutlinedButton(
                 style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16.0),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                ),
                child: const Text('Register', style: TextStyle(fontSize: 18)),
                onPressed: () {
                  // Lógica de navegación para ir a la pantalla de Registro
                   Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const RegisterScreen()),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}

