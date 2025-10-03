import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  // Reemplaza esta URL si tu backend está en otro lugar.
  // 10.0.2.2 es la dirección para que el emulador de Android se conecte al localhost de tu computadora.
  final String _baseUrl = 'http://127.0.0.1:8000/api';

  Future<bool> register(String email, String password) async {
    final url = Uri.parse('$_baseUrl/users/');

    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'email': email,
          'password': password,
        }),
      );

      // El código 201 significa "Created" (Creado), que es lo que nuestra API devuelve si tiene éxito.
      if (response.statusCode == 201) {
        print('Registro exitoso');
        return true;
      } else {
        // Imprimimos el error para depuración
        print('Error en el registro: ${response.body}');
        return false;
      }
    } catch (e) {
      // Atrapamos errores de conexión (ej. si el servidor no está corriendo)
      print('Error de conexión: $e');
      return false;
    }
  }
}

