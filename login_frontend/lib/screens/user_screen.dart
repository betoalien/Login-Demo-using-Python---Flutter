import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class UserScreen extends StatelessWidget {
  final String email;

  const UserScreen({super.key, required this.email});

  @override
  Widget build(BuildContext context) {
    final String formattedDate =
    DateFormat('yyyy-MM-dd – kk:mm').format(DateTime.now());

    return Scaffold(
      appBar: AppBar(
        title: const Text('User Dashboard'),
        elevation: 0,
        backgroundColor: Colors.transparent,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Welcome $email',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 16),
              Text(
                'Last Login: $formattedDate',
                style: const TextStyle(
                  fontSize: 16,
                  color: Colors.grey,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
