import 'package:flutter/material.dart';

class LoggingComponent extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text(
          'Logging',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
