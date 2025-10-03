import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart'; // Importamos nuestra nueva pantalla inicial

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // Este widget es la raíz de tu aplicación.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login App',
      theme: ThemeData(
        // Define el tema de la aplicación.
        // Usaremos un tema oscuro para un look moderno.
        brightness: Brightness.dark,
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      // La propiedad 'home' define qué widget se mostrará al iniciar la app.
      home: const WelcomeScreen(),
      // Ocultamos el banner de "Debug"
      debugShowCheckedModeBanner: false,
    );
  }
}
