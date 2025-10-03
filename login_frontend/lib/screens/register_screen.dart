import 'package.flutter/material.dart';
import '../services/auth_service.dart'; // Importamos nuestro servicio
import 'login_screen.dart'; // Importamos para la navegación

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  // Controladores para obtener el texto de los campos
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final AuthService _authService = AuthService();
  bool _isLoading = false;

  void _handleRegister() async {
    // Evitar múltiples envíos si ya se está procesando
    if (_isLoading) return;

    setState(() {
      _isLoading = true;
    });

    final email = _emailController.text;
    final password = _passwordController.text;

    // Pequeña validación para no enviar datos vacíos
    if (email.isEmpty || password.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Por favor, completa todos los campos')),
      );
      setState(() {
        _isLoading = false;
      });
      return;
    }

    bool success = await _authService.register(email, password);

    // Verificamos si el widget sigue "montado" antes de usar el context
    if (!mounted) return;

    setState(() {
      _isLoading = false;
    });

    if (success) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('¡Registro exitoso! Por favor, inicia sesión.')),
      );
      // Navegamos a la pantalla de login y reemplazamos la actual para que no pueda volver atrás
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => const LoginScreen()),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Error en el registro. El email ya puede existir.')),
      );
    }
  }

  @override
  void dispose() {
    // Limpiamos los controladores cuando el widget se destruye para liberar memoria
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Register'),
        elevation: 0,
        backgroundColor: Colors.transparent, // Hace la AppBar transparente
      ),
      body: Center(
        child: SingleChildScrollView( // Permite hacer scroll si el teclado cubre los campos
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Text(
                'Create your Account',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 48),
              
              // Campo para el Email
              TextField(
                controller: _emailController,
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(
                  labelText: 'Email',
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.email_outlined),
                ),
              ),
              const SizedBox(height: 16),

              // Campo para la Contraseña
              TextField(
                controller: _passwordController,
                obscureText: true, // Oculta el texto de la contraseña
                decoration: const InputDecoration(
                  labelText: 'Password',
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.lock_outline),
                ),
              ),
              const SizedBox(height: 24),

              // Botón de Registro
              ElevatedButton(
                onPressed: _isLoading ? null : _handleRegister, // Deshabilita el botón mientras carga
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16.0),
                ),
                child: _isLoading
                    ? const SizedBox(
                        height: 20,
                        width: 20,
                        child: CircularProgressIndicator(strokeWidth: 3, color: Colors.white),
                      )
                    : const Text('Register', style: TextStyle(fontSize: 18)),
              ),
              const SizedBox(height: 16),
              
              // Texto de "Olvidaste tu contraseña?"
              TextButton(
                onPressed: () {
                  // Lógica para recuperación de contraseña (se puede implementar en el futuro)
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Función no implementada todavía.')),
                  );
                },
                child: const Text('Forgot your password?'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

