import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  // Replace this URL if your backend is running elsewhere.
  // 10.0.2.2 is the special IP that allows the Android emulator
  // to access the localhost of your development machine.
  final String _baseUrl = 'http://192.168.9.116:5000/api';

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

      // 201 means "Created" — what our API returns if the registration is successful.
      if (response.statusCode == 201) {
        print('✅ Registration successful');
        return true;
      } else {
        // Log the error for debugging
        print('❌ Registration error: ${response.body}');
        return false;
      }
    } catch (e) {
      // Catch connection errors (e.g. if the server is not running)
      print('❌ Connection error: $e');
      return false;
    }
  }
}
