import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  // Adjust to your backend host/port
  final String _baseUrl = 'http://192.168.9.116:5000/api';

  String? _accessToken;
  String? get accessToken => _accessToken;

  /// Registers a new user via POST /api/users/
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

      if (response.statusCode == 201) {
        print('✅ Registration successful');
        return true;
      } else {
        print('❌ Registration error [${response.statusCode}]: ${response.body}');
        return false;
      }
    } catch (e) {
      print('❌ Connection error (register): $e');
      return false;
    }
  }

  /// Logs in a user via POST /api/token (OAuth2PasswordRequestForm)
  /// Backend expects form fields: username, password
  Future<bool> login(String email, String password) async {
    final url = Uri.parse('$_baseUrl/token');

    try {
      final response = await http.post(
        url,
        headers: {
          // Important: form-encoded, not JSON
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: {
          'username': email,
          'password': password,
        },
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body) as Map<String, dynamic>;
        _accessToken = data['access_token'] as String?;
        if (_accessToken == null || _accessToken!.isEmpty) {
          print('❌ Login error: missing access_token in response');
          return false;
        }
        print('✅ Login successful, token stored in memory');
        return true;
      } else {
        print('❌ Login error [${response.statusCode}]: ${response.body}');
        return false;
      }
    } catch (e) {
      print('❌ Connection error (login): $e');
      return false;
    }
  }

  /// Optional helper to attach bearer token to requests
  Map<String, String> authHeaders({Map<String, String>? extra}) {
    final headers = <String, String>{
      'Accept': 'application/json',
      if (_accessToken != null) 'Authorization': 'Bearer $_accessToken',
    };
    if (extra != null) headers.addAll(extra);
    return headers;
  }

  /// Clears the in-memory token
  void logout() {
    _accessToken = null;
  }
}
