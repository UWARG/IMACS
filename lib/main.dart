import 'package:flutter/material.dart';
import 'logging.dart';
import 'motor.dart';
import 'setup.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Split Screen Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Widget _currentScreen = HomeComponent();

  void _changeScreen(Widget screen) {
    setState(() {
      _currentScreen = screen;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Test Flutter App'),
      ),
      body: Column(
        children: [
          NavigationBar(onButtonPressed: _changeScreen),
          Expanded(child: _currentScreen),
        ],
      ),
    );
  }
}

class NavigationBar extends StatelessWidget {
  final Function(Widget) onButtonPressed;

  NavigationBar({required this.onButtonPressed});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.grey[200],
      child: Row(
        children: [
          NavButton(
            title: 'Home',
            onPressed: () {
              onButtonPressed(HomeComponent());
            },
          ),
          NavButton(
            title: 'Logging',
            onPressed: () {
              onButtonPressed(LoggingComponent());
            },
          ),
          NavButton(
            title: 'Setup',
            onPressed: () {
              onButtonPressed(SetupComponent());
            },
          ),
          NavButton(
            title: 'Motor',
            onPressed: () {
              onButtonPressed(MotorComponent());
            },
          ),
        ],
      ),
    );
  }
}

class NavButton extends StatelessWidget {
  final String title;
  final VoidCallback onPressed;

  NavButton({required this.title, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: TextButton(
        onPressed: onPressed,
        child: Text(
          title,
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}

class HomeComponent extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Center(
        child: Text(
          'Main Home Area',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
